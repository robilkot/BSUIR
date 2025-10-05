using backend.Model;
using backend.Repository;
using backend.Services;
using CommonLib.Models;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Concurrent;

namespace backend.Controllers;

[ApiController]
[Route("api/[controller]")]
public class SearchController(IndexRepository repo, NLPService nlpService, ILogger<SearchController> logger) : ControllerBase
{
    private readonly IndexRepository _indexRepository = repo;
    private readonly NLPService _nlpService = nlpService;
    private readonly ILogger<SearchController> _logger = logger;

    [HttpGet]
    [ProducesResponseType(StatusCodes.Status200OK)]
    [ProducesResponseType(StatusCodes.Status400BadRequest)]
    [ProducesResponseType(StatusCodes.Status500InternalServerError)]
    public async Task<IActionResult> Get(
        [FromQuery] string text,
        [FromQuery] DateTimeOffset? startDate,
        [FromQuery] DateTimeOffset? endDate,
        [FromQuery] int? pageSize,
        [FromQuery] int? page,
        IServiceScopeFactory serviceScopeFactory,
        CancellationToken cancellationToken)
    {
        SearchQuery query = new(text, startDate, endDate, page ?? 1, pageSize ?? 10);

        var documents = await _indexRepository.GetAllAsync(cancellationToken);
        var filter = await query.ToQueryFilter(_indexRepository, _nlpService, cancellationToken);

        if (filter is null)
        {
            return StatusCode(500, "NLP service did not respond");
        }

        ConcurrentBag<(double, Document, List<string>)> filteredDocs = [];

        List<Task> filterTasks = [];

        foreach (var document in documents)
        {
            var task = Task.Run(async () =>
            {
                var scope = serviceScopeFactory.CreateAsyncScope();
                var repo = scope.ServiceProvider.GetRequiredService<IndexRepository>();

                var (result, keywords) = await filter(document, repo);

                filteredDocs.Add((result, document, keywords));
            }, cancellationToken);

            filterTasks.Add(task);
        }

        await Task.WhenAll(filterTasks);

        var results = filteredDocs
            .Where(pair => pair.Item1 > 0.015)
            .OrderByDescending(pair => pair.Item1);

        List<(double, Document, List<string>)> total = [];

        if (pageSize != 0)
        {
            total = [.. results
            .Skip((query.Page - 1) * query.PageSize).Take(query.PageSize)];
        }
        else
        {
            total = [.. results];
        }

        _logger.LogInformation("Searching: {}. Returned {} results", text, total.Count);

        return Ok(total.ToSearchResults());
    }
}
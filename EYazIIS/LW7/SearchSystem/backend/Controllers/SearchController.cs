using backend.Model;
using backend.Repository;
using backend.Services;
using CommonLib.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Infrastructure;

[ApiController]
[Route("api/[controller]")]
public class SearchController : ControllerBase
{
    private readonly IndexRepository _indexRepository;
    private readonly NLPService _nlpService;

    public SearchController(IndexRepository repo, NLPService nlpService)
    {
        _nlpService = nlpService;
        _indexRepository = repo;
    }

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
        CancellationToken cancellationToken)
    {
        SearchQuery query = new(text, startDate, endDate, page ?? 1, pageSize ?? 10);

        var documents = await _indexRepository.GetAllAsync(cancellationToken);

        var filter = await query.ToQueryFilter(_indexRepository, _nlpService, cancellationToken);

        if(filter is null)
        {
            return StatusCode(500, "NLP service did not respond");
        }

        List<(double, Document)> filteredDocs = [];

        foreach (var document in documents)
        {
            filteredDocs.Add((await filter(document), document));
        }

        var results = filteredDocs
            .Where(pair => pair.Item1 > 0)
            .OrderByDescending(pair => pair.Item1)
            .Skip((query.Page - 1) * query.PageSize).Take(query.PageSize)
            .ToList();

        return Ok(await results.ToSearchResultsAsync(cancellationToken));
    }

    [HttpGet("health")]
    [ProducesResponseType(StatusCodes.Status200OK)]
    public IActionResult GetHealth()
    {
        return Ok(new
        {
            status = "healthy",
            timestamp = DateTimeOffset.UtcNow
        });
    }
}
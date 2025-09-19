using backend.Model;
using backend.Repository;
using CommonLib.Models;
using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("api/[controller]")]
public class SearchController : ControllerBase
{
    private readonly IndexRepository _indexRepository;

    public SearchController(IndexRepository repo)
    {
        _indexRepository = repo;
    }

    /// <summary>
    /// Searches through indexed documents based on the specified criteria
    /// </summary>
    /// <param name="text">Search text to look for</param>
    /// <param name="startDate">Optional start date filter</param>
    /// <param name="endDate">Optional end date filter</param>
    /// <param name="pageSize">Number of items per page (default: 10)</param>
    /// <param name="page">Page number (default: 1)</param>
    /// <param name="cancellationToken">Cancellation token for the operation</param>
    /// <returns>An asynchronous stream of search results</returns>
    [HttpGet]
    [ProducesResponseType(StatusCodes.Status200OK)]
    [ProducesResponseType(StatusCodes.Status400BadRequest)]
    public async Task<List<SearchResult>> Get(
        [FromQuery] string text,
        [FromQuery] DateTimeOffset? startDate,
        [FromQuery] DateTimeOffset? endDate,
        [FromQuery] int? pageSize,
        [FromQuery] int? page,
        CancellationToken cancellationToken)
    {
        SearchQuery query = new(text, startDate, endDate, page ?? 1, pageSize ?? 10);

        var documents = await _indexRepository.SearchAsync(query, cancellationToken);

        return await documents.ToSearchResultsAsync(cancellationToken);
    }

    /// <summary>
    /// Gets the current health status of the search endpoint
    /// </summary>
    /// <param name="cancellationToken">Cancellation token for the operation</param>
    /// <returns>Health status response</returns>
    [HttpGet("health")]
    [ProducesResponseType(StatusCodes.Status200OK)]
    public IActionResult GetHealth()
    {
        // Add health check logic here
        return Ok(new
        {
            status = "healthy",
            timestamp = DateTimeOffset.UtcNow
        });
    }
}
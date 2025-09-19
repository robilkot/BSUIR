using CommonLib.Models;
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text.Json;
using System.Threading.Tasks;

namespace frontend.Services;

public class ApiService
{
    private readonly HttpClient _httpClient;
    private const string BaseUrl = "http://localhost:5054/api/search";

    public ApiService()
    {
        _httpClient = new HttpClient
        {
            Timeout = TimeSpan.FromSeconds(30)
        };
    }

    public async Task<IEnumerable<SearchResult>> SearchAsync(SearchQuery request)
    {
        try
        {
            var queryString = System.Web.HttpUtility.ParseQueryString(string.Empty);
            queryString["page"] = request.Page.ToString();
            queryString["pageSize"] = request.PageSize.ToString();

            if (!string.IsNullOrEmpty(request.Text))
                queryString["text"] = request.Text;

            if (request.StartDate.HasValue)
                queryString["startDate"] = request.StartDate.Value.ToString("yyyy-MM-dd");

            if (request.EndDate.HasValue)
                queryString["endDate"] = request.EndDate.Value.ToString("yyyy-MM-dd");

            var url = $"{BaseUrl}?{queryString}";

            var response = await _httpClient.GetAsync(url);
            response.EnsureSuccessStatusCode();

            var content = await response.Content.ReadAsStringAsync();
            var results = JsonSerializer.Deserialize<IEnumerable<SearchResult>>(
                content,
                new JsonSerializerOptions { PropertyNameCaseInsensitive = true }
            );

            return results ?? [];
        }
        catch (Exception ex)
        {
            Console.WriteLine($"API Error: {ex.Message}");
            return [];
        }
    }
}
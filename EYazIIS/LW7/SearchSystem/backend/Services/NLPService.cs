using CommonLib.Models;

namespace backend.Services
{
    public class MetadataResponse
    {
        public required List<NamedEntity> Entities { get; set; }
        public required List<KeywordMetadata> Keywords { get; set; }
    }

    public class TextRequest
    {
        public required string Text { get; set; }
        public int? MaxKeywords { get; set; }
        public int? MaxEntities { get; set; }
    }

    public class NLPService
    {
        private readonly HttpClient _httpClient;

        public NLPService(HttpClient httpClient)
        {
            _httpClient = httpClient;
        }

        public async Task<MetadataResponse?> GetTextMetadataAsync(string text)
        {
            var request = new TextRequest() { Text = text };
            HttpResponseMessage response = await _httpClient.PostAsJsonAsync("extract-metadata", request);

            response.EnsureSuccessStatusCode();

            var responseContent = await response.Content.ReadFromJsonAsync<MetadataResponse>();

            return responseContent;
        }
    }
}

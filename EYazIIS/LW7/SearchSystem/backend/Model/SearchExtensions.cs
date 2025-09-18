using backend.DatetimeProviders;
using CommonLib.Models;

namespace backend.Model
{
    public delegate double DocumentFilter(Document document);
    
    public static class SearchExtensions
    {
        // AI NLP STUFF BEGIN

        // todo ranks document based on logical function on document metadata. use natasha for NER and keywords extraction
        public async static Task<DocumentFilter> ToQueryFilter(this SearchQuery document)
        {
            // extract keywords
            // account for TF-IDF
            // extract NER

            return doc => 0d;
        }

        public async static Task<DocumentMetadata> ToMetadataAsync(this Uri uri, CancellationToken cancellationToken = default)
        {
            // extract keywords (1.6 formula)
            // extract NER (natasha service)
            // tags = empty

            return new([], [], []);
        }

        // AI NLP STUFF END

        public static async Task<Document> ToDocumentAsync(this Uri uri, IDatetimeProvider datetimeProvider, CancellationToken cancellationToken = default)
            => new(uri.ToGuid(), uri, await uri.ToMetadataAsync(cancellationToken), datetimeProvider.Now);

        public static IEnumerable<(double relevance, Document document)> Filter(this IEnumerable<Document> documents, DocumentFilter filter)
            => documents
            .Select(doc => (relevance: filter(doc), doc))
            .Where(pair => pair.relevance > 0);

        public static async Task<SearchResult> ToSearchResult(this (double relevance, Document doc) pair)
            => new(pair.doc.Id, pair.doc.ToTitle(), await pair.doc.ToSnippet(), pair.doc.IndexedAt, pair.relevance);

        public async static IAsyncEnumerable<SearchResult> ToSearchResults(this IEnumerable<(double, Document)> documents)
        {
            foreach (var doc in documents)
            {
                yield return await doc.ToSearchResult();
            }
        }
    }
}

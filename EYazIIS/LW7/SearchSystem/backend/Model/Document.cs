using CommonLib.Models;
using System.Security.Cryptography;
using System.Text;

namespace backend.Model
{
    public static class SearchExtensions
    {
        public delegate double DocumentFilter(Document document);

        // AI NLP STUFF BEGIN

        // todo ranks document based on logical function on document metadata. use natasha for NER and keywords extraction
        public static DocumentFilter ToQueryFilter(this SearchQuery document)
        {
            return doc => 0d;
        }

        public async static Task<DocumentMetadata> ToMetadataAsync(this Uri uri, CancellationToken cancellationToken = default)
        {
            throw new NotImplementedException();
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

    public static class DocumentExtensions
    {
        public static Guid ToGuid(this Uri input)
        {
            byte[] inputBytes = Encoding.UTF8.GetBytes(input.AbsoluteUri);
            byte[] hashBytes = MD5.HashData(inputBytes);
            return new Guid(hashBytes);
        }

        public static string ToTitle(this Document doc)
            => Path.GetFileName(doc.Uri.LocalPath);

        public async static Task<string> ToSnippet(this Document doc)
            => (string)(await File.ReadAllTextAsync(doc.Uri.LocalPath)).Take(100);
    }
}

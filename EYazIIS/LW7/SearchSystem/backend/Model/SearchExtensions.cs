using backend.DatetimeProviders;
using backend.Repository;
using backend.Services;
using CommonLib.Models;
using System.Diagnostics.CodeAnalysis;

namespace backend.Model
{
    public delegate Task<double> DocumentFilter(Document document, IndexRepository repo);

    public class NamedEntityComparer : IEqualityComparer<NamedEntity>
    {
        private static readonly NamedEntityComparer _instance = new();
        public static NamedEntityComparer Instance => _instance;

        public bool Equals(NamedEntity? x, NamedEntity? y) => x?.NormalizedText == y?.NormalizedText;
        public int GetHashCode([DisallowNull] NamedEntity obj) => obj.NormalizedText.GetHashCode();
    }

    public static class SearchExtensions
    {   
        public async static Task<DocumentFilter?> ToQueryFilter(this SearchQuery query, IndexRepository repository, NLPService nlp, CancellationToken cancellationToken = default)
        {
            var queryMetadata = await nlp.GetTextMetadataAsync(query.Text);

            if (queryMetadata is null)
            {
                return null;
            }

            var documentsCount = await repository.GetDocumentsCount(cancellationToken);

            
            async Task<double> filter(Document doc, IndexRepository repo)
            {
                // account for TF-IDF
                var documentTfIdf = new Dictionary<string, double>();

                foreach (var keyword in doc.Metadata.Keywords)
                {
                    var lexeme = await repo.GetByTextAsync(keyword.Text, cancellationToken);

                    var tf = keyword.Frequency;
                    var idf = Math.Log(documentsCount / lexeme!.ContainingDocuments);
                    var tfidf = tf * idf;

                    documentTfIdf.Add(lexeme.Text, tfidf);
                }
                
                double keywordsScore = 0;

                foreach(var keyword in queryMetadata.Keywords)
                {
                    if(documentTfIdf.TryGetValue(keyword.Text, out double tfidf))
                    {
                        keywordsScore += tfidf;
                    }
                }


                double totalScore = 0;

                if (queryMetadata.Entities.Count == 0)
                {
                    totalScore = keywordsScore;
                }
                else
                {
                    // account for named entities
                    var foundNerCount = doc.Metadata.NamedEntities
                        .Intersect(queryMetadata.Entities, NamedEntityComparer.Instance)
                        .Count();

                    double nerScore = foundNerCount / queryMetadata.Entities.Count;

                    totalScore = 0.3 * nerScore + 0.7 * keywordsScore;
                }

                return totalScore;
            }

            return filter;
        }

        public async static Task<DocumentMetadata> ToMetadataAsync(this Uri uri, NLPService nlp, CancellationToken cancellationToken = default)
        {
            string content = await File.ReadAllTextAsync(uri.LocalPath, cancellationToken);

            var metadataResponse = await nlp.GetTextMetadataAsync(content);
            // todo handle errors
            
            var metadata = new DocumentMetadata([.. metadataResponse.Keywords], [.. metadataResponse.Entities]);

            return metadata;
        }
        

        public static async Task<Document> ToDocumentAsync(this Uri uri, 
            IDatetimeProvider datetimeProvider, 
            NLPService nlp, 
            CancellationToken cancellationToken = default)
            => new(uri.ToGuid(), uri, await uri.ToMetadataAsync(nlp, cancellationToken), datetimeProvider.Now);

        public static async Task<SearchResult> ToSearchResult(this (double relevance, Document doc) pair, CancellationToken cancellationToken = default)
            => new(pair.doc.Id, pair.doc.Uri, pair.doc.ToTitle(), await pair.doc.ToSnippetAsync(cancellationToken) ?? "Ошибка чтения документа", pair.doc.IndexedAt, pair.relevance);

        public async static Task<List<SearchResult>> ToSearchResultsAsync(this IEnumerable<(double, Document)> documents, CancellationToken cancellationToken = default)
        {
            var result = new List<SearchResult>();

            foreach (var doc in documents)
            {
                result.Add(await doc.ToSearchResult(cancellationToken));
            }

            return result;
        }
    }
}

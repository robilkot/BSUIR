using backend.DatetimeProviders;
using backend.Repository;
using backend.Services;
using CommonLib.Models;
using System.Diagnostics.CodeAnalysis;

namespace backend.Model
{
    public delegate Task<(double relevance, List<string> keywords)> DocumentFilter(Document document, IndexRepository repo);

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

            
            async Task<(double, List<string>)> filter(Document doc, IndexRepository repo)
            {
                // account for TF-IDF
                double keywordsScore = 0;
                List<string> matches = [];

                foreach (var keyword in doc.Metadata.Keywords)
                {
                    if(!queryMetadata.Keywords.Any(kw => kw.Text == keyword.Text))
                    {
                        continue;
                    }
                        
                    var lexeme = await repo.GetByTextAsync(keyword.Text, cancellationToken);

                    var tf = keyword.Frequency;
                    var idf = Math.Log(documentsCount / lexeme!.ContainingDocuments) + 0.7;
                    var tfidf = tf * idf;

                    keywordsScore += tfidf;
                    matches.Add(keyword.Text);
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

                return (totalScore, matches);
            }

            return filter;
        }

        public async static Task<DocumentMetadata?> ToMetadataAsync(this Uri uri, NLPService nlp, CancellationToken cancellationToken = default)
        {
            try
            {
                string content = await File.ReadAllTextAsync(uri.LocalPath, cancellationToken);

                var metadataResponse = await nlp.GetTextMetadataAsync(content);

                if(metadataResponse is null)
                {
                    return null;
                }

                var metadata = new DocumentMetadata([.. metadataResponse.Keywords], [.. metadataResponse.Entities]);

                return metadata;
            }
            catch (Exception)
            {
                return null;
            }
        }
        
        public static async Task<Document?> ToDocumentAsync(this Uri uri, 
            IDatetimeProvider datetimeProvider, 
            NLPService nlp, 
            CancellationToken cancellationToken = default)
        {
            var metadata = await uri.ToMetadataAsync(nlp, cancellationToken);

            if(metadata is null)
            {
                return null;
            }

            var doc = new Document(uri.ToGuid(), uri, metadata, datetimeProvider.Now);
            return doc;
        }

        public static SearchResult ToSearchResult(this (double relevance, Document doc, List<string> keywords) pair)
            => new(pair.doc.Id, pair.doc.Uri, pair.doc.ToTitle(), pair.doc.IndexedAt, pair.keywords);

        public static IEnumerable<SearchResult> ToSearchResults(this IEnumerable<(double, Document, List<string> keywords)> documents)
            => documents.Select(doc => doc.ToSearchResult());
    }
}

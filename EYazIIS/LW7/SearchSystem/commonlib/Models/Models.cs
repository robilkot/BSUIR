using System.Collections.Immutable;

namespace CommonLib.Models;

public record SearchResult(Guid DocumentId, Uri Uri, string Title, DateTimeOffset IndexedAt, List<string> KeywordMatches);

public enum NamedEntityType
{
    PERSON = 1,
    LOCATION = 2,
    ORGANISATION = 3,
};

public record NamedEntity(string Text, NamedEntityType Type, string NormalizedText);

public record KeywordMetadata(string Text, double Frequency);
public record DocumentMetadata(ImmutableList<KeywordMetadata> Keywords, ImmutableList<NamedEntity> NamedEntities);

public class Document
{
#pragma warning disable CS8618 // Поле, не допускающее значения NULL, должно содержать значение, отличное от NULL, при выходе из конструктора. Рассмотрите возможность добавления модификатора "required" или объявления значения, допускающего значение NULL.
    public Document()
#pragma warning restore CS8618 // Поле, не допускающее значения NULL, должно содержать значение, отличное от NULL, при выходе из конструктора. Рассмотрите возможность добавления модификатора "required" или объявления значения, допускающего значение NULL.
    {
        
    }
    public Document(Guid guid, Uri uri, DocumentMetadata metadaa, DateTimeOffset indexedAt)
    {
        Id = guid;
        Uri = uri;
        Metadata = metadaa;
        IndexedAt = indexedAt;
    }

    public Guid Id { get; init; }
    public Uri Uri { get; init; }
    public DocumentMetadata Metadata { get; set; }
    public DateTimeOffset IndexedAt { get; set; }
};

public record SearchQuery(string Text, DateTimeOffset? StartDate, DateTimeOffset? EndDate, int Page = 1, int PageSize = 10);

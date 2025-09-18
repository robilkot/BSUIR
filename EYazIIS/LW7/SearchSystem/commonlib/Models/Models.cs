using System.Collections.Immutable;

namespace CommonLib.Models;

// Not tracked by EF Core, can remain a record
public record SearchResult(Guid DocumentId, Uri Uri, string Title, string Snippet, DateTimeOffset IndexedAt, double Relevance);

// Polymorphic base for NER
public abstract record NamedEntity;
public sealed record Name(string Text) : NamedEntity;
public sealed record Location(string Text) : NamedEntity;
public sealed record Organization(string Text) : NamedEntity;

public record DocumentMetadata(ImmutableList<string> Keywords, ImmutableList<NamedEntity> NamedEntities, ImmutableList<string> Tags);
public class Document
{
    public Document()
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

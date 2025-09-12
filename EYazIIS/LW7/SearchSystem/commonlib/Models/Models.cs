using System.Collections.Immutable;

namespace CommonLib.Models;

public record SearchResult(Guid DocumentId, string Title, string Snippet, DateTimeOffset IndexedAt, double Relevance);

public abstract record NamedEntity;
public sealed record Name(string Text) : NamedEntity;
public sealed record Location(string Text) : NamedEntity;
public sealed record Organization(string Text) : NamedEntity;

public record DocumentMetadata(ImmutableList<string> Keywords, ImmutableList<NamedEntity> NamedEntities, ImmutableList<string> Tags);
public record Document(Guid Id, Uri Uri, DocumentMetadata Metadata, DateTimeOffset IndexedAt);

public record SearchQuery(string Text, DateTimeOffset? StartDate, DateTimeOffset? EndDate, int Page = 1, int PageSize = 10);

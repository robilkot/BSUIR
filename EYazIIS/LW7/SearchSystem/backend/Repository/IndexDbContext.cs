using backend.Model;
using CommonLib.Models;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.ChangeTracking;
using System.Collections.Immutable;
using System.Text.Json;

namespace backend.Repository;

public static class Comparers<T>
{
    private static ValueComparer<ImmutableList<T>>? _comparer;
    public static ValueComparer<ImmutableList<T>> Get()
    {
        _comparer ??= new((c1, c2) => c1!.SequenceEqual(c2!), c => c.GetHashCode(), c => c);
        return _comparer;
    }
}

public class IndexDbContext : DbContext
{
    public IndexDbContext(DbContextOptions<IndexDbContext> options) : base(options)
    {
    }

    public DbSet<LexemeMetadata> Lexemes { get; set; }
    public DbSet<Document> Documents { get; set; }


    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<LexemeMetadata>(entity =>
        {
            entity.HasKey(l => l.Text);

            entity.Property(l => l.ContainingDocuments);
        });

        modelBuilder.Entity<Document>(entity =>
        {
            entity.HasKey(d => d.Id);

            entity.ComplexProperty(d => d.Metadata, property =>
            {
                property.Property(m => m.Keywords)
                    .HasConversion(
                        v => JsonSerializer.Serialize(v, JsonSerializerOptions.Default),
                        v => JsonSerializer.Deserialize<ImmutableList<KeywordMetadata>>(v, JsonSerializerOptions.Default)!,
                        Comparers<KeywordMetadata>.Get());

                property.Property(m => m.NamedEntities)
                    .HasConversion(
                        v => JsonSerializer.Serialize(v, JsonSerializerOptions.Default),
                        v => JsonSerializer.Deserialize<ImmutableList<NamedEntity>>(v, JsonSerializerOptions.Default)!,
                        Comparers<NamedEntity>.Get());
            });
        });
    }
}
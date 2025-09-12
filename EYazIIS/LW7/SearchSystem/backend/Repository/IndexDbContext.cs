using CommonLib.Models;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.ChangeTracking;
using System.Collections.Immutable;
using System.Text.Json;

namespace backend.Repository;

public class IndexDbContext : DbContext
{
    public IndexDbContext(DbContextOptions<IndexDbContext> options) : base(options)
    {
    }

    public DbSet<Document> Documents { get; set; }

    private static ValueComparer<ImmutableList<T>> GetEqualityComparer<T>()
        => new((c1, c2) => c1.SequenceEqual(c2), c => c.GetHashCode(), c => c);

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Document>(entity =>
        {
            entity.HasKey(d => d.Id);

            entity.ComplexProperty(d => d.Metadata, property =>
            {
                property.Property(m => m.Keywords)
                    .HasConversion(
                        v => string.Join(";", v),
                        v => v.Split(';', StringSplitOptions.RemoveEmptyEntries).ToImmutableList(),
                        GetEqualityComparer<string>());

                property.Property(m => m.Tags)
                    .HasConversion(
                        v => string.Join(";", v),
                        v => v.Split(';', StringSplitOptions.RemoveEmptyEntries).ToImmutableList(),
                        GetEqualityComparer<string>());

                property.Property(m => m.NamedEntities)
                    .HasConversion(
                        v => JsonSerializer.Serialize(v, (JsonSerializerOptions)null),
                        v => JsonSerializer.Deserialize<ImmutableList<NamedEntity>>(v, (JsonSerializerOptions)null),
                        GetEqualityComparer<NamedEntity>());
            });

            // todo: Indexes for substring search
            //entity.HasIndex(m => m.Metadata.Keywords)
            //    .HasDatabaseName("IX_DocumentMetadata_Keywords");
            //entity.HasIndex(m => m.Metadata.Tags)
            //    .HasDatabaseName("IX_DocumentMetadata_Tags");
            //entity.HasIndex(m => m.Metadata.NamedEntities)
            //    .HasDatabaseName("IX_DocumentMetadata_NamedEntities");
        });
    }
}
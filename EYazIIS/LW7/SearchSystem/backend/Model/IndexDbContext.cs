using CommonLib.Models;
using Microsoft.EntityFrameworkCore;
using System.Collections.Immutable;
using System.Text.Json;

namespace backend.Model;

public class IndexDbContext : DbContext
{
    public IndexDbContext(DbContextOptions<IndexDbContext> options) : base(options)
    {
    }

    public DbSet<Document> Documents { get; set; }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        // Document entity
        modelBuilder.Entity<Document>(entity =>
        {
            entity.HasKey(d => d.Id);

            // One-to-one relationship: Document <-> DocumentMetadata
            entity.OwnsOne(d => d.Metadata, md =>
            {
                // Store Keywords as concatenated string for LIKE search
                md.Property(m => m.Keywords)
                    .HasConversion(
                        v => string.Join(";", v),
                        v => v.Split(';', StringSplitOptions.RemoveEmptyEntries).ToImmutableList())
                    .HasColumnType("nvarchar(max)");

                // Store NamedEntities as JSON for LIKE search
                md.Property(m => m.NamedEntities)
                    .HasConversion(
                        v => JsonSerializer.Serialize(v, (JsonSerializerOptions)null),
                        v => JsonSerializer.Deserialize<ImmutableList<NamedEntity>>(v, (JsonSerializerOptions)null))
                    .HasColumnType("nvarchar(max)");

                // Store Tags as concatenated string for LIKE search
                md.Property(m => m.Tags)
                    .HasConversion(
                        v => string.Join(";", v),
                        v => v.Split(';', StringSplitOptions.RemoveEmptyEntries).ToImmutableList())
                    .HasColumnType("nvarchar(max)");

                // Indexes for substring search
                md.HasIndex(m => m.Keywords)
                    .HasDatabaseName("IX_DocumentMetadata_Keywords");
                md.HasIndex(m => m.Tags)
                    .HasDatabaseName("IX_DocumentMetadata_Tags");
                md.HasIndex(m => m.NamedEntities)
                    .HasDatabaseName("IX_DocumentMetadata_NamedEntities");
            });
        });
    }
}
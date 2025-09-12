using CommonLib.Models;
using Microsoft.EntityFrameworkCore;
using System.Linq.Expressions;

namespace backend.Model
{
    public class IndexRepository : IIndexRepository
    {
        private readonly IndexDbContext _context;

        public IndexRepository(IndexDbContext context)
        {
            _context = context;
        }

        public async Task<Document?> GetByIdAsync(Guid id, CancellationToken cancellationToken = default)
            => await _context.Documents
            .Include(d => d.Metadata)
            .FirstOrDefaultAsync(d => d.Id == id, cancellationToken);

        public async Task<IEnumerable<Document>> GetAllAsync(CancellationToken cancellationToken = default)
            => await _context.Documents
            .Include(d => d.Metadata)
            .ToListAsync(cancellationToken);

        public async Task AddAsync(Document document, CancellationToken cancellationToken = default)
        {
            await _context.Documents.AddAsync(document, cancellationToken);
            await _context.SaveChangesAsync(cancellationToken);
        }

        public async Task UpdateAsync(Document document, CancellationToken cancellationToken = default)
        {
            _context.Documents.Update(document);
            await _context.SaveChangesAsync(cancellationToken);
        }

        public async Task DeleteAsync(Guid id, CancellationToken cancellationToken = default)
        {
            var document = await GetByIdAsync(id, cancellationToken);
            if (document != null)
            {
                _context.Documents.Remove(document);
                await _context.SaveChangesAsync(cancellationToken);
            }
        }

        public async Task<IEnumerable<Document>> FindAsync(Expression<Func<Document, bool>> predicate, CancellationToken cancellationToken = default)
            => await _context.Documents
            .Include(d => d.Metadata)
            .Where(predicate)
            .ToListAsync(cancellationToken);

        public async Task<IEnumerable<Document>> SearchAsync(SearchQuery query, CancellationToken cancellationToken = default)
        {
            var filter = query.ToQueryFilter();

            var documents = _context.Documents
                .Filter(filter)
                .Skip(0) // todo
                .Take(query.PageSize)
                .AsQueryable();

            var filteredDocuments = documents
                .OrderByDescending(pair => pair.relevance)
                .Select(pair => pair.document);

            return await filteredDocuments.ToListAsync(cancellationToken);
        }
    }
}

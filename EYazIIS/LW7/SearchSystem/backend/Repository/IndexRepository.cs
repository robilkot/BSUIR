using backend.Model;
using backend.Services;
using CommonLib.Models;
using Microsoft.EntityFrameworkCore;

namespace backend.Repository
{
    public class IndexRepository
    {
        private readonly IndexDbContext _context;
        private readonly NLPService _nlpService;

        public IndexRepository(IndexDbContext context, NLPService nlpService)
        {
            _context = context;
            _nlpService = nlpService;
        }

        public async Task<LexemeMetadata?> GetByTextAsync(string text, CancellationToken cancellationToken = default)
            => await _context.Lexemes.FirstOrDefaultAsync(l => l.Text == text, cancellationToken);

        public async Task<Document?> GetByIdAsync(Guid id, CancellationToken cancellationToken = default)
            => await _context.Documents
            .FirstOrDefaultAsync(d => d.Id == id, cancellationToken);

        public async Task<IEnumerable<Document>> GetAllAsync(CancellationToken cancellationToken = default)
            => await _context.Documents
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

        public async Task<List<(double relevance, Document doc)>> SearchAsync(SearchQuery query, CancellationToken cancellationToken = default)
        {
            var filter = await query.ToQueryFilter(this, _nlpService, cancellationToken);

            // todo optimize
            var documents = await _context.Documents.ToListAsync();

            var results = documents
                .Select(doc => (filter(doc), doc))
                .Where(pair => pair.Item1 > 0)
                .OrderByDescending(pair => pair.Item1)
                .Skip((query.Page - 1) * query.PageSize).Take(query.PageSize)
                .ToList();

            return results;
        }

        public async Task<int> GetDocumentsCount(CancellationToken cancellationToken)
        {
            return await _context.Documents.CountAsync(cancellationToken);
        }
    }
}

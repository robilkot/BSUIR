using backend.Model;
using CommonLib.Models;
using Microsoft.EntityFrameworkCore;

namespace backend.Repository
{
    public class IndexRepository
    {
        private readonly IndexDbContext _context;

        public IndexRepository(IndexDbContext context)
        {
            _context = context;
        }

        public async Task AddAsync(LexemeMetadata lexeme, CancellationToken cancellationToken = default)
        {
            _context.Lexemes.Add(lexeme);
            await _context.SaveChangesAsync(cancellationToken);
        }
        public async Task UpdateAsync(LexemeMetadata lexeme, CancellationToken cancellationToken = default)
        {
            _context.Lexemes.Update(lexeme);
            await _context.SaveChangesAsync(cancellationToken);
        }
        public async Task<LexemeMetadata?> GetByTextAsync(string text, CancellationToken cancellationToken = default)
            => await _context.Lexemes.FirstOrDefaultAsync(l => l.Text == text, cancellationToken);
        
        public async Task DeleteAsync(LexemeMetadata lexeme, CancellationToken cancellationToken = default)
        {
            _context.Lexemes.Remove(lexeme);
            await _context.SaveChangesAsync();
        }

        public async Task<Document?> GetByIdAsync(Guid id, CancellationToken cancellationToken = default)
            => await _context.Documents.FirstOrDefaultAsync(d => d.Id == id, cancellationToken);

        public async Task<List<Document>> GetAllAsync(CancellationToken cancellationToken = default)
            => await _context.Documents.ToListAsync(cancellationToken);

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

        public async Task<int> GetDocumentsCount(CancellationToken cancellationToken)
        {
            return await _context.Documents.CountAsync(cancellationToken);
        }
    }
}

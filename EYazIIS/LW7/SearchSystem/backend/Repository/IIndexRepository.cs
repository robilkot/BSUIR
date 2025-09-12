using CommonLib.Models;

namespace backend.Repository
{
    public interface IIndexRepository
    {
        Task<Document?> GetByIdAsync(Guid id, CancellationToken cancellationToken = default);
        Task<IEnumerable<Document>> GetAllAsync(CancellationToken cancellationToken = default);
        Task AddAsync(Document document, CancellationToken cancellationToken = default);
        Task UpdateAsync(Document document, CancellationToken cancellationToken = default);
        Task DeleteAsync(Guid id, CancellationToken cancellationToken = default);
        Task<IEnumerable<Document>> SearchAsync(SearchQuery query, CancellationToken cancellationToken = default);
    }
}

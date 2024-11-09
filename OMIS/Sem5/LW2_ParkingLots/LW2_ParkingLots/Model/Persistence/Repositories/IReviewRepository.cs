using LW2_ParkingLots.Model.Entities;

namespace LW2_ParkingLots.Model.Persistence.Repositories
{
    public interface IReviewRepository
    {
        public Task<Review> GetReviewAsync(int id);
        public Task<Review> AddReviewAsync(Review review);
        public Task<List<Review>> GetReviewsAsync(int page);
        public Task DeleteReviewAsync(int id);
    }
}

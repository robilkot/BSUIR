using LW2_ParkingLots.Model.Entities;

namespace LW2_ParkingLots.Model.Persistence.Repositories
{
    public class ReviewRepository : IReviewRepository
    {
        public Task<Review> AddReviewAsync(Review review)
        {
            throw new NotImplementedException();
        }

        public Task DeleteReviewAsync(int id)
        {
            throw new NotImplementedException();
        }

        public Task<Review> GetReviewAsync(int id)
        {
            throw new NotImplementedException();
        }

        public Task<List<Review>> GetReviewsAsync(int page)
        {
            throw new NotImplementedException();
        }
    }
}

using LW2_ParkingLots.Model.Entities;

namespace LW2_ParkingLots.Model.Persistence.Repositories
{
    public class ReviewRepository : IReviewRepository
    {
        private static readonly List<Review> _reviews = [
            new(1, "Bad review", 1, DateTime.Now),
            new(2, "It was great", 5, DateTime.Now),
            new(3, "Mediocre review", 3, DateTime.Now),
            new(4, "Good review", 4, DateTime.Now),
            ];

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
            return Task.FromResult(_reviews.First(review => review.Id == id)); 
        }

        public Task<List<Review>> GetReviewsAsync(int page)
        {
            return Task.FromResult(_reviews.ToList());
        }
    }
}

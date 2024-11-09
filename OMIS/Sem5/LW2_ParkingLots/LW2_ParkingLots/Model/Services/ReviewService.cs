using LW2_ParkingLots.Model.Entities;
using LW2_ParkingLots.Model.Persistence.Repositories;

namespace LW2_ParkingLots.Model.Services
{
    public class ReviewService(IReviewRepository repository) : IReviewService
    {
        private readonly IReviewRepository _repository = repository;
        public async Task<Review> AddReviewAsync(Review review)
        {
            return await _repository.AddReviewAsync(review);
        }

        public async Task DeleteReviewAsync(int id)
        {
            await _repository.DeleteReviewAsync(id);
        }

        public async Task<Review> GetReviewAsync(int id)
        {
            return await _repository.GetReviewAsync(id);
        }

        public async Task<List<Review>> GetReviewsAsync(int page)
        {
            return await _repository.GetReviewsAsync(page);
        }
    }
}

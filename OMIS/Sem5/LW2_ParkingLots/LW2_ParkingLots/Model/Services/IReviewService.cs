using LW2_ParkingLots.Model.Entities;

namespace LW2_ParkingLots.Model.Services
{
    public interface IReviewService
    {
        Task<Review> AddReviewAsync(Review review);
        Task DeleteReviewAsync(int id);
        Task<Review> GetReviewAsync(int id);
        Task<List<Review>> GetReviewsAsync(int page);
    }
}
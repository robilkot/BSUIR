
using LW2_ParkingLots.Model.Persistence.Repositories;

namespace LW2_ParkingLots.Model.Services
{
    public class PaymentService(IPaymentRepository repo) : IPaymentService
    {
        private readonly IPaymentRepository _repo = repo;
        public async Task ProcessPayment(int userId, decimal amount, int parkingLotId)
        {
            await _repo.ProcessPayment(userId, amount, parkingLotId);
        }
    }
}


namespace LW2_ParkingLots.Model.Services
{
    public interface IPaymentService
    {
        Task ProcessPayment(int userId, decimal amount, int parkingLotId);
    }
}
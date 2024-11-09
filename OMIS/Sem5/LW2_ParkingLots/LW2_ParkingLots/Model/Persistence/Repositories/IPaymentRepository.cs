namespace LW2_ParkingLots.Model.Persistence.Repositories
{
    public interface IPaymentRepository
    {
        public Task ProcessPayment(int userId, decimal amount, int parkingLotId);
    }
}

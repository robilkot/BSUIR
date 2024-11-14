using LW2_ParkingLots.Model.Entities;

namespace LW2_ParkingLots.Model.Persistence.Repositories
{
    public class ParkingLotRepository : IParkingLotRepository
    {
        private static List<ParkingLot> _lots = [
            new ParkingLot(1, ParkingLotStatus.Available, ParkingLotType.Regular, false, 10, DateTime.Now, DateTime.Now),
            new ParkingLot(2, ParkingLotStatus.Available, ParkingLotType.Truck, false, 10, DateTime.Now, DateTime.Now),
            new ParkingLot(3, ParkingLotStatus.Reserved, ParkingLotType.Truck, false, 30, DateTime.Now, DateTime.Now),
            new ParkingLot(4, ParkingLotStatus.Occupied, ParkingLotType.Regular, false, 30, DateTime.Now, DateTime.Now),
            new ParkingLot(5, ParkingLotStatus.Occupied, ParkingLotType.Motorcycle, true, 30, DateTime.Now, DateTime.Now),
            new ParkingLot(6, ParkingLotStatus.Reserved, ParkingLotType.Motorcycle, false, 20, DateTime.Now, DateTime.Now),
            new ParkingLot(7, ParkingLotStatus.Available, ParkingLotType.Truck, true, 20, DateTime.Now, DateTime.Now),
            ];

        public Task<bool> AddLotToUserAsync(int parkingLotId, int userId)
        {
            throw new NotImplementedException();
        }

        public Task<ParkingLot> CreateParkingLotAsync()
        {
            throw new NotImplementedException();
        }

        public Task DeleteParkingLotAsync(int id)
        {
            throw new NotImplementedException();
        }

        public Task<ParkingLot> GetParkingLotAsync(int id)
        {
            return Task.FromResult(_lots.First(x => x.Id == id));
        }

        public Task<List<ParkingLot>> GetParkingLotWithFilterAsync(ParkingLotFilter filter, int parkingZoneId)
        {
            return Task.FromResult(_lots.ToList());
        }

        public Task<bool> SetTimeToLotAsync(int parkingLotId, int userId, DateTime startTime, DateTime endTime)
        {
            throw new NotImplementedException();
        }

        public Task<ParkingLot> UpdateParkingLotAsync(ParkingLot parkingLot)
        {
            throw new NotImplementedException();
        }
    }
}

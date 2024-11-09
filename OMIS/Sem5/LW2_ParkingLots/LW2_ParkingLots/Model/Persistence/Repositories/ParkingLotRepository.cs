using LW2_ParkingLots.Model.Entities;

namespace LW2_ParkingLots.Model.Persistence.Repositories
{
    public class ParkingLotRepository : IParkingLotRepository
    {
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
            throw new NotImplementedException();
        }

        public Task<List<ParkingLot>> GetParkingLotWithFilterAsync(ParkingLotFilter filter, int parkingZoneId)
        {
            throw new NotImplementedException();
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

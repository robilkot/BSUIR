using LW2_ParkingLots.Model.Entities;

namespace LW2_ParkingLots.Model.Persistence.Repositories
{
    public interface IParkingLotRepository
    {
        public Task<ParkingLot> GetParkingLotAsync(int id);
        public Task<ParkingLot> CreateParkingLotAsync();
        public Task DeleteParkingLotAsync(int id);
        public Task<List<ParkingLot>> GetParkingLotWithFilterAsync(ParkingLotFilter filter, int parkingZoneId);
        public Task<ParkingLot> UpdateParkingLotAsync(ParkingLot parkingLot);
        public Task<bool> AddLotToUserAsync(int parkingLotId, int userId); // todo: user id int?
        public Task<bool> SetTimeToLotAsync(int parkingLotId, int userId, DateTime startTime, DateTime endTime); // todo: wtf
    }
}

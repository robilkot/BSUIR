using LW2_ParkingLots.Model.Entities;
using LW2_ParkingLots.Model.Persistence;

namespace LW2_ParkingLots.Model.Services
{
    public interface IParkingLotService
    {
        Task<bool> AddLotToUserAsync(int parkingLotId, int userId);
        Task<ParkingLot> CreateParkingLotAsync();
        Task DeleteParkingLotAsync(int id);
        Task<ParkingLot> GetParkingLotAsync(int id);
        Task<List<ParkingLot>> GetParkingLotWithFilterAsync(ParkingLotFilter filter, int parkingZoneId);
        Task<bool> SetTimeToLotAsync(int parkingLotId, int userId, DateTime startTime, DateTime endTime);
        Task<ParkingLot> UpdateParkingLotAsync(ParkingLot parkingLot);
    }
}
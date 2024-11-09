using LW2_ParkingLots.Model.Entities;

namespace LW2_ParkingLots.Model.Services
{
    public interface IZoneService
    {
        Task AddParkingLotToZoneAsync(int parkingZoneId, ParkingLot parkingLot);
        Task<ParkingZone> AddParkingZoneAsync(ParkingZone parkingZone);
        Task DeleteParkingLotFromZoneAsync(int parkingZoneId, ParkingLot parkingLot);
        Task DeleteParkingZoneAsync(int parkingZoneId);
        Task<ParkingZone> GetParkingZoneAsync(int parkingZoneId);
        Task<List<ParkingZone>> GetZonesAsync();
        Task<ParkingZone> SearchZoneByParkingLotAsync(int parkingLotId);
        Task<ParkingZone> UpdateParkingZoneAsync(ParkingZone parkingZone);
    }
}
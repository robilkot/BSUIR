using LW2_ParkingLots.Model.Entities;

namespace LW2_ParkingLots.Model.Persistence.Repositories
{
    public interface IZoneRepository
    {
        public Task<List<ParkingZone>> GetZonesAsync();
        public Task<ParkingZone> GetParkingZoneAsync(int parkingZoneId);
        public Task<ParkingZone> AddParkingZoneAsync(ParkingZone parkingZone);
        public Task DeleteParkingZoneAsync(int parkingZoneId);
        public Task<ParkingZone> UpdateParkingZoneAsync(ParkingZone parkingZone);
        public Task AddParkingLotToZoneAsync(int parkingZoneId, ParkingLot parkingLot);
        public Task DeleteParkingLotFromZoneAsync(int parkingZoneId, ParkingLot parkingLot);
        public Task<ParkingZone> SearchZoneByParkingLotAsync(int parkingLotId);
    }
}

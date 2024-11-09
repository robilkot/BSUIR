using LW2_ParkingLots.Model.Entities;
using LW2_ParkingLots.Model.Persistence.Repositories;

namespace LW2_ParkingLots.Model.Services
{
    public class ZoneService(IZoneRepository repo) : IZoneService
    {
        private readonly IZoneRepository _zoneRepository = repo;
        public async Task AddParkingLotToZoneAsync(int parkingZoneId, ParkingLot parkingLot)
        {
            await _zoneRepository.AddParkingLotToZoneAsync(parkingZoneId, parkingLot);
        }

        public async Task<ParkingZone> AddParkingZoneAsync(ParkingZone parkingZone)
        {
            return await _zoneRepository.AddParkingZoneAsync(parkingZone);
        }

        public async Task DeleteParkingLotFromZoneAsync(int parkingZoneId, ParkingLot parkingLot)
        {
            await _zoneRepository.DeleteParkingLotFromZoneAsync(parkingZoneId, parkingLot);
        }

        public async Task DeleteParkingZoneAsync(int parkingZoneId)
        {
            await _zoneRepository.DeleteParkingZoneAsync(parkingZoneId);
        }

        public async Task<ParkingZone> GetParkingZoneAsync(int parkingZoneId)
        {
            return await _zoneRepository.GetParkingZoneAsync(parkingZoneId);
        }

        public async Task<List<ParkingZone>> GetZonesAsync()
        {
            return await _zoneRepository.GetZonesAsync();
        }

        public async Task<ParkingZone> SearchZoneByParkingLotAsync(int parkingLotId)
        {
            return await _zoneRepository.SearchZoneByParkingLotAsync(parkingLotId);
        }

        public async Task<ParkingZone> UpdateParkingZoneAsync(ParkingZone parkingZone)
        {
            return await _zoneRepository.UpdateParkingZoneAsync(parkingZone);
        }
    }
}

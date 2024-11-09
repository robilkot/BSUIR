using LW2_ParkingLots.Model.Entities;

namespace LW2_ParkingLots.Model.Persistence.Repositories
{
    public class ZoneRepository : IZoneRepository
    {
        private static List<ParkingZone> _zonesList = []; // todo init
        private static int MaxId => _zonesList.Max(z => z.Id);
        public Task AddParkingLotToZoneAsync(int parkingZoneId, ParkingLot parkingLot)
        {
            _zonesList.WithId(parkingZoneId).ParkingLots.Add(parkingLot);

            return Task.CompletedTask;
        }

        public Task<ParkingZone> AddParkingZoneAsync(ParkingZone parkingZone)
        {
            parkingZone.Id = MaxId + 1;
            
            _zonesList.Add(parkingZone);

            return Task.FromResult(parkingZone);
        }

        public Task DeleteParkingLotFromZoneAsync(int parkingZoneId, ParkingLot parkingLot)
        {
            _zonesList.WithId(parkingZoneId).ParkingLots.Remove(parkingLot);

            return Task.CompletedTask;
        }

        public Task DeleteParkingZoneAsync(int parkingZoneId)
        {
            _zonesList.Remove(_zonesList.WithId(parkingZoneId));

            return Task.CompletedTask;
        }

        public Task<ParkingZone> GetParkingZoneAsync(int parkingZoneId)
        {
            return Task.FromResult(_zonesList.WithId(parkingZoneId));
        }

        public Task<List<ParkingZone>> GetZonesAsync()
        {
            return Task.FromResult(_zonesList.ToList());
        }

        public Task<ParkingZone> SearchZoneByParkingLotAsync(int parkingLotId)
        {
            return Task.FromResult(_zonesList.First(z => z.ParkingLots.Any(p => p.Id == parkingLotId)));
        }

        public Task<ParkingZone> UpdateParkingZoneAsync(ParkingZone parkingZone)
        {
            _zonesList.Remove(_zonesList.WithId(parkingZone.Id));
            
            _zonesList.Add(parkingZone);

            return Task.FromResult(parkingZone);
        }
    }
}

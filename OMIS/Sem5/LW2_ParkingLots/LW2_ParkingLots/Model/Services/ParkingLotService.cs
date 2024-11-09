using LW2_ParkingLots.Model.Entities;
using LW2_ParkingLots.Model.Persistence;
using LW2_ParkingLots.Model.Persistence.Repositories;

namespace LW2_ParkingLots.Model.Services
{
    public class ParkingLotService(IParkingLotRepository repository) : IParkingLotService
    {
        private readonly IParkingLotRepository _repository = repository;

        public async Task<bool> AddLotToUserAsync(int parkingLotId, int userId)
        {
            return await _repository.AddLotToUserAsync(parkingLotId, userId);
        }

        public async Task<ParkingLot> CreateParkingLotAsync()
        {
            return await _repository.CreateParkingLotAsync();
        }

        public async Task DeleteParkingLotAsync(int id)
        {
            await _repository.DeleteParkingLotAsync(id);
        }

        public async Task<ParkingLot> GetParkingLotAsync(int id)
        {
            return await _repository.GetParkingLotAsync(id);
        }

        public async Task<List<ParkingLot>> GetParkingLotWithFilterAsync(ParkingLotFilter filter, int parkingZoneId)
        {
            return await _repository.GetParkingLotWithFilterAsync(filter, parkingZoneId);
        }

        public async Task<bool> SetTimeToLotAsync(int parkingLotId, int userId, DateTime startTime, DateTime endTime)
        {
            return await _repository.SetTimeToLotAsync(parkingLotId, userId, startTime, endTime);
        }

        public async Task<ParkingLot> UpdateParkingLotAsync(ParkingLot parkingLot)
        {
            return await _repository.UpdateParkingLotAsync(parkingLot);
        }
    }
}

using LW2_ParkingLots.Model.Entities;
using LW2_ParkingLots.Model.Persistence;
using LW2_ParkingLots.Model.Persistence.Repositories;

namespace LW2_ParkingLots.Model.Services
{
    public class ProfileService(IProfileRepository repo) : IProfileService
    {
        private readonly IProfileRepository _repo = repo;
        public async Task AddParkingLotToCurrentLots(ApplicationUser user, ParkingLot lot)
        {
            await _repo.AddParkingLotToCurrentLots(user, lot);
        }

        public async Task AddParkingLotToHistory(ApplicationUser user, ParkingLot lot)
        {
            await _repo.AddParkingLotToHistory(user, lot);
        }

        public async Task DeleteParkingLotFromCurrentLots(ApplicationUser user, ParkingLot lot)
        {
            await _repo.DeleteParkingLotFromCurrentLots(user, lot);
        }

        public async Task<List<ParkingLot>> GetBookingHistoryAsync(ApplicationUser user)
        {
            return await _repo.GetBookingHistoryAsync(user);
        }

        public async Task<List<ParkingLot>> GetCurrentParkingLotsAsync(ApplicationUser user)
        {
            return await _repo.GetCurrentParkingLotsAsync(user);
        }

        public async Task<ApplicationUser> GetUserAsync(int id)
        {
            return await _repo.GetUserAsync(id);
        }

        public async Task<ApplicationUser> GetUserDetailsAsync(ApplicationUser user)
        {
            return await _repo.GetUserDetailsAsync(user);
        }

        public async Task<List<ApplicationUser>> GetUsers()
        {
            return await _repo.GetUsers();
        }

        public async Task LoadPersonalPhoto(ApplicationUser user, byte[] personalPhoto)
        {
            await _repo.LoadPersonalPhoto(user, personalPhoto);
        }

        public async Task UpdateRole(ApplicationUser user, Role role)
        {
            await _repo.UpdateRole(user, role);
        }

        public async Task<ApplicationUser> UpdateUserInfo(ApplicationUser user)
        {
            return await _repo.UpdateUserInfo(user);
        }
    }
}
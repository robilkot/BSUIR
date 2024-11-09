using LW2_ParkingLots.Model.Entities;

namespace LW2_ParkingLots.Model.Persistence.Repositories
{
    public interface IProfileRepository
    {
        Task AddParkingLotToCurrentLots(ApplicationUser user, ParkingLot lot);
        Task AddParkingLotToHistory(ApplicationUser user, ParkingLot lot);
        Task DeleteParkingLotFromCurrentLots(ApplicationUser user, ParkingLot lot);
        Task<List<ParkingLot>> GetBookingHistoryAsync(ApplicationUser user);
        Task<List<ParkingLot>> GetCurrentParkingLotsAsync(ApplicationUser user);
        Task<ApplicationUser> GetUserAsync(int id);
        Task<ApplicationUser> GetUserDetailsAsync(ApplicationUser user);
        Task<List<ApplicationUser>> GetUsers();
        Task LoadPersonalPhoto(ApplicationUser user, byte[] personalPhoto);
        Task UpdateRole(ApplicationUser user, Role role);
        Task<ApplicationUser> UpdateUserInfo(ApplicationUser user);
    }
}
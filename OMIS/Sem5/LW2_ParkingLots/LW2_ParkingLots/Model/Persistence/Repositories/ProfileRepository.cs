using LW2_ParkingLots.Model.Entities;

namespace LW2_ParkingLots.Model.Persistence.Repositories
{
    public class ProfileRepository : IProfileRepository
    {
        private static List<ApplicationUser> _users = [
            new ApplicationUser() {
                Id = "0",
                FullName = "Tim Robilko",
                Email = "timur.robilko@gmail.com",
                PhoneNumber = "1234567890",
            },
            new ApplicationUser() {
                Id = "1",
                FullName = "Netim Robilko",
                Email = "netimur.robilko@gmail.com",
                PhoneNumber = "1234567890",
            },
            new ApplicationUser() {
                Id = "2",
                FullName = "Tim Nerobilko",
                Email = "timur.nerobilko@gmail.com",
                PhoneNumber = "1234567890",
            },
            new ApplicationUser() {
                Id = "3",
                FullName = "Netim Nerobilko",
                Email = "netimur.nerobilko@gmail.com",
                PhoneNumber = "1234567890",
            }
            ];
        public Task<ApplicationUser> GetUserAsync(int id)
        {
            return Task.FromResult(_users.First(u => u.Id == $"{id}"));
        }
        public async Task<List<ApplicationUser>> GetUsers()
        {
            return await Task.FromResult(_users.ToList());
        }
        public async Task<List<ParkingLot>> GetBookingHistoryAsync(ApplicationUser user)
        {
            throw new NotImplementedException();
        }
        public async Task<List<ParkingLot>> GetCurrentParkingLotsAsync(ApplicationUser user)
        {
            throw new NotImplementedException();
        }
        public async Task AddParkingLotToHistory(ApplicationUser user, ParkingLot lot)
        {
            throw new NotImplementedException();
        }
        public async Task AddParkingLotToCurrentLots(ApplicationUser user, ParkingLot lot)
        {
            throw new NotImplementedException();
        }
        public async Task DeleteParkingLotFromCurrentLots(ApplicationUser user, ParkingLot lot)
        {
            throw new NotImplementedException();
        }
        public async Task LoadPersonalPhoto(ApplicationUser user, byte[] personalPhoto)
        {
            throw new NotImplementedException();
        }
        public async Task<ApplicationUser> UpdateUserInfo(ApplicationUser user)
        {
            throw new NotImplementedException();
        }
        public async Task UpdateRole(ApplicationUser user, Role role)
        {
            throw new NotImplementedException();
        }
        public async Task<ApplicationUser> GetUserDetailsAsync(ApplicationUser user)
        {
            throw new NotImplementedException();
        }
    }
}

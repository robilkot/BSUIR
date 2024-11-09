
using LW2_ParkingLots.Model.Persistence;
using LW2_ParkingLots.Model.Persistence.Repositories;

namespace LW2_ParkingLots.Model.Services
{
    public class LoginService(ILoginRepository repo) : ILoginService
    {
        private readonly ILoginRepository _repo = repo;
        public async Task<ApplicationUser> Login(string email, string password)
        {
            return await _repo.Login(email, password);
        }
        public async Task<ApplicationUser> ResetPassword(ApplicationUser user, string newPassword)
        {
            return await _repo.ResetPassword(user, newPassword);
        }
    }
}

using LW2_ParkingLots.Model.Persistence;

namespace LW2_ParkingLots.Model.Services
{
    public interface ILoginService
    {
        Task<ApplicationUser> Login(string email, string password);
        Task<ApplicationUser> ResetPassword(ApplicationUser user, string newPassword);
    }
}

namespace LW2_ParkingLots.Model.Persistence.Repositories
{
    public interface ILoginRepository
    {
        Task<ApplicationUser> Login(string email, string password);
        Task<ApplicationUser> ResetPassword(ApplicationUser user, string newPassword);
    }
}
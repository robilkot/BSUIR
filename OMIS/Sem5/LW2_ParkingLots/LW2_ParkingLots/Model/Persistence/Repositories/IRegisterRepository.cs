
namespace LW2_ParkingLots.Model.Persistence.Repositories
{
    public interface IRegisterRepository
    {
        Task<ApplicationUser> SaveUser(string email, string password, string phoneNumber, string fullName);
    }
}
using LW2_ParkingLots.Model.Persistence;

namespace LW2_ParkingLots.Model.Services
{
    public interface IRegisterService
    {
        Task<ApplicationUser> SaveUser(string email, string password, string phoneNumber, string fullName);
    }
}
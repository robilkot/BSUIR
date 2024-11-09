using LW2_ParkingLots.Model.Persistence;
using LW2_ParkingLots.Model.Persistence.Repositories;

namespace LW2_ParkingLots.Model.Services
{
    public class RegisterService(IRegisterRepository repo) : IRegisterService
    {
        private readonly IRegisterRepository _repository = repo;

        public async Task<ApplicationUser> SaveUser(string email, string password, string phoneNumber, string fullName)
        {
            return await _repository.SaveUser(email, password, phoneNumber, fullName);
        }
    }
}
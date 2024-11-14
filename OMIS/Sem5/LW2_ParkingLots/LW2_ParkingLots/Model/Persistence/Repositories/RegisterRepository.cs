namespace LW2_ParkingLots.Model.Persistence.Repositories
{
    public class RegisterRepository(IProfileRepository repo) : IRegisterRepository
    {
        private readonly IProfileRepository _repo = repo;
        public async Task<ApplicationUser> SaveUser(string email, string password, string phoneNumber, string fullName)
        {
            return await _repo.GetUserAsync(0);
        }
    }
}

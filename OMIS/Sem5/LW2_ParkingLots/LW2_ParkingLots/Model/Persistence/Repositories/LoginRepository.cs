namespace LW2_ParkingLots.Model.Persistence.Repositories
{
    public class LoginRepository(IProfileRepository repo) : ILoginRepository
    {
        private readonly IProfileRepository _repo = repo;
        public async Task<ApplicationUser> ResetPassword(ApplicationUser user, string newPassword)
        {
            return await _repo.GetUserAsync(0);
        }
        public async Task<ApplicationUser> Login(string email, string password)
        {
            return await _repo.GetUserAsync(0);
        }
    }
}

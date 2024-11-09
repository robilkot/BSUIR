namespace LW2_ParkingLots.Model.Persistence.Repositories
{
    public class LoginRepository : ILoginRepository
    {
        public async Task<ApplicationUser> ResetPassword(ApplicationUser user, string newPassword)
        {
            throw new NotImplementedException();
        }
        public async Task<ApplicationUser> Login(string email, string password)
        {
            throw new NotImplementedException();
        }
    }
}

namespace LW2_ParkingLots.Model.Persistence.Repositories
{
    public class RegisterRepository : IRegisterRepository
    {
        public async Task<ApplicationUser> SaveUser(string email, string password, string phoneNumber, string fullName)
        {
            throw new NotImplementedException();
        }
    }
}

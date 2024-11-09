using LW2_ParkingLots.Model.Entities;
using Microsoft.AspNetCore.Identity;

namespace LW2_ParkingLots.Model.Persistence
{
    public class ApplicationUser : IdentityUser
    {
        public string FullName { get; set; }
        public byte[] PersonalPhoto { get; set; }

        public Review? Review { get; set; }
        public Role Role { get; set; }
        public List<ParkingLot> CurrentParkingLots { get; set; } = [];
        public List<ParkingLot> BookingHistory { get; set; } = [];
    }
}

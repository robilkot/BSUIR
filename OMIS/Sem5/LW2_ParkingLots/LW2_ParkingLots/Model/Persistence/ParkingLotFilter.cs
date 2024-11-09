namespace LW2_ParkingLots.Model.Persistence
{
    public class ParkingLotFilter
    {
        public ParkingLotStatus ParkingLotStatus {  get; set; }
        public ParkingLotType ParkingLotType { get; set; }
        public double Cost { get; set; }
        public DateTime ArrivalTime { get; set; }
    }
}

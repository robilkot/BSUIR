namespace LW2_ParkingLots.Model.Entities
{
    public record struct ParkingZone(
        int Id,
        string Address,
        List<ParkingLot> ParkingLots
        ) : IEntity;
}

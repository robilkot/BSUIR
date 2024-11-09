namespace LW2_ParkingLots.Model.Entities
{
    public record ParkingLot(
        int Id,
        ParkingLotStatus Status,
        ParkingLotType Type,
        bool IsForHandicapped,
        double Cost,
        DateTime ArrivalTime,
        DateTime DepartureTime
        );
}

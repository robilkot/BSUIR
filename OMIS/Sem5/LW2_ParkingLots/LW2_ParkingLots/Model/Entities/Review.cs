namespace LW2_ParkingLots.Model.Entities
{
    public record Review(
        int Id,
        string Content,
        int Rating,
        DateTime CreatedAt
        );
}

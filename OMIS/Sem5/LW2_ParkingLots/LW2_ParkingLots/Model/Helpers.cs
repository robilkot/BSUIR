namespace LW2_ParkingLots.Model
{
    public static class Helpers
    {
        public static T WithId<T>(this IEnumerable<T> list, int id) where T : IEntity
            => list.First(t => t.Id == id);
    }

    public interface IEntity
    {
        public int Id { get; }
    }
}

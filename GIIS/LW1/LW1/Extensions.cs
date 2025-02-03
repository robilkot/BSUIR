namespace LW1
{
    public static class Extensions
    {
        static Random rnd = new();
        public static T Random<T>(this ICollection<T> enumerable)
        {
            int random = rnd.Next(enumerable.Count);
            return enumerable.ElementAt(random);
        }
        public static void Each<T>(this IEnumerable<T> ie, Action<T> action)
        {
            foreach (var e in ie) action(e);
        }
    }
}

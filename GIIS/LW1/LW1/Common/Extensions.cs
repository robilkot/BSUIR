namespace LW1.Common
{
    public static class Extensions
    {
        static Random rnd = new();
        public static T Random<T>(this ICollection<T> enumerable)
        {
            int random = rnd.Next(enumerable.Count);
            return enumerable.ElementAt(random);
        }

        public static IEnumerable<string> IntParameters(this Type t)
            => t.GetProperties()
            .Where(info => info.PropertyType.Equals(typeof(int)))
            .Select(info => info.Name);
    }
}

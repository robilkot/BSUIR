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

        public static IEnumerable<(string name, T? value)> Properties<T>(this object t)
            => t
            .GetType()
            .GetProperties()
            .Where(info => info.PropertyType.Equals(typeof(T)))
            .Select(info => (info.Name, (T)info.GetValue(t)));
    }
}

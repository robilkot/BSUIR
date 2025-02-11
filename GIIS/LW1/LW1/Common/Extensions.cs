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

        public static List<Parameter<T>> Properties<T>(this object obj)
            => obj
            .GetType()
            .GetProperties()
            .Where(info => info.PropertyType.Equals(typeof(Parameter<T>)))
            .Select(info => (Parameter<T>)info.GetValue(obj)!)
            .ToList();
    }
}

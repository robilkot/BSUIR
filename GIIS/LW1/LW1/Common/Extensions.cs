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

        public static Dictionary<Type, List<IParameter>> Properties(this object obj)
        {
            Dictionary<Type, List<IParameter>> result = [];

            var propertiesTypes = obj
            .GetType()
            .GetProperties()
            .Where(t => typeof(IParameter).IsAssignableFrom(t.PropertyType));
            //.Where(info => info.PropertyType.Equals(typeof(IParameter)))

            foreach (var property in propertiesTypes)
            {
                var genericType = property.PropertyType.GenericTypeArguments[0];

                if (!result.ContainsKey(genericType))
                    result[genericType] = [];

                result[genericType].Add((IParameter)property.GetValue(obj)!);
            }

            return result;
        }

        public static List<Parameter<T>> Properties<T>(this object obj)
            => obj
            .GetType()
            .GetProperties()
            .Where(info => info.PropertyType.Equals(typeof(Parameter<T>)))
            .Select(info => (Parameter<T>)info.GetValue(obj)!)
            .ToList();

        public static List<T> FilledWithSubtypes<T>(this List<T> list)
        {
            var type = typeof(T);
            var algorithms = type.Assembly
                .GetTypes()
                //.Where(t => t.IsSubclassOf(type))
                .Where(t => type.IsAssignableFrom(t) && t.IsClass)
                .ToArray();

            foreach (var algType in algorithms)
            {
                var alg = (T)Activator.CreateInstance(algType)!;
                list.Add(alg);
            }

            return list;
        }
    }
}

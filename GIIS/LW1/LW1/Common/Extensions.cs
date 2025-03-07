using LW1.LineDrawing;

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

        public static IEnumerable<IParameter> Properties(this object obj)
            => obj
            .GetType()
            .GetProperties()
            .Where(prop => (typeof(IParameter)).IsAssignableFrom(prop.PropertyType))
            .Select(prop => (IParameter)prop.GetValue(obj)!);

        public static List<T> FilledWithSubtypes<T>(this List<T> list)
        {
            var type = typeof(T);
            var algorithms = type.Assembly
                .GetTypes()
                .Where(t => type.IsAssignableFrom(t) && t.IsClass)
                .ToArray();

            foreach (var algType in algorithms)
            {
                var alg = (T)Activator.CreateInstance(algType)!;
                list.Add(alg);
            }

            return list;
        }

        public static void InitWithSubtypes<T>(this ComboBox comboBox)
        {
            comboBox.DataSource = new List<T>().FilledWithSubtypes();
            comboBox.DisplayMember = nameof(IDrawingAlgorithm.DisplayName);
            comboBox.ValueMember = nameof(IDrawingAlgorithm.DisplayName);
        }
    }
}

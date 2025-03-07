using LW1.Common.Algorithms;
using LW1.Common.Parameters;
using LW1.Common.Shapes;
using LW1.Polygons.Common;

namespace LW1.Polygons.Fill
{
    public class SimpleSeedFillDebugInfo : DebugInfo
    {
        public Point CurrentPoint { get; set; }
        public int StackCount { get; set; }
    }
    public class SimpleSeedFill : IPolygonDrawingAlgorithm
    {
        public IDrawingParameters EmptyParameters => new PolygonParameters();
        public string DisplayName => "Простой алгоритм заполнения (с затравкой)";

        public IEnumerable<DrawInfo> Draw(IParameters param)
        {
            if (param is not PolygonParameters polygon)
                yield break;

            var vertices = polygon.Vertices.Select(p => p.Value).ToList();
            var color = polygon.Color.Value;
            if (vertices.Count < 3)
                yield break;

            // Вычисляем затравочную точку как центр масс вершин
            int seedX = vertices.Sum(p => p.X) / vertices.Count;
            int seedY = vertices.Sum(p => p.Y) / vertices.Count;
            var seed = new Point(seedX, seedY);

            var filled = new HashSet<Point>();
            var stack = new Stack<Point>();
            stack.Push(seed);

            while (stack.Count > 0)
            {
                var p = stack.Pop();
                if (filled.Contains(p))
                    continue;
                if (!IsPointInsidePolygon(p, vertices))
                    continue;

                filled.Add(p);
                yield return new()
                {
                    Drawable = new ColorPoint(p, color),
                    DebugInfo = new SimpleSeedFillDebugInfo
                    {
                        CurrentPoint = p,
                        StackCount = stack.Count
                    },
                };

                // Добавляем соседей (4-связность)
                stack.Push(new Point(p.X + 1, p.Y));
                stack.Push(new Point(p.X - 1, p.Y));
                stack.Push(new Point(p.X, p.Y + 1));
                stack.Push(new Point(p.X, p.Y - 1));
            }
        }

        // Метод определения принадлежности точки полигону (алгоритм "чет-нечет")
        private bool IsPointInsidePolygon(Point p, List<Point> poly)
        {
            bool inside = false;
            int n = poly.Count;
            for (int i = 0, j = n - 1; i < n; j = i++)
            {
                if (poly[i].Y > p.Y != poly[j].Y > p.Y &&
                    p.X < (poly[j].X - poly[i].X) * (p.Y - poly[i].Y) / (double)(poly[j].Y - poly[i].Y) + poly[i].X)
                {
                    inside = !inside;
                }
            }
            return inside;
        }
    }
}

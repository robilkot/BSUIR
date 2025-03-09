using LW1.Common.Algorithms;
using LW1.Common.Parameters;
using LW1.Common.Shapes;
using LW1.Polygons.Common;

namespace LW1.Polygons.Fill
{
    public class ScanlineSeedFillDebugInfo : DebugInfo
    {
        public int CurrentScanline { get; set; }
        public int XStart { get; set; }
        public int XEnd { get; set; }
        public int StackCount { get; set; }
    }

    public class ScanlineSeedFill : IPolygonDrawingAlgorithm
    {
        public IDrawingParameters EmptyParameters => new PolygonParameters();
        public string DisplayName => "Построчный алгоритм заполнения (с затравкой)";

        public IEnumerable<DrawInfo> Draw(IParameters param)
        {
            if (param is not PolygonParameters polygon)
                yield break;

            var vertices = polygon.Vertices.Select(p => p.Value).ToList();
            var color = polygon.Color.Value;
            if (vertices.Count < 3)
                yield break;

            var filled = new HashSet<Point>();
            var stack = new Stack<Point>();

            // Затравочная точка – центр масс вершин
            int seedX = vertices.Sum(p => p.X) / vertices.Count;
            int seedY = vertices.Sum(p => p.Y) / vertices.Count;
            var seed = new Point(seedX, seedY);
            stack.Push(seed);

            while (stack.Count > 0)
            {
                var p = stack.Pop();
                int x = p.X;
                int y = p.Y;

                // Находим левую границу заливки на текущей строке
                int xLeft = x;
                while (!filled.Contains(new Point(xLeft - 1, y)) && Common.PolygonsHelpers.IsPointInsidePolygon(new Point(xLeft - 1, y), polygon))
                {
                    xLeft--;
                }
                // Находим правую границу
                int xRight = x;
                while (!filled.Contains(new Point(xRight + 1, y)) && Common.PolygonsHelpers.IsPointInsidePolygon(new Point(xRight + 1, y), polygon))
                {
                    xRight++;
                }
                // Заполняем найденный интервал и проверяем строки сверху и снизу
                for (int xi = xLeft; xi <= xRight; xi++)
                {
                    var pt = new Point(xi, y);
                    if (!filled.Contains(pt) && Common.PolygonsHelpers.IsPointInsidePolygon(pt, polygon))
                    {
                        filled.Add(pt);
                        yield return new()
                        {
                            Drawable = new ColorPoint(pt, color),
                            DebugInfo = new ScanlineSeedFillDebugInfo
                            {
                                CurrentScanline = y,
                                XStart = xLeft,
                                XEnd = xRight,
                                StackCount = stack.Count
                            },
                        };
                        // Если сверху/снизу есть незалитые точки – добавляем их в стек
                        if (!filled.Contains(new Point(xi, y - 1)) && Common.PolygonsHelpers.IsPointInsidePolygon(new Point(xi, y - 1), polygon))
                            stack.Push(new Point(xi, y - 1));
                        if (!filled.Contains(new Point(xi, y + 1)) && Common.PolygonsHelpers.IsPointInsidePolygon(new Point(xi, y + 1), polygon))
                            stack.Push(new Point(xi, y + 1));
                    }
                }
            }
        }
    }
}

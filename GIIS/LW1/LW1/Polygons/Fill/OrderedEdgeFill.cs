using LW1.Common.Algorithms;
using LW1.Common.Parameters;
using LW1.Common.Shapes;
using LW1.Polygons.Common;

namespace LW1.Polygons.Fill
{
    public class OrderedEdgeFillDebugInfo : DebugInfo
    {
        public int Scanline { get; set; }
        public double XLeft { get; set; }
        public double XRight { get; set; }
        public int FillPixelX { get; set; }
        public int FillPixelY { get; set; }
    }
    public class OrderedEdgeFill : IPolygonDrawingAlgorithm
    {
        public IDrawingParameters EmptyParameters => new PolygonParameters();
        public string DisplayName => "Заполнение полигона (упорядоченный список ребер)";

        public IEnumerable<DrawInfo> Draw(IParameters param)
        {
            if (param is not PolygonParameters polygon)
                yield break;

            // Получаем список вершин и цвет
            var vertices = polygon.Vertices.Select(p => p.Value).ToList();
            var color = polygon.Color.Value;

            if (vertices.Count < 3)
                yield break;

            // Определяем границы по Y
            int minY = vertices.Min(p => p.Y);
            int maxY = vertices.Max(p => p.Y);

            // Формируем таблицу ребер (пропускаем горизонтальные ребра)
            var edges = new List<EdgeRecord>();
            for (int i = 0; i < vertices.Count; i++)
            {
                var p1 = vertices[i];
                var p2 = vertices[(i + 1) % vertices.Count];
                if (p1.Y == p2.Y)
                    continue; // горизонтальные ребра не учитываем

                var edge = new EdgeRecord();
                if (p1.Y < p2.Y)
                {
                    edge.yMin = p1.Y;
                    edge.yMax = p2.Y;
                    edge.x = p1.X;
                    edge.invSlope = (double)(p2.X - p1.X) / (p2.Y - p1.Y);
                }
                else
                {
                    edge.yMin = p2.Y;
                    edge.yMax = p1.Y;
                    edge.x = p2.X;
                    edge.invSlope = (double)(p1.X - p2.X) / (p1.Y - p2.Y);
                }
                edges.Add(edge);
            }

            // Сортируем ребра по yMin
            edges.Sort((a, b) => a.yMin.CompareTo(b.yMin));

            // Для каждой строки (scanline)
            for (int y = minY; y <= maxY; y++)
            {
                var xIntersections = new List<double>();
                // Находим точки пересечения ребер с текущей горизонтальной линией
                foreach (var edge in edges)
                {
                    if (y >= edge.yMin && y < edge.yMax)
                    {
                        double xInt = edge.x + (y - edge.yMin) * edge.invSlope;
                        xIntersections.Add(xInt);
                    }
                }
                xIntersections.Sort();

                // Заполняем пиксели между парами пересечений
                for (int i = 0; i < xIntersections.Count; i += 2)
                {
                    if (i + 1 >= xIntersections.Count)
                        break;
                    int xStart = (int)Math.Round(xIntersections[i]);
                    int xEnd = (int)Math.Round(xIntersections[i + 1]);
                    for (int x = xStart; x <= xEnd; x++)
                    {
                        yield return new()
                        {
                            Drawable = new ColorPoint(new Point(x, y), polygon.Color),
                            DebugInfo = new OrderedEdgeFillDebugInfo
                            {
                                Scanline = y,
                                XLeft = xIntersections[i],
                                XRight = xIntersections[i + 1],
                                FillPixelX = x,
                                FillPixelY = y
                            },
                        };
                    }
                }
            }
        }

        private class EdgeRecord
        {
            public int yMin;
            public int yMax;
            public double x;
            public double invSlope;
        }
    }
}

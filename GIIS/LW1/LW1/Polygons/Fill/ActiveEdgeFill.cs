using LW1.Common.Algorithms;
using LW1.Common.Parameters;
using LW1.Common.Shapes;
using LW1.Polygons.Common;

namespace LW1.Polygons.Fill
{
    public class ActiveEdgeFillDebugInfo : DebugInfo
    {
        public int Scanline { get; set; }
        public List<double> ActiveX { get; set; }
        public int FillPixelX { get; set; }
        public int FillPixelY { get; set; }
    }

    public class ActiveEdgeFill : IPolygonDrawingAlgorithm
    {
        public IDrawingParameters EmptyParameters => new PolygonParameters();
        public string DisplayName => "Заполнение полигона (активный список ребер)";

        public IEnumerable<DrawInfo> Draw(IParameters param)
        {
            if (param is not PolygonParameters polygon)
                yield break;

            var vertices = polygon.Vertices.Select(p => p.Value).ToList();
            var color = polygon.Color.Value;
            if (vertices.Count < 3)
                yield break;

            int minY = vertices.Min(p => p.Y);
            int maxY = vertices.Max(p => p.Y);

            // Построение таблицы ребер
            var edgeTable = new List<EdgeRecord>();
            for (int i = 0; i < vertices.Count; i++)
            {
                var p1 = vertices[i];
                var p2 = vertices[(i + 1) % vertices.Count];
                if (p1.Y == p2.Y)
                    continue;
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
                edgeTable.Add(edge);
            }
            edgeTable.Sort((a, b) => a.yMin.CompareTo(b.yMin));

            var activeEdgeList = new List<EdgeRecord>();

            // Проходим по всем строкам
            for (int y = minY; y <= maxY; y++)
            {
                // Добавляем ребра, начинающиеся на текущей строке
                foreach (var edge in edgeTable.Where(e => e.yMin == y))
                    activeEdgeList.Add(edge);

                // Удаляем ребра, для которых достигнута верхняя граница
                activeEdgeList.RemoveAll(e => y >= e.yMax);

                // Сортируем активный список по текущему значению X (пересечение с y)
                activeEdgeList.Sort((a, b) =>
                {
                    double xA = a.x + (y - a.yMin) * a.invSlope;
                    double xB = b.x + (y - b.yMin) * b.invSlope;
                    return xA.CompareTo(xB);
                });

                // Вычисляем список X-пересечений
                var activeXs = activeEdgeList
                    .Select(e => e.x + (y - e.yMin) * e.invSlope)
                    .OrderBy(x => x)
                    .ToList();

                // Заполняем промежутки между парами пересечений
                for (int i = 0; i < activeXs.Count; i += 2)
                {
                    if (i + 1 >= activeXs.Count)
                        break;
                    int xStart = (int)Math.Round(activeXs[i]);
                    int xEnd = (int)Math.Round(activeXs[i + 1]);
                    for (int x = xStart; x <= xEnd; x++)
                    {
                        yield return new()
                        {
                            Drawable = new ColorPoint(new Point(x, y), polygon.Color),
                            DebugInfo = new ActiveEdgeFillDebugInfo
                            {
                                Scanline = y,
                                ActiveX = new List<double>(activeXs),
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

using LW1.Common;
using LW1.Common.Shapes;
using LW1.LineDrawing;
using LW1.Polygons.Common;
using System.Drawing;
using System.Xml.Linq;

namespace LW1.Polygons.Fill
{
    #region Алгоритм 1: Заполнение полигона с упорядоченным списком ребер

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
    #endregion

    #region Алгоритм 2: Заполнение полигона с активным списком ребер

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
    #endregion

    #region Алгоритм 3: Простой алгоритм заполнения с затравкой (seed fill)

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
    #endregion

    #region Алгоритм 4: Построчный алгоритм заполнения с затравкой (scanline seed fill)

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
                while (!filled.Contains(new Point(xLeft - 1, y)) && IsPointInsidePolygon(new Point(xLeft - 1, y), polygon))
                {
                    xLeft--;
                }
                // Находим правую границу
                int xRight = x;
                while (!filled.Contains(new Point(xRight + 1, y)) && IsPointInsidePolygon(new Point(xRight + 1, y), polygon))
                {
                    xRight++;
                }
                // Заполняем найденный интервал и проверяем строки сверху и снизу
                for (int xi = xLeft; xi <= xRight; xi++)
                {
                    var pt = new Point(xi, y);
                    if (!filled.Contains(pt) && IsPointInsidePolygon(pt, polygon))
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
                        if (!filled.Contains(new Point(xi, y - 1)) && IsPointInsidePolygon(new Point(xi, y - 1), polygon))
                            stack.Push(new Point(xi, y - 1));
                        if (!filled.Contains(new Point(xi, y + 1)) && IsPointInsidePolygon(new Point(xi, y + 1), polygon))
                            stack.Push(new Point(xi, y + 1));
                    }
                }
            }
        }

        private bool IsPointInsidePolygon(Point p, PolygonParameters poly)
        {
            return new BelongingCheck().Execute((poly, p));
        }
    }
}
#endregion

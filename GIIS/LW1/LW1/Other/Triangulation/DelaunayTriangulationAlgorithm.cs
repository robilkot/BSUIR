using LW1.Common.Algorithms;
using LW1.Common.Parameters;
using LW1.LineDrawing;
using LW1.LineDrawing.Common;
using LW1.Polygons.Common;

namespace LW1.Other.Triangulation
{
    public partial class DelaunayTriangulationAlgorithm : IOtherDrawingAlgorithm
    {
        public string DisplayName => "Триангуляция Делоне";

        public IDrawingParameters EmptyParameters => new PolygonParameters();

        public IEnumerable<DrawInfo> Draw(IParameters parameters)
        {
            if (parameters is not PolygonParameters param)
                yield break;

            // Извлекаем точки из параметров полигона
            var points = param.Vertices.Select(v => v.Value).ToList();
            if (points.Count < 3)
                yield break;

            // Наивная триангуляция Делоне:
            // Перебираем все возможные тройки точек и выбираем те, у которых
            // описанная окружность не содержит ни одной другой точки.
            var triangles = new List<(Point A, Point B, Point C)>();
            for (int i = 0; i < points.Count; i++)
            {
                for (int j = i + 1; j < points.Count; j++)
                {
                    for (int k = j + 1; k < points.Count; k++)
                    {
                        if (IsDelaunayTriangle(points[i], points[j], points[k], points))
                        {
                            triangles.Add((points[i], points[j], points[k]));
                        }
                    }
                }
            }

            // Собираем уникальные ребра (учитывая, что ребро A-B такое же, как B-A)
            var edges = new HashSet<UndirectedEdge>(new UndirectedEdgeComparer());
            foreach (var (A, B, C) in triangles)
            {
                edges.Add(new UndirectedEdge(A, B));
                edges.Add(new UndirectedEdge(B, C));
                edges.Add(new UndirectedEdge(C, A));
            }

            var lineAlgorithm = new Wu();
            foreach (var edge in edges)
            {
                var cdaParams = new LineDrawingParameters()
                {
                    Color = param.Color,
                    Start = edge.A,
                    End = edge.B
                };
                foreach (var pt in lineAlgorithm.Draw(cdaParams))
                    yield return pt;
            }
        }

        // Метод проверки, удовлетворяет ли тройка точек условию Делоне:
        // описанная окружность треугольника не должна содержать никаких других точек.
        private static bool IsDelaunayTriangle(Point a, Point b, Point c, List<Point> points)
        {
            // Вычисляем определитель, чтобы проверить, не коллинеарны ли точки
            double d = 2 * (a.X * (b.Y - c.Y) + b.X * (c.Y - a.Y) + c.X * (a.Y - b.Y));
            if (Math.Abs(d) < 1e-6) return false; // вырожденный треугольник

            double ax2 = a.X * a.X + a.Y * a.Y;
            double bx2 = b.X * b.X + b.Y * b.Y;
            double cx2 = c.X * c.X + c.Y * c.Y;

            double centerX = (ax2 * (b.Y - c.Y) + bx2 * (c.Y - a.Y) + cx2 * (a.Y - b.Y)) / d;
            double centerY = (ax2 * (c.X - b.X) + bx2 * (a.X - c.X) + cx2 * (b.X - a.X)) / d;

            // Вычисляем квадрат радиуса описанной окружности
            double r2 = (a.X - centerX) * (a.X - centerX) + (a.Y - centerY) * (a.Y - centerY);

            // Если любая другая точка лежит строго внутри окружности, то треугольник не удовлетворяет условию Делоне.
            foreach (var p in points)
            {
                if (p.Equals(a) || p.Equals(b) || p.Equals(c))
                    continue;
                double dist2 = (p.X - centerX) * (p.X - centerX) + (p.Y - centerY) * (p.Y - centerY);
                if (dist2 < r2 - 1e-6)
                    return false;
            }
            return true;
        }   
    }
}
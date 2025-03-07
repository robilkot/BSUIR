using LW1.Common.Algorithms;
using LW1.Common.Parameters;
using LW1.Common.Shapes;
using LW1.LineDrawing;
using LW1.LineDrawing.Common;
using LW1.Polygons.Common;

namespace LW1.Polygons
{
    public class PolygonNormalsDrawingAlgorithm : IDrawingAlgorithm
    {
        private static readonly int s_normalLength = 3;
        private static readonly Color s_normalColor = Color.Blue;

        public IDrawingParameters EmptyParameters => new PolygonParameters();

        public string DisplayName => throw new NotImplementedException();

        public IEnumerable<DrawInfo> Draw(IParameters parameters)
        {
            if (parameters is not PolygonParameters polygon)
                yield break;

            var normals = GetNormals(polygon);

            var lineAlgo = new CDA();

            foreach (var normal in normals)
            {
                var lineParams = new LineDrawingParameters()
                {
                    Color = s_normalColor,
                    Start = normal.start,
                    End = normal.end,
                };

                foreach(var point in lineAlgo.Draw(lineParams))
                {
                    yield return point;
                }
            }
        }

        private static List<(Point start, Point end)> GetNormals(PolygonParameters polygon)
        {
            var normals = new List<(Point Start, Point End)>();
            var vertices = polygon.Vertices.Select(v => v.Value).ToList();
            int n = vertices.Count;
            if (n < 2)
                return normals;

            // Вычисляем центроид полигона (среднее арифметическое координат вершин)
            double sumX = 0, sumY = 0;
            foreach (var v in vertices)
            {
                sumX += v.X;
                sumY += v.Y;
            }
            double centroidX = sumX / n;
            double centroidY = sumY / n;

            // Для каждого ребра полигона
            for (int i = 0; i < n; i++)
            {
                Point p1 = vertices[i];
                Point p2 = vertices[(i + 1) % n];

                // Середина ребра
                double midX = (p1.X + p2.X) / 2.0;
                double midY = (p1.Y + p2.Y) / 2.0;

                // Вектор ребра
                double dx = p2.X - p1.X;
                double dy = p2.Y - p1.Y;

                // Кандидат на нормаль (перпендикуляр) равен (dy, -dx)
                double nx = dy;
                double ny = -dx;

                // Определяем, куда направлен кандидат.
                // Вычисляем вектор от середины ребра к центроиду
                double toCentroidX = centroidX - midX;
                double toCentroidY = centroidY - midY;
                // Если кандидат указывает внутрь (то есть dot > 0), разворачиваем его.
                double dot = nx * toCentroidX + ny * toCentroidY;
                if (dot > 0)
                {
                    nx = -nx;
                    ny = -ny;
                }

                // Нормируем вектор нормали
                double length = Math.Sqrt(nx * nx + ny * ny);
                if (length == 0)
                    continue; // вырожденное ребро
                double unitNx = nx / length;
                double unitNy = ny / length;

                // Умножаем на заданную длину
                double normalDx = unitNx * s_normalLength;
                double normalDy = unitNy * s_normalLength;

                // Конечная точка отрезка нормали
                int endX = (int)Math.Round(midX + normalDx);
                int endY = (int)Math.Round(midY + normalDy);
                int startX = (int)Math.Round(midX);
                int startY = (int)Math.Round(midY);

                normals.Add((new Point(startX, startY), new Point(endX, endY)));
            }

            return normals;
        }
    }
}

using LW1.Common.Algorithms;
using LW1.LineDrawing.Common;
using LW1.Polygons.Common;

namespace LW1.Polygons.Algorithms
{
    public class IntersectionCheck : IAlgorithm<(PolygonParameters polygon, LineDrawingParameters line), IEnumerable<Point>>
    {
        public IEnumerable<Point> Execute((PolygonParameters polygon, LineDrawingParameters line) param)
        {
            var (polygon, line) = (param.polygon, param.line);

            var intersections = new List<Point>();
            var vertices = polygon.Vertices.Select(v => v.Value).ToList();
            int n = vertices.Count;
            if (n < 2)
                yield break;

            for (int i = 0; i < n; i++)
            {
                // Ребро многоугольника (с циклическим замыканием)
                Point polyStart = vertices[i];
                Point polyEnd = vertices[(i + 1) % n];

                Point? intersection = GetSegmentIntersection(polyStart, polyEnd, line.Start, line.End);
                if (intersection.HasValue)
                {
                    // Если такая точка пересечения ещё не добавлена, добавляем её
                    if (!intersections.Contains(intersection.Value))
                    {
                        intersections.Add(intersection.Value);
                        yield return intersection.Value;
                    }
                }
            }
        }

        private static Point? GetSegmentIntersection(Point p, Point p2, Point q, Point q2)
        {
            // Векторы направления: r = p2 - p, s = q2 - q
            int rX = p2.X - p.X;
            int rY = p2.Y - p.Y;
            int sX = q2.X - q.X;
            int sY = q2.Y - q.Y;

            // Вычисляем векторное произведение r x s
            int rxs = rX * sY - rY * sX;
            if (rxs == 0) // отрезки параллельны или коллинеарны
                return null;

            // Параметры t и u для параметрического представления отрезков
            double t = ((q.X - p.X) * sY - (q.Y - p.Y) * sX) / (double)rxs;
            double u = ((q.X - p.X) * rY - (q.Y - p.Y) * rX) / (double)rxs;

            // Проверяем, что пересечение попадает в оба отрезка
            if (t >= 0 && t <= 1 && u >= 0 && u <= 1)
            {
                double interX = p.X + t * rX;
                double interY = p.Y + t * rY;
                // Округляем до ближайшего целого
                int intX = (int)Math.Round(interX);
                int intY = (int)Math.Round(interY);
                return new Point(intX, intY);
            }

            return null;
        }
    }
}
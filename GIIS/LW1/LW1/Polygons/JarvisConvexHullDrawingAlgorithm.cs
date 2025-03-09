using LW1.Common.Algorithms;
using LW1.Common.Parameters;
using LW1.LineDrawing;
using LW1.LineDrawing.Common;
using LW1.Polygons.Common;
using static LW1.Common.Helpers;

namespace LW1.Polygons
{
    public class JarvisConvexHullDrawingAlgorithm : IPolygonDrawingAlgorithm
    {
        public IDrawingParameters EmptyParameters => new PolygonParameters();
        public string DisplayName => "Выпуклая оболочка (Джарвис)";

        public IEnumerable<DrawInfo> Draw(IParameters parameters)
        {
            if (parameters is not PolygonParameters param)
                yield break;

            // Извлекаем список точек из параметров.
            var points = param.Vertices.Select(p => p.Value).ToList();
            if (points.Count < 3)
            {
                // Если точек меньше трёх, просто соединяем их последовательно.
                var cda = new CDA();
                for (int i = 0; i < points.Count; i++)
                {
                    var start = points[i];
                    var end = points[(i + 1) % points.Count];
                    var cdaParams = new LineDrawingParameters()
                    {
                        Color = param.Color,
                        Start = new Parameter<Point>() { DisplayName = $"P{i + 1}", Value = start },
                        End = new Parameter<Point>() { DisplayName = $"P{(i + 2)}", Value = end }
                    };
                    foreach (var pt in cda.Draw(cdaParams))
                        yield return pt;
                }
                yield break;
            }

            // Шаг 1: Выбираем самую левую точку (с минимальной координатой X, при равенстве — минимальной Y).
            var startPoint = points.OrderBy(p => p.X).ThenBy(p => p.Y).First();
            var hullPoints = new List<Point>();
            var currentPoint = startPoint;

            // Шаг 2: Алгоритм Джарвиса: на каждом шаге выбираем точку, которая расположена максимально «слева»
            // относительно текущей, то есть такая, что все остальные точки находятся правее направления.
            do
            {
                hullPoints.Add(currentPoint);
                // Инициализируем следующую точку кандидатом (можно взять любую, отличную от currentPoint).
                var nextPoint = points[0];
                foreach (var candidate in points)
                {
                    if (candidate.Equals(currentPoint))
                        continue;
                    double cross = CrossProduct(currentPoint, nextPoint, candidate);
                    // Если nextPoint равна currentPoint или кандидат находится левее относительно текущего направления,
                    // либо лежит на одной прямой, но дальше от currentPoint, выбираем кандидата.
                    if (nextPoint.Equals(currentPoint) || cross > 0 ||
                        (Math.Abs(cross) < 1e-9 && Distance(currentPoint, candidate) > Distance(currentPoint, nextPoint)))
                    {
                        nextPoint = candidate;
                    }
                }
                currentPoint = nextPoint;
            } while (!currentPoint.Equals(startPoint));

            // Шаг 3: Отрисовка сторон выпуклой оболочки с помощью алгоритма ЦДА.
            var cdaAlgorithm = new CDA();
            for (int i = 0; i < hullPoints.Count; i++)
            {
                var start = hullPoints[i];
                var end = hullPoints[(i + 1) % hullPoints.Count];
                var cdaParams = new LineDrawingParameters()
                {
                    Color = param.Color,
                    Start = start,
                    End = end
                };

                foreach (var pt in cdaAlgorithm.Draw(cdaParams))
                {
                    yield return pt;
                }
            }
        }
    }
}

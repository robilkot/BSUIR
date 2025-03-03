using LW1.Common;
using LW1.LineDrawing;
using LW1.LineDrawing.Common;
using LW1.Polygons.Common;

namespace LW1.Polygons
{
    public class PolygonParameters : IDrawingParameters
    {
        public Parameter<Color> Color { get; init; } = new() { DisplayName = "Цвет", Value = System.Drawing.Color.Black };
        public ParametersList<Point> Vertices { get; init; } = new("Вершины")
        {
            new() { DisplayName = "P1", Value = new(24, 21) },
            new() { DisplayName = "P2", Value = new(31, 4) },
            new() { DisplayName = "P3", Value = new(38, 21) },
            new() { DisplayName = "P4", Value = new(56, 25) },
            new() { DisplayName = "P5", Value = new(43, 38) },
            new() { DisplayName = "P6", Value = new(50, 55) },
            new() { DisplayName = "P7", Value = new(31, 43) },
            new() { DisplayName = "P8", Value = new(13, 55) },
            new() { DisplayName = "P9", Value = new(18, 37) },
            new() { DisplayName = "P10", Value = new(6, 25) },
        };
    }

    public class SimplePolygonDrawingAlgorithm : IPolygonDrawingAlgorithm
    {
        public IDrawingParameters EmptyParameters => new PolygonParameters();
        public string DisplayName => "Полигон по точкам";

        public IEnumerable<(ColorPoint point, DebugInfo info)> Draw(IDrawingParameters parameters)
        {
            if (parameters is not PolygonParameters param)
                yield break;

            IEnumerable<(Parameter<Point> Start, Parameter<Point> End)> pairs = param.Vertices.Select((point, index)
                => (point, param.Vertices[(index + 1) % param.Vertices.Count]));

            var cda = new CDA();

            foreach (var (Start, End) in pairs)
            {
                var cdaParams = new LineDrawingParameters()
                {
                    Color = param.Color,
                    Start = Start,
                    End = End,
                };

                foreach (var point in cda.Draw(cdaParams))
                {
                    yield return point;
                }
            }
        }
    }

    public class GrahamConvexHullDrawingAlgorithm : IPolygonDrawingAlgorithm
    {
        public IDrawingParameters EmptyParameters => new PolygonParameters();
        public string DisplayName => "Выпуклая оболочка (Грэхем)";

        public IEnumerable<(ColorPoint point, DebugInfo info)> Draw(IDrawingParameters parameters)
        {
            if (parameters is not PolygonParameters param)
                yield break;

            // Извлекаем список точек
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
                        Start = start,
                        End = end
                    };
                    foreach (var pt in cda.Draw(cdaParams))
                    {
                        yield return pt;
                    }
                }
                yield break;
            }

            // Шаг 1: Находим точку с минимальной координатой Y (при равенстве выбираем с минимальной X).
            var pivot = points.OrderBy(p => p.Y).ThenBy(p => p.X).First();

            // Шаг 2: Сортируем точки по полярному углу относительно pivot.
            var sortedPoints = points.OrderBy(p => Math.Atan2(p.Y - pivot.Y, p.X - pivot.X)).ToList();

            // Шаг 3: Алгоритм Грэхема. Используем стек для формирования выпуклой оболочки.
            Stack<Point> hull = new();
            foreach (var pt in sortedPoints)
            {
                while (hull.Count >= 2)
                {
                    var q = hull.Pop();
                    var r = hull.Peek();
                    // Если тройка (r, q, pt) не образует левый поворот (то есть не против часовой стрелки), отбрасываем q.
                    if (CrossProduct(r, q, pt) <= 0)
                        continue;
                    else
                    {
                        hull.Push(q);
                        break;
                    }
                }
                hull.Push(pt);
            }

            // Получаем последовательность точек выпуклой оболочки в порядке обхода
            var hullPoints = hull.Reverse().ToList();

            // Шаг 4: Отрисовка сторон выпуклой оболочки с помощью алгоритма ЦДА.
            var cdaAlgorithm = new CDA();
            for (int i = 0; i < hullPoints.Count; i++)
            {
                var start = hullPoints[i];
                var end = hullPoints[(i + 1) % hullPoints.Count];
                var cdaParams = new LineDrawingParameters()
                {
                    Color = param.Color,
                    Start = new Parameter<Point>() { DisplayName = $"P{i + 1}", Value = start },
                    End = new Parameter<Point>() { DisplayName = $"P{(i + 2)}", Value = end }
                };

                foreach (var pt in cdaAlgorithm.Draw(cdaParams))
                {
                    yield return pt;
                }
            }
        }
        private double CrossProduct(Point a, Point b, Point c)
        {
            return (b.X - a.X) * (c.Y - a.Y) - (b.Y - a.Y) * (c.X - a.X);
        }
    }

    public class JarvisConvexHullDrawingAlgorithm : IPolygonDrawingAlgorithm
    {
        public IDrawingParameters EmptyParameters => new PolygonParameters();
        public string DisplayName => "Выпуклая оболочка (Джарвис)";

        public IEnumerable<(ColorPoint point, DebugInfo info)> Draw(IDrawingParameters parameters)
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

        // Вспомогательный метод для вычисления векторного произведения (определение ориентации)
        private double CrossProduct(Point a, Point b, Point c)
        {
            return (b.X - a.X) * (c.Y - a.Y) - (b.Y - a.Y) * (c.X - a.X);
        }

        // Вспомогательный метод для вычисления расстояния между двумя точками
        private double Distance(Point a, Point b)
        {
            double dx = a.X - b.X;
            double dy = a.Y - b.Y;
            return Math.Sqrt(dx * dx + dy * dy);
        }
    }
}

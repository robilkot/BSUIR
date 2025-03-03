using LW1.Common;
using LW1.LineDrawing;
using LW1.LineDrawing.Common;
using LW1.Polygons.Common;

namespace LW1.Polygons
{
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
}

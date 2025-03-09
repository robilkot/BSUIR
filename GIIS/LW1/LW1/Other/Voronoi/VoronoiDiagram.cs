using LW1.Common.Algorithms;
using LW1.Common.Parameters;
using LW1.LineDrawing;
using LW1.LineDrawing.Common;
using LW1.Other.Helpers;
using LW1.Polygons.Common;
using static LW1.Other.Helpers.OtherHelpers;
using static LW1.Common.Helpers;

namespace LW1.Other.Voronoi
{
    public partial class VoronoiDiagram : IOtherDrawingAlgorithm
    {
        public string DisplayName => "Диаграмма Вороного";
        public IDrawingParameters EmptyParameters => new PolygonParameters();

        public IEnumerable<DrawInfo> Draw(IParameters parameters)
        {
            if (parameters is not PolygonParameters param)
                yield break;

            var points = param.Vertices.Select(v => v.Value).Distinct().ToList();
            if (points.Count <= 1)
                yield break;

            // Вычисляем bounding box для отсечения бесконечных отрезков.
            int minX = points.Min(p => p.X);
            int maxX = points.Max(p => p.X);
            int minY = points.Min(p => p.Y);
            int maxY = points.Max(p => p.Y);
            int marginX = (maxX - minX) / 10 + 10;
            int marginY = (maxY - minY) / 10 + 10;
            int bboxMinX = minX - marginX;
            int bboxMaxX = maxX + marginX;
            int bboxMinY = minY - marginY;
            int bboxMaxY = maxY + marginY;
            var bbox = new Rectangle(bboxMinX, bboxMinY, bboxMaxX - bboxMinX, bboxMaxY - bboxMinY);

            var lineAlgorithm = new Wu();

            // Специальный случай для двух точек: перпендикулярная биссектриса
            if (points.Count == 2)
            {
                var a = points[0];
                var b = points[1];
                var mid = new Point((a.X + b.X) / 2, (a.Y + b.Y) / 2);
                double dx = b.X - a.X;
                double dy = b.Y - a.Y;
                // Выбираем перпендикуляр (dy, -dx)
                double len = Math.Sqrt(dx * dx + dy * dy);
                if (len == 0)
                    yield break;
                double vx = dy / len;
                double vy = -dx / len;
                // Выбираем достаточно большое t, чтобы луч пересёк bbox
                double t = Math.Max(bboxMaxX - bboxMinX, bboxMaxY - bboxMinY);
                var start = new Point((int)Math.Round(mid.X - vx * t), (int)Math.Round(mid.Y - vy * t));
                var end = new Point((int)Math.Round(mid.X + vx * t), (int)Math.Round(mid.Y + vy * t));
                var lineParams = new LineDrawingParameters()
                {
                    Color = param.Color,
                    Start = start,
                    End = end
                };
                foreach (var pt in lineAlgorithm.Draw(lineParams))
                    yield return pt;
                yield break;
            }

            // Для 3 и более точек – наивная триангуляция Делоне
            var triangles = new List<Triangle>();
            for (int i = 0; i < points.Count; i++)
            {
                for (int j = i + 1; j < points.Count; j++)
                {
                    for (int k = j + 1; k < points.Count; k++)
                    {
                        if (AreCollinear(points[i], points[j], points[k]))
                            continue;
                        if (IsDelaunayTriangle(points[i], points[j], points[k], points))
                        {
                            var circumcenter = ComputeCircumcenter(points[i], points[j], points[k]);
                            triangles.Add(new Triangle(points[i], points[j], points[k], circumcenter));
                        }
                    }
                }
            }

            // Построим словарь ребер триангуляции (каждое ребро без направления) -> список треугольников
            var edgeDict = new Dictionary<UndirectedEdge, List<Triangle>>(new UndirectedEdgeComparer());
            foreach (var tri in triangles)
            {
                AddEdge(edgeDict, new UndirectedEdge(tri.A, tri.B), tri);
                AddEdge(edgeDict, new UndirectedEdge(tri.B, tri.C), tri);
                AddEdge(edgeDict, new UndirectedEdge(tri.C, tri.A), tri);
            }

            // Для каждого ребра строим соответствующий отрезок диаграммы Вороного
            foreach (var kv in edgeDict)
            {
                var edge = kv.Key;
                var tris = kv.Value;
                Point start, end;
                if (tris.Count == 2)
                {
                    // Внутреннее ребро: соединяем центры описанных окружностей двух треугольников
                    var c1 = tris[0].Circumcenter;
                    var c2 = tris[1].Circumcenter;
                    start = new Point((int)Math.Round(c1.X), (int)Math.Round(c1.Y));
                    end = new Point((int)Math.Round(c2.X), (int)Math.Round(c2.Y));
                }
                else
                {
                    // Граничное ребро: строим луч из центра описанной окружности треугольника
                    var tri = tris[0];
                    var c = tri.Circumcenter;
                    // Вычисляем середину ребра
                    double mx = (edge.A.X + edge.B.X) / 2.0;
                    double my = (edge.A.Y + edge.B.Y) / 2.0;
                    // Вектор ребра
                    double dx = edge.B.X - edge.A.X;
                    double dy = edge.B.Y - edge.A.Y;
                    // Два перпендикулярных вектора
                    double candidate1 = (c.X - mx) * dy + (c.Y - my) * -dx;
                    double candidate2 = (c.X - mx) * -dy + (c.Y - my) * dx;
                    double vx, vy;
                    if (candidate1 > candidate2)
                    {
                        vx = dy;
                        vy = -dx;
                    }
                    else
                    {
                        vx = -dy;
                        vy = dx;
                    }

                    // Инвертируем направление, если оно указывает к центру треугольника
                    if ((c.X - mx) * vx + (c.Y - my) * vy > 0)
                    {
                        vx = -vx;
                        vy = -vy;
                    }

                    double len = Math.Sqrt(vx * vx + vy * vy);
                    if (len == 0)
                        continue;
                    vx /= len;
                    vy /= len;
                    // Строим луч, начинающийся в c, и находим точку пересечения с bbox
                    var origin = new PointF(c.X, c.Y);
                    var dir = new PointF((float)vx, (float)vy);

                    var pre_end = new PointF(origin.X + dir.X, origin.Y + dir.Y);

                    // Инвертируем луч, если он "крайний" и направлен внутрь диаграммы
                    var checkPoint = triangles
                        .SelectMany(t => t.Select(a => a))
                        .OrderBy(p => Distance(p, edge.A) + Distance(p, edge.B))
                        .First(p => edge.A != p && edge.B != p);

                    if(Distance(checkPoint, origin) > Distance(checkPoint, pre_end))
                    {
                        dir = new(-dir.X, -dir.Y);
                    }

                    // Debug
                    //var pp = new PointDrawingParameters()
                    //{
                    //    Color = Color.Red,
                    //    Point = new Point((int)origin.X, (int)origin.Y),
                    //};
                    //foreach (var pt in new CrossDrawingAlgorithm().Draw(pp))
                    //    yield return pt;

                    //pp = new PointDrawingParameters()
                    //{
                    //    Color = Color.Blue,
                    //    Point = new Point((int)(pre_end.X), (int)(pre_end.Y)),
                    //};
                    //foreach (var pt in new CrossDrawingAlgorithm().Draw(pp))
                    //    yield return pt;

                    var intersect = ComputeRayBoxIntersection(origin, dir, bbox);
                    if (intersect == null)
                        continue;
                    start = new((int)Math.Round(c.X), (int)Math.Round(c.Y));
                    end = new((int)Math.Round(intersect.Value.X), (int)Math.Round(intersect.Value.Y));
                }
                var lineParams = new LineDrawingParameters()
                {
                    Color = param.Color,
                    Start = start,
                    End = end
                };
                foreach (var pt in lineAlgorithm.Draw(lineParams))
                    yield return pt;
            }
        }

        private static void AddEdge(Dictionary<UndirectedEdge, List<Triangle>> dict, UndirectedEdge edge, Triangle tri)
        {
            if (!dict.ContainsKey(edge))
                dict[edge] = [];
            dict[edge].Add(tri);
        }
    }
}
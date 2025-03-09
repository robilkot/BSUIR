using LW1.Common.Algorithms;
using LW1.Common.Parameters;
using LW1.LineDrawing;
using LW1.LineDrawing.Common;
using LW1.Other.Helpers;
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

            // Перебираем все возможные тройки точек и выбираем те, у которых
            // описанная окружность не содержит ни одной другой точки.
            var triangles = new List<(Point A, Point B, Point C)>();
            for (int i = 0; i < points.Count; i++)
            {
                for (int j = i + 1; j < points.Count; j++)
                {
                    for (int k = j + 1; k < points.Count; k++)
                    {
                        if (Helpers.OtherHelpers.IsDelaunayTriangle(points[i], points[j], points[k], points))
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
    }
}
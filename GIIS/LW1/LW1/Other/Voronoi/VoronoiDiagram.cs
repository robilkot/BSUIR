using LW1.Common.Algorithms;
using LW1.Common.Parameters;
using LW1.Polygons.Common;

namespace LW1.Other.Voronoi
{
    public class VoronoiDiagram : IOtherDrawingAlgorithm
    {
        public string DisplayName => "Диаграмма Вороного";

        public IDrawingParameters EmptyParameters => new PolygonParameters();

        public IEnumerable<DrawInfo> Draw(IParameters parameters)
        {
            if (parameters is not PolygonParameters param)
                yield break;

        }
    }
}

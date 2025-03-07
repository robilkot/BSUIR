using LW1.Common;
using LW1.Common.Shapes;
using LW1.LineDrawing;
using LW1.LineDrawing.Common;
using LW1.Polygons.Common;

namespace LW1.Polygons
{
    public class SimplePolygonDrawingAlgorithm : IPolygonDrawingAlgorithm
    {
        public IDrawingParameters EmptyParameters => new PolygonParameters();
        public string DisplayName => "Полигон по точкам";

        public IEnumerable<DrawInfo> Draw(IParameters parameters)
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
}

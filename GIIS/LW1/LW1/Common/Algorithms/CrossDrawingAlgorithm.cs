using LW1.Common.Parameters;
using LW1.LineDrawing;
using LW1.LineDrawing.Common;

namespace LW1.Common.Algorithms
{
    public class CrossDrawingAlgorithm : IDrawingAlgorithm
    {
        private static readonly int CrossLeaf = 2;
        public IDrawingParameters EmptyParameters => new PointDrawingParameters();

        public string DisplayName => throw new NotImplementedException();

        public IEnumerable<DrawInfo> Draw(IParameters parameters)
        {
            if (parameters is not PointDrawingParameters pointParams)
                yield break;

            var cda = new CDA();
            var center = pointParams.Point.Value;

            Point begin = new(center.X - CrossLeaf, center.Y);
            Point end = new(center.X + CrossLeaf, center.Y);
            LineDrawingParameters lineParams = new()
            {
                Start = begin,
                End = end,
                Color = pointParams.Color,
            };
            foreach (var pair in cda.Draw(lineParams))
            {
                yield return pair;
            }

            begin = new(center.X, center.Y - CrossLeaf);
            end = new(center.X, center.Y + CrossLeaf);
            lineParams = new()
            {
                Start = begin,
                End = end,
                Color = pointParams.Color,
            };
            foreach (var pair in cda.Draw(lineParams))
            {
                yield return pair;
            }
        }
    }
}

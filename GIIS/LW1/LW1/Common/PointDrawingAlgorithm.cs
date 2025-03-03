using LW1.LineDrawing;

namespace LW1.Common
{
    public class PointDrawingAlgorithm : IDrawingAlgorithm
    {
        public IDrawingParameters EmptyParameters => new PointDrawingParameters();

        public string DisplayName => throw new NotImplementedException();

        public IEnumerable<(ColorPoint point, DebugInfo info)> Draw(IDrawingParameters parameters)
        {
            if (parameters is not PointDrawingParameters pointParams)
                yield break;

            yield return (new(pointParams.Point, pointParams.Color), new CDADrawInfo() { });
        }
    }
}

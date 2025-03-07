using LW1.Common.Parameters;
using LW1.Common.Shapes;

namespace LW1.Common.Algorithms
{
    public class PointDrawingAlgorithm : IDrawingAlgorithm
    {
        public IDrawingParameters EmptyParameters => new PointDrawingParameters();

        public string DisplayName => throw new NotImplementedException();

        public IEnumerable<DrawInfo> Draw(IParameters parameters)
        {
            if (parameters is not PointDrawingParameters pointParams)
                yield break;

            yield return new()
            {
                Drawable = new ColorPoint(pointParams.Point, pointParams.Color),
            };
        }
    }
}

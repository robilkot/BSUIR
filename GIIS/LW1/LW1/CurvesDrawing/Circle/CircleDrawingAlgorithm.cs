using LW1.Common;
using LW1.LineDrawing;

namespace LW1.CurvesDrawing.Circle
{
    public class CircleDrawingAlgorithm : ICurveDrawingAlgorithm
    {
        public string DisplayName => "Окружность";

        public IDrawingParameters EmptyParameters => new CircleDrawingParameters();

        public IEnumerable<(ColorPoint point, IDebugInfo info)> Draw<T>(T parameters) where T : IDrawingParameters
        {
            throw new NotImplementedException();
        }
    }
}

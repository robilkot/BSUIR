using LW1.Common;
using LW1.LineDrawing;

namespace LW1.CurvesDrawing.Circle
{
    public class CircleDrawingAlgorithm : ICurveDrawingAlgorithm<CircleDrawingParameters>
    {
        public string DisplayName => "Окружность";

        public IEnumerable<(ColorPoint point, IDebugInfo info)> Draw(CircleDrawingParameters parameters)
        {
            throw new NotImplementedException();
        }
    }
}

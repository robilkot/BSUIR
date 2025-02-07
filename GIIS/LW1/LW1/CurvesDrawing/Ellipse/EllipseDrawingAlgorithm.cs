using LW1.Common;
using LW1.LineDrawing;

namespace LW1.CurvesDrawing.Ellipse
{
    public class EllipseDrawingAlgorithm : ICurveDrawingAlgorithm<EllipseDrawingParameters>
    {
        public string DisplayName => "Эллипс";

        public IEnumerable<(ColorPoint point, IDebugInfo info)> Draw(EllipseDrawingParameters parameters)
        {
            throw new NotImplementedException();
        }
    }
}

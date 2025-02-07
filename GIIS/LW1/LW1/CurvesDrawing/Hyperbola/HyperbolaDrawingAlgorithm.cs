using LW1.Common;
using LW1.LineDrawing;

namespace LW1.CurvesDrawing.Hyperbola
{
    public class HyperbolaDrawingAlgorithm : ICurveDrawingAlgorithm<HyperbolaDrawingParameters>
    {
        public string DisplayName => "Гипербола";

        public IEnumerable<(ColorPoint point, IDebugInfo info)> Draw(HyperbolaDrawingParameters parameters)
        {
            throw new NotImplementedException();
        }
    }
}

using LW1.Common;
using LW1.LineDrawing;

namespace LW1.CurvesDrawing.Parabola
{
    public class ParabolaDrawingAlgorithm : ICurveDrawingAlgorithm<ParabolaDrawingParameters>
    {
        public string DisplayName => "Парабола";

        public IEnumerable<(ColorPoint point, IDebugInfo info)> Draw(ParabolaDrawingParameters parameters)
        {
            throw new NotImplementedException();
        }
    }
}

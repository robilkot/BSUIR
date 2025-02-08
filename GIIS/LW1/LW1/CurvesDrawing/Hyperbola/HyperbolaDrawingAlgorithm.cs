using LW1.Common;
using LW1.LineDrawing;

namespace LW1.CurvesDrawing.Hyperbola
{
    public class HyperbolaDrawingAlgorithm : ICurveDrawingAlgorithm
    {
        public string DisplayName => "Гипербола";

        public IDrawingParameters EmptyParameters => new HyperbolaDrawingParameters();

        public IEnumerable<(ColorPoint point, IDebugInfo info)> Draw<T>(T parameters) where T : IDrawingParameters
        {
            throw new NotImplementedException();
        }
    }
}

using LW1.Common;
using LW1.CurvesDrawing.Common;

namespace LW1.CurvesDrawing
{
    public class HyperbolaDrawingParameters : CurveDrawingParameters
    {
        public override Color Color { get; set; }
    }
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

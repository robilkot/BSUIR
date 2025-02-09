using LW1.Common;
using LW1.CurvesDrawing.Common;

namespace LW1.CurvesDrawing
{
    public class EllipseDrawingParameters : CurveDrawingParameters
    {
        public override Color Color { get; set; }
    }
    public class EllipseDrawingAlgorithm : ICurveDrawingAlgorithm
    {
        public string DisplayName => "Эллипс";

        public IDrawingParameters EmptyParameters => new EllipseDrawingParameters();

        public IEnumerable<(ColorPoint point, IDebugInfo info)> Draw<T>(T parameters) where T : IDrawingParameters
        {
            throw new NotImplementedException();
        }
    }
}

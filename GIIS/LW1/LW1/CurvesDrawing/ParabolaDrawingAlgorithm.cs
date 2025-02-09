using LW1.Common;
using LW1.CurvesDrawing.Common;

namespace LW1.CurvesDrawing
{
    public class ParabolaDrawingParameters : CurveDrawingParameters
    {
        public override Color Color { get; set; }
    }
    public class ParabolaDrawingAlgorithm : ICurveDrawingAlgorithm
    {
        public string DisplayName => "Парабола";

        public IDrawingParameters EmptyParameters => new ParabolaDrawingParameters();

        public IEnumerable<(ColorPoint point, IDebugInfo info)> Draw<T>(T parameters) where T : IDrawingParameters
        {
            throw new NotImplementedException();
        }
    }
}

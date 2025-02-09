using LW1.Common;

namespace LW1.CurvesDrawing.Common
{
    public abstract class CurveDrawingParameters : IDrawingParameters
    {
        public abstract Color Color { get; set; }
    }
}

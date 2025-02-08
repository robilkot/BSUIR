using LW1.Common;

namespace LW1.LineDrawing
{
    public abstract class CurveDrawingParameters : IDrawingParameters
    {
        public abstract Color Color { get; set; }
    }
}

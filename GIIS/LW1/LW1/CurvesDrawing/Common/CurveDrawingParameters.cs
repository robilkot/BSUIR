using LW1.Common;

namespace LW1.CurvesDrawing.Common
{
    public abstract class CurveDrawingParameters : IDrawingParameters
    {
        public Parameter<Color> Color { get; init; } = new() { DisplayName = "Цвет", Value = System.Drawing.Color.Black };
    }
}

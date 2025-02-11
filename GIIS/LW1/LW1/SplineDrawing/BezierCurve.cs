using LW1.Common;
using LW1.SplineDrawing.Common;

namespace LW1.SplineDrawing
{
    public class BezierCurveParameters : IDrawingParameters
    {
        public Parameter<Color> Color { get; init; } = new() { DisplayName = "Цвет", Value = System.Drawing.Color.Black };
    }

    public class BezierCurve : ISplineDrawingAlgorithm
    {
        public string DisplayName => "Кривая Безье";

        public IDrawingParameters EmptyParameters => new BezierCurveParameters();

        public IEnumerable<(ColorPoint point, IDebugInfo info)> Draw<T>(T parameters) where T : IDrawingParameters
        {
            throw new NotImplementedException();
        }
    }
}

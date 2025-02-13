using LW1.Common;
using LW1.SplineDrawing.Common;

namespace LW1.SplineDrawing
{
    public class BSplinemParameters : IDrawingParameters
    {
        public Parameter<Color> Color { get; init; } = new() { DisplayName = "Цвет", Value = System.Drawing.Color.Black };
    }

    public class BSpline : ISplineDrawingAlgorithm
    {
        public string DisplayName => "B-Сплайн";

        public IDrawingParameters EmptyParameters => new BSplinemParameters();

        public IEnumerable<(ColorPoint point, IDebugInfo info)> Draw(IDrawingParameters parameters)
        {
            throw new NotImplementedException();
        }
    }
}

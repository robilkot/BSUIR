using LW1.Common;
using LW1.SplineDrawing.Common;

namespace LW1.SplineDrawing
{
    public class HermitianFormParameters : IDrawingParameters
    {
        public Parameter<Color> Color { get; init; } = new() { DisplayName = "Цвет", Value = System.Drawing.Color.Black };
    }

    public class HermitianForm : ISplineDrawingAlgorithm
    {
        public string DisplayName => "Форма Эрмита";

        public IDrawingParameters EmptyParameters => new HermitianFormParameters();

        public IEnumerable<(ColorPoint point, IDebugInfo info)> Draw<T>(T parameters) where T : IDrawingParameters
        {
            throw new NotImplementedException();
        }
    }
}

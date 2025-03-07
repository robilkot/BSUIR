using LW1.Common.Parameters;

namespace LW1.LineDrawing.Common
{
    public class LineDrawingParameters : IDrawingParameters
    {
        public Parameter<Color> Color { get; init; } = new() { DisplayName = "Цвет", Value = System.Drawing.Color.Black };
        public Parameter<Point> Start { get; init; } = new() { DisplayName = "Начало", Value = new(3, 26) };
        public Parameter<Point> End { get; init; } = new() { DisplayName = "Конец", Value = new(29, 5) };
    }
}

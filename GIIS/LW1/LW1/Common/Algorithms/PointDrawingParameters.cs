namespace LW1.Common.Algorithms
{
    public class PointDrawingParameters : IDrawingParameters
    {
        public Parameter<Color> Color { get; init; } = new() { DisplayName = "Цвет", Value = System.Drawing.Color.Black };
        public Parameter<Point> Point { get; init; } = new() { DisplayName = "Точка", Value = new(20, 20) };
    }
}

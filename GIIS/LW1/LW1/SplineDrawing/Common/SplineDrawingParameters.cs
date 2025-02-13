using LW1.Common;

namespace LW1.SplineDrawing.Common
{
    public class SplineDrawingParameters : IDrawingParameters
    {
        public Parameter<Color> Color { get; init; } = new() { DisplayName = "Цвет", Value = System.Drawing.Color.Black };
        public Parameter<Point> P1 { get; init; } = new() { DisplayName = "P1", Value = new(0, 0) };
        public Parameter<Point> P2 { get; init; } = new() { DisplayName = "P2", Value = new(0, 0) };
        public Parameter<Point> P3 { get; init; } = new() { DisplayName = "P3", Value = new(0, 0) };
        public Parameter<Point> P4 { get; init; } = new() { DisplayName = "P4", Value = new(0, 0) };
        public Parameter<Point> R1 { get; init; } = new() { DisplayName = "R1", Value = new(0, 0) };
        public Parameter<Point> R2 { get; init; } = new() { DisplayName = "R2", Value = new(0, 0) };
    }
}

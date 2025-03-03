using LW1.Common;

namespace LW1.Polygons
{
    public class PolygonParameters : IDrawingParameters
    {
        public Parameter<Color> Color { get; init; } = new() { DisplayName = "Цвет", Value = System.Drawing.Color.Black };
        public ParametersList<Point> Vertices { get; init; } = new("Вершины")
        {
            new() { DisplayName = "P1", Value = new(24, 21) },
            new() { DisplayName = "P2", Value = new(31, 4) },
            new() { DisplayName = "P3", Value = new(38, 21) },
            new() { DisplayName = "P4", Value = new(56, 25) },
            new() { DisplayName = "P5", Value = new(43, 38) },
            new() { DisplayName = "P6", Value = new(50, 55) },
            new() { DisplayName = "P7", Value = new(31, 43) },
            new() { DisplayName = "P8", Value = new(13, 55) },
            new() { DisplayName = "P9", Value = new(18, 37) },
            new() { DisplayName = "P10", Value = new(6, 25) },
        };
    }
}

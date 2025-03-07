using LW1.Common;

namespace LW1.Polygons.Common
{
    public class PolygonParameters : IDrawingParameters
    {
        public Parameter<Color> Color { get; init; } = new() { DisplayName = "Цвет", Value = System.Drawing.Color.Black };
        public ParametersList<Point> Vertices { get; init; } = new("Вершины")
        {
            new() { DisplayName = "P1", Value = new(32, 45) },
            new() { DisplayName = "P2", Value = new(51, 15) },
            new() { DisplayName = "P3", Value = new(53, 51) },
            new() { DisplayName = "P4", Value = new(32, 24) },
            new() { DisplayName = "P5", Value = new(11, 45) },
            new() { DisplayName = "P6", Value = new(10, 17) },
        };
    }
}

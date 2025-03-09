using LW1.Common.Parameters;

namespace LW1.Polygons.Common
{
    public class PolygonParameters : IDrawingParameters
    {
        public Parameter<Color> Color { get; init; } = new() { DisplayName = "Цвет", Value = System.Drawing.Color.Black };
        public ParametersList<Point> Vertices { get; init; } = new("Вершины")
        {
            new() { DisplayName = "P1", Value = new(32 * 4, 45 * 4) },
            new() { DisplayName = "P2", Value = new(51 * 4, 15 * 4) },
            new() { DisplayName = "P3", Value = new(53 * 4, 51 * 4) },
            new() { DisplayName = "P4", Value = new(32 * 4, 24 * 4) },
            new() { DisplayName = "P5", Value = new(11 * 4, 45 * 4) },
            new() { DisplayName = "P6", Value = new(10 * 4, 17 * 4) },
        };
    }
}

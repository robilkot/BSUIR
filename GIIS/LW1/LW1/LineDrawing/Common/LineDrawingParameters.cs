using LW1.Common;

namespace LW1.LineDrawing.Common
{
    public class LineDrawingParameters : IDrawingParameters
    {
        public Parameter<int> StartX { get; init; } = new() { DisplayName = "Начало (X)", Value = 3 };
        public Parameter<int> StartY { get; init; } = new() { DisplayName = "Начало (Y)", Value = 26 };
        public Parameter<int> EndX { get; init; } = new() { DisplayName = "Конец (X)", Value = 29 };
        public Parameter<int> EndY { get; init; } = new() { DisplayName = "Конец (Y)", Value = 5 };
        public Parameter<Color> Color { get; init; } = new() { DisplayName = "Цвет", Value = System.Drawing.Color.Black };
    }
}

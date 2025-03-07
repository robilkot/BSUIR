namespace LW1.Common
{
    public class ApplicationParameters : IParameters
    {
        public Parameter<Size> CanvasSize { get; init; } = new() { DisplayName = "Размер холста", Value = new(256, 256) };
        public Parameter<int> CanvasPixelSize { get; init; } = new() { DisplayName = "Размер пикселя на холсте", Value = 2 };
    }
}

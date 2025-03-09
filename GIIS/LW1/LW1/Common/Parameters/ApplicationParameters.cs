using LW1.Common.Parameters;

namespace LW1.Common
{
    public class ApplicationParameters : IParameters
    {
        public Parameter<Size> CanvasSize { get; init; } = new() { DisplayName = "Размер холста (px)", Value = new(256, 256) };
        public Parameter<int> CanvasPixelSize { get; init; } = new() { DisplayName = "Размер пикселя на холсте (px)", Value = 2 };
        public Parameter<int> DebugStepsInterval { get; init; } = new() { DisplayName = "Интервал шагов отладки (ms)", Value = 75 };
    }
}

using LW1.Common;
using LW1.CurvesDrawing.Common;

namespace LW1.CurvesDrawing
{
    public class HyperbolaDrawingInfo : IDebugInfo
    {
        public required int Iteration { get; set; }
        public required double Delta { get; set; }
        public required int DisplayX { get; set; }
        public required int DisplayY { get; set; }
        public IEnumerable<string> Columns => ["i", "delta", "(x, y)"];
        public IEnumerable<string> Row => [$"{Iteration}", $"{Delta:F2}", $"{DisplayX}, {DisplayY}"];
    }
    public class HyperbolaDrawingParameters : CurveDrawingParameters
    {
        public Parameter<int> CenterX { get; init; } = new() { DisplayName = "Центр (X)", Value = 15 };
        public Parameter<int> CenterY { get; init; } = new() { DisplayName = "Центр (Y)", Value = 15 };
        public Parameter<int> A { get; init; } = new() { DisplayName = "A", Value = 6 };
        public Parameter<int> B { get; init; } = new() { DisplayName = "B", Value = 6 };
        public Parameter<int> MaximumX { get; init; } = new() { DisplayName = "Ограничение (X)", Value = 31 };
    }
    public class HyperbolaDrawingAlgorithm : ICurveDrawingAlgorithm
    {
        public string DisplayName => "Гипербола";

        public IDrawingParameters EmptyParameters => new HyperbolaDrawingParameters();

        public IEnumerable<(ColorPoint point, IDebugInfo info)> Draw<T>(T param) where T : IDrawingParameters
        {
            if (param is not HyperbolaDrawingParameters parameters) yield break;

            IEnumerable<(ColorPoint point, IDebugInfo info)> yieldPoint(int i, int delta, int x, int y, HyperbolaDrawingParameters parameters)
            {
                Point[] points = [
                    new(parameters.CenterX.Value + x, parameters.CenterY.Value + y),
                    new(parameters.CenterX.Value - x, parameters.CenterY.Value + y),
                    new(parameters.CenterX.Value + x, parameters.CenterY.Value - y),
                    new(parameters.CenterX.Value - x, parameters.CenterY.Value - y)
                ];

                foreach (var point in points)
                {
                    var info = new HyperbolaDrawingInfo()
                    {
                        Iteration = i,
                        Delta = delta,
                        DisplayX = point.X,
                        DisplayY = point.Y,
                    };
                    yield return (new(point, parameters.Color.Value), info);
                }
            }

            int a = parameters.A.Value;
            int b = parameters.B.Value;
            int x = a;
            int y = 0;

            double delta = a * a - 2 * a * b * b + b * b;

            int iteration = 0;
            while (parameters.MaximumX.Value == 0 || x < parameters.MaximumX.Value)
            {
                foreach (var point in yieldPoint(iteration, (int)delta, x, y, parameters))
                {
                    yield return point;
                }

                if (delta < 0)
                {
                    delta += 2 * a * a * y + 3 * a * a;
                    y++;
                }
                else
                {
                    delta += -2 * b * b * x + 2 * a * a * y + 3 * a * a;
                }
                x++;
                iteration++;
            }
        }
    }
}
using LW1.Common;
using LW1.CurvesDrawing.Common;

namespace LW1.CurvesDrawing
{
    public class HyperbolaDrawingInfo : DebugInfo
    {
        public required int Iteration { get; set; }
        public required double Delta { get; set; }
        public required int DisplayX { get; set; }
        public required int DisplayY { get; set; }
    }
    public class HyperbolaDrawingParameters : IDrawingParameters
    {
        public Parameter<Color> Color { get; init; } = new() { DisplayName = "Цвет", Value = System.Drawing.Color.Black };
        public Parameter<Point> Center { get; init; } = new() { DisplayName = "Центр", Value = new(15, 15) };
        public Parameter<int> A { get; init; } = new() { DisplayName = "A", Value = 6 };
        public Parameter<int> B { get; init; } = new() { DisplayName = "B", Value = 6 };
        public Parameter<int> MaximumX { get; init; } = new() { DisplayName = "Ограничение (X)", Value = 31 };
    }
    public class HyperbolaDrawingAlgorithm : ICurveDrawingAlgorithm
    {
        public string DisplayName => "Гипербола";

        public IDrawingParameters EmptyParameters => new HyperbolaDrawingParameters();

        public IEnumerable<(ColorPoint point, DebugInfo info)> Draw(IDrawingParameters param)
        {
            if (param is not HyperbolaDrawingParameters parameters) yield break;

            IEnumerable<(ColorPoint point, DebugInfo info)> yieldPoint(int i, int delta, int x, int y, HyperbolaDrawingParameters parameters)
            {
                Point[] points = [
                    new(parameters.Center.Value.X + x, parameters.Center.Value.Y + y),
                    new(parameters.Center.Value.X - x, parameters.Center.Value.Y + y),
                    new(parameters.Center.Value.X + x, parameters.Center.Value.Y - y),
                    new(parameters.Center.Value.X - x, parameters.Center.Value.Y - y)
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
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
        public override Color Color { get; set; }
        public int CenterX { get; set; } = 15;
        public int CenterY { get; set; } = 15;
        public int A { get; set; } = 6;
        public int B { get; set; } = 6;
        public int MaximumX { get; set; } = 31;
        public int MaximumY { get; set; } = 31;
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
                    new(parameters.CenterX + x, parameters.CenterY + y),
                    new(parameters.CenterX - x, parameters.CenterY + y),
                    new(parameters.CenterX + x, parameters.CenterY - y),
                    new(parameters.CenterX - x, parameters.CenterY - y)
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
                    yield return (new(point, parameters.Color), info);
                }
            }

            int a = parameters.A;
            int b = parameters.B;
            int x = a;
            int y = 0;

            double delta = a * a - 2 * a * b * b + b * b;

            int iteration = 0;
            while ((parameters.MaximumX == 0 || x < parameters.MaximumX) && (parameters.MaximumY == 0 || y < parameters.MaximumY))
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
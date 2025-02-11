using LW1.Common;
using LW1.CurvesDrawing.Common;

namespace LW1.CurvesDrawing
{
    public class EllipseDrawingInfo : IDebugInfo
    {
        public required int Iteration { get; set; }
        public required double Delta { get; set; }
        public required double? Sigma { get; set; }
        public required double? SigmaStar { get; set; }
        public required char? Pixel { get; set; }
        public required int DisplayX { get; set; }
        public required int DisplayY { get; set; }
        public IEnumerable<string> Columns => ["i", "delta", "sigma", "sigma*", "pixel", "(x, y)"];
        public IEnumerable<string> Row => [$"{Iteration}", $"{Delta:F2}", $"{Sigma:F2}", $"{SigmaStar:F2}", $"{Pixel}", $"{DisplayX}, {DisplayY}"];
    }
    public class EllipseDrawingParameters : CurveDrawingParameters
    {
        public Parameter<int> CenterX { get; init; } = new() { DisplayName = "Центр (X)", Value = 15 };
        public Parameter<int> CenterY { get; init; } = new() { DisplayName = "Центр (Y)", Value = 15 };
        public Parameter<int> A { get; init; } = new() { DisplayName = "A", Value = 7 };
        public Parameter<int> B { get; init; } = new() { DisplayName = "B", Value = 4 };
    }
    public class EllipseDrawingAlgorithm : ICurveDrawingAlgorithm
    {
        public string DisplayName => "Эллипс";

        public IDrawingParameters EmptyParameters => new EllipseDrawingParameters();

        public IEnumerable<(ColorPoint point, IDebugInfo info)> Draw<T>(T param) where T : IDrawingParameters
        {
            if (param is not EllipseDrawingParameters parameters) yield break;

            IEnumerable<(ColorPoint point, IDebugInfo info)> yieldPoint(int i, int delta, int? sigma, int? sigma_star, char? pixel, int x, int y, EllipseDrawingParameters parameters)
            {
                Point[] points = [
                    new(parameters.CenterX.Value + x, parameters.CenterY.Value + y),
                    new(parameters.CenterX.Value - x, parameters.CenterY.Value + y),
                    new(parameters.CenterX.Value + x, parameters.CenterY.Value - y),
                    new(parameters.CenterX.Value - x, parameters.CenterY.Value - y)
                    ];

                foreach (var point in points)
                {
                    var info = new CircleDrawingInfo()
                    {
                        Iteration = i,
                        Delta = delta,
                        Sigma = sigma,
                        SigmaStar = sigma_star,
                        DisplayX = point.X,
                        DisplayY = point.Y,
                        Pixel = pixel,
                    };

                    yield return (new(point, parameters.Color.Value), info);
                }
            }

            var x = 0;
            var y = parameters.B.Value;
            int limit = 0;
            int delta = parameters.A.Value * parameters.A.Value + parameters.B.Value * parameters.B.Value - 2 * parameters.A.Value * parameters.A.Value * parameters.B.Value;

            foreach (var point in yieldPoint(0, delta, null, null, null, x, y, parameters))
            {
                yield return point;
            }

            char chooseDiagonal()
            {
                x++;
                y--;
                delta = delta + parameters.B.Value * parameters.B.Value * (2 * x + 1) + parameters.A.Value * parameters.A.Value * (1 - 2 * y);
                return 'D';
            }
            char chooseHorizontal()
            {
                x++;
                delta = delta + parameters.B.Value * parameters.B.Value * (2 * x + 1);
                return 'H';
            }
            char chooseVertical()
            {
                y--;
                delta = delta + parameters.A.Value * parameters.A.Value * (1 - 2 * y);
                return 'V';
            }

            for (int i = 1; y > limit; i++)
            {
                int? sigma = null;
                int? sigma_star = null;
                char? pixel = null;

                if (delta > 0)
                {
                    sigma_star = 2 * (delta  - parameters.B.Value * parameters.B.Value * x) - 1;

                    if (sigma_star <= 0)
                    {
                        pixel = chooseDiagonal();
                    }
                    else
                    {
                        pixel = chooseVertical();
                    }
                }
                else if (delta < 0)
                {
                    sigma = 2 * (delta + parameters.A.Value * parameters.A.Value * y) - 1;

                    if (sigma > 0)
                    {
                        pixel = chooseDiagonal();
                    }
                    else
                    {
                        pixel = chooseHorizontal();
                    }
                }
                else
                {
                    pixel = chooseDiagonal();
                }

                foreach (var point in yieldPoint(i, delta, sigma, sigma_star, pixel, x, y, parameters))
                {
                    yield return point;
                }
            }
        }
    }
}

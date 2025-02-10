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
        public override Color Color { get; set; }
        public int CenterX { get; set; }
        public int CenterY { get; set; }
        public int A { get; set; }
        public int B { get; set; }
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
                    new(parameters.CenterX + x, parameters.CenterY + y),
                    new(parameters.CenterX - x, parameters.CenterY + y),
                    new(parameters.CenterX + x, parameters.CenterY - y),
                    new(parameters.CenterX - x, parameters.CenterY - y)
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

                    yield return (new(point, parameters.Color), info);
                }
            }

            var x = 0;
            var y = parameters.B;
            int limit = 0;
            int delta = parameters.A * parameters.A + parameters.B * parameters.B - 2 * parameters.A * parameters.A * parameters.B;

            foreach (var point in yieldPoint(0, delta, null, null, null, x, y, parameters))
            {
                yield return point;
            }

            char chooseDiagonal()
            {
                x++;
                y--;
                delta = delta + parameters.B * parameters.B * (2 * x + 1) + parameters.A * parameters.A * (1 - 2 * y);
                return 'D';
            }
            char chooseHorizontal()
            {
                x++;
                delta = delta + parameters.B * parameters.B * (2 * x + 1);
                return 'H';
            }
            char chooseVertical()
            {
                y--;
                delta = delta + parameters.A * parameters.A * (1 - 2 * y);
                return 'V';
            }

            for (int i = 1; y > limit; i++)
            {
                int? sigma = null;
                int? sigma_star = null;
                char? pixel = null;

                if (delta > 0)
                {
                    sigma_star = 2 * (delta  - parameters.B * parameters.B * x) - 1;

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
                    sigma = 2 * (delta + parameters.A * parameters.A * y) - 1;

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

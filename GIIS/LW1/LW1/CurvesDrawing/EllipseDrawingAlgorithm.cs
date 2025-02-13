using LW1.Common;
using LW1.CurvesDrawing.Common;

namespace LW1.CurvesDrawing
{
    public class EllipseDrawingInfo : DebugInfo
    {
        public required int Iteration { get; set; }
        public required double Delta { get; set; }
        public required double? Sigma { get; set; }
        public required double? SigmaStar { get; set; }
        public required char? Pixel { get; set; }
        public required int DisplayX { get; set; }
        public required int DisplayY { get; set; }
    }
    public class EllipseDrawingParameters : IDrawingParameters
    {
        public Parameter<Color> Color { get; init; } = new() { DisplayName = "Цвет", Value = System.Drawing.Color.Black };
        public Parameter<Point> Center { get; init; } = new() { DisplayName = "Центр", Value = new(15, 15) };
        public Parameter<int> A { get; init; } = new() { DisplayName = "A", Value = 9 };
        public Parameter<int> B { get; init; } = new() { DisplayName = "B", Value = 4 };
    }
    public class EllipseDrawingAlgorithm : ICurveDrawingAlgorithm
    {
        public string DisplayName => "Эллипс";

        public IDrawingParameters EmptyParameters => new EllipseDrawingParameters();

        public IEnumerable<(ColorPoint point, DebugInfo info)> Draw(IDrawingParameters param)
        {
            if (param is not EllipseDrawingParameters parameters) yield break;

            IEnumerable<(ColorPoint point, DebugInfo info)> yieldPoint(int i, int delta, int? sigma, int? sigma_star, char? pixel, int x, int y, EllipseDrawingParameters parameters)
            {
                Point[] points = [
                    new(parameters.Center.Value.X + x, parameters.Center.Value.Y + y),
                    new(parameters.Center.Value.X - x, parameters.Center.Value.Y + y),
                    new(parameters.Center.Value.X + x, parameters.Center.Value.Y - y),
                    new(parameters.Center.Value.X - x, parameters.Center.Value.Y - y)
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

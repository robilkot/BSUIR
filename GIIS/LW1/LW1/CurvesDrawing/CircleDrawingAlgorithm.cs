using LW1.Common;
using LW1.Common.Shapes;
using LW1.CurvesDrawing.Common;

namespace LW1.CurvesDrawing
{
    public class CircleDrawingInfo : DebugInfo
    {
        public required int Iteration { get; set; }
        public required double Delta { get; set; }
        public required double? Sigma { get; set; }
        public required double? SigmaStar { get; set; }
        public required char? Pixel { get; set; }
        public required int DisplayX { get; set; }
        public required int DisplayY { get; set; }
    }

    public class CircleDrawingParameters : IDrawingParameters
    {
        public Parameter<Color> Color { get; init; } = new() { DisplayName = "Цвет", Value = System.Drawing.Color.Black };
        public Parameter<Point> Center { get; init; } = new() { DisplayName = "Центр", Value = new(15, 15) };
        public Parameter<int> Radius { get; init; } = new() { DisplayName = "Радиус", Value = 7 };
    }
    public class CircleDrawingAlgorithm : ICurveDrawingAlgorithm
    {
        public string DisplayName => "Окружность";

        public IDrawingParameters EmptyParameters => new CircleDrawingParameters();

        public IEnumerable<DrawInfo> Draw(IParameters param)
        {
            if(param is not CircleDrawingParameters parameters) yield break;

            IEnumerable<DrawInfo> yieldPoint(int i, int delta, int? sigma, int? sigma_star, char? pixel, int x, int y, CircleDrawingParameters parameters)
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

                    yield return new()
                    {
                        Drawable = new ColorPoint(point, parameters.Color),
                        DebugInfo = info,
                    };
                }
            }

            var x = 0;
            var y = parameters.Radius.Value;
            int limit = 0;
            int delta = 2 - 2 * parameters.Radius.Value;

            foreach (var point in yieldPoint(0, delta, null, null, null, x, y, parameters))
            {
                yield return point;
            }

            char chooseDiagonal()
            {
                x++;
                y--;
                delta = delta + 2 * x - 2 * y + 2;
                return 'D';
            }
            char chooseHorizontal()
            {
                x++;
                delta = delta + 2 * x + 1;
                return 'H';
            }
            char chooseVertical()
            {
                y--;
                delta = delta - 2 * y + 1;
                return 'V';
            }

            for(int i = 1; y > limit; i++)
            {
                int? sigma = null;
                int? sigma_star = null;
                char? pixel = null;

                if (delta > 0)
                {
                    sigma_star = 2 * delta - 2 * x - 1;

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
                    sigma = 2 * delta + 2 * y - 1;

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

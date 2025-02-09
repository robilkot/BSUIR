using LW1.Common;
using LW1.CurvesDrawing.Common;
using System.Drawing;

namespace LW1.CurvesDrawing
{
    public class CircleDrawingInfo : IDebugInfo
    {
        public IEnumerable<string> Columns => throw new NotImplementedException();

        public IEnumerable<string> Row => throw new NotImplementedException();
    }

    public class CircleDrawingParameters : CurveDrawingParameters
    {
        public override Color Color { get; set; }
        public int CenterX { get; set; }
        public int CenterY { get; set; }
        public int Radius { get; set; }
    }
    public class CircleDrawingAlgorithm : ICurveDrawingAlgorithm
    {
        public string DisplayName => "Окружность";

        public IDrawingParameters EmptyParameters => new CircleDrawingParameters();

        public IEnumerable<(ColorPoint point, IDebugInfo info)> Draw<T>(T param) where T : IDrawingParameters
        {
            IEnumerable<(ColorPoint point, IDebugInfo info)> yieldPoint(int x, int y, CircleDrawingParameters parameters)
            {
                var point1 = new ColorPoint(new(parameters.CenterX + x, parameters.CenterY + y), parameters.Color);
                var point2 = new ColorPoint(new(parameters.CenterX - x, parameters.CenterY + y), parameters.Color);
                var point3 = new ColorPoint(new(parameters.CenterX + x, parameters.CenterY - y), parameters.Color);
                var point4 = new ColorPoint(new(parameters.CenterX - x, parameters.CenterY - y), parameters.Color);
                var info = new CircleDrawingInfo();

                foreach (var point in new ColorPoint[] { point1, point2, point3, point4 })
                {
                    yield return (point, info);
                }
            }

            var parameters = param as CircleDrawingParameters;

            var x = 0;
            var y = parameters.Radius;
            double limit = 0;
            double delta = 2 - 2 * parameters.Radius;

            foreach (var point in yieldPoint(x, y, parameters))
            {
                yield return point;
            }

            void chooseDiagonal()
            {
                x++;
                y--;
                delta = delta + 2 * x - 2 * y + 2;
            }
            void chooseHorizontal()
            {
                x++;
                delta = delta + 2 * x + 1;
            }
            void chooseVertical()
            {
                y--;
                delta = delta - 2 * y + 1;
            }

            while (y > limit)
            {
                if (delta > 0)
                {
                    var sigma_star = 2 * delta - 2 * x - 1;

                    if (sigma_star <= 0)
                    {
                        chooseDiagonal();
                    }
                    else
                    {
                        chooseVertical();
                    }
                }
                else if (delta < 0)
                {
                    var sigma = 2 * delta + 2 * y - 1;

                    if (sigma > 0)
                    {
                        chooseDiagonal();
                    }
                    else
                    {
                        chooseHorizontal();
                    }
                }
                else
                {
                    chooseDiagonal();
                }

                foreach (var point in yieldPoint(x, y, parameters))
                {
                    yield return point;
                }
            }
        }
    }
}

using LW1.Common;
using LW1.CurvesDrawing.Common;

namespace LW1.CurvesDrawing
{
    public class ParabolaDrawingParameters : CurveDrawingParameters
    {
        public override Color Color { get; set; }
        public int CenterX { get; set; } = 15;
        public int CenterY { get; set; } = 15;
        public int MaximumX { get; set; } = 31;
        public int MaximumY { get; set; } = 31;
        public int P { get; set; } = 5;
    }
    public class ParabolaDrawingAlgorithm : ICurveDrawingAlgorithm
    {
        public string DisplayName => "Парабола";

        public IDrawingParameters EmptyParameters => new ParabolaDrawingParameters();

        public IEnumerable<(ColorPoint point, IDebugInfo info)> Draw<T>(T param) where T : IDrawingParameters
        {
            if (param is not ParabolaDrawingParameters parameters) yield break;

            IEnumerable<(ColorPoint point, IDebugInfo info)> yieldPoint(int i, int delta, int x, int y, ParabolaDrawingParameters parameters)
            {
                Point[] points = [
                    new(parameters.CenterX + x, parameters.CenterY + y),
                    new(parameters.CenterX + x, parameters.CenterY - y),
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

            int x = 0;
            int y = 0;

            int iteration = 0;
            while((x < parameters.MaximumX || parameters.MaximumX == 0) && (parameters.MaximumY == 0 || y < parameters.MaximumY))
            {
                double delta = y * y - 2 * parameters.P * x;

                foreach (var point in yieldPoint(iteration, (int)delta, x, y, parameters))
                {
                    yield return point;
                }
                
                if(delta < 0)
                {
                    y++;
                }
                else if(delta > 0)
                {
                    x++;
                }
                else
                {
                    x++;
                    y++;
                }
                
                iteration++;
            }
        }
    }
}

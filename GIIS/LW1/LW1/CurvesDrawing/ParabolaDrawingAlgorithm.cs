using LW1.Common;
using LW1.CurvesDrawing.Common;

namespace LW1.CurvesDrawing
{
    public class ParabolaDrawingParameters : IDrawingParameters
    {
        public Parameter<Color> Color { get; init; } = new() { DisplayName = "Цвет", Value = System.Drawing.Color.Black };
        public Parameter<int> CenterX { get; init; } = new() { DisplayName = "Центр (X)", Value = 15 };
        public Parameter<int> CenterY { get; init; } = new() { DisplayName = "Центр (Y)", Value = 15 };
        public Parameter<int> P { get; init; } = new() { DisplayName = "P", Value = 5 };
        public Parameter<int> MaximumX { get; init; } = new() { DisplayName = "Ограничение (X)", Value = 31 };
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
                    new(parameters.CenterX.Value + x, parameters.CenterY.Value + y),
                    new(parameters.CenterX.Value + x, parameters.CenterY.Value - y),
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

            int x = 0;
            int y = 0;

            int iteration = 0;
            while(x < parameters.MaximumX.Value || parameters.MaximumX.Value == 0)
            {
                double delta = y * y - 2 * parameters.P.Value * x;

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

using LW1.Common;
using LW1.LineDrawing.Common;

namespace LW1.LineDrawing
{
    public class CDADrawInfo : IDebugInfo
    {
        public int Iteration { get; set; }
        public double X { get; set; }
        public double Y { get; set; }
        public int DisplayX { get; set; }
        public int DisplayY { get; set; }
        public IEnumerable<string> Columns => ["i", "x", "y", "(x, y)"];
        public IEnumerable<string> Row => [$"{Iteration}", $"{X:F2}", $"{Y:F2}", $"{DisplayX}, {DisplayY}"];
    }

    public class CDA : ILineDrawingAlgorithm
    {
        public IDrawingParameters EmptyParameters => new LineDrawingParameters();
        public string DisplayName => "ЦДА";

        public IEnumerable<(ColorPoint point, IDebugInfo info)> Draw<T>(T param) where T : IDrawingParameters
        {
            if (param is not LineDrawingParameters parameters) yield break;

            var start = new Point(parameters.StartX.Value, parameters.StartY.Value);
            var end = new Point(parameters.EndX.Value, parameters.EndY.Value);
            var color = parameters.Color.Value;

            int len = Math.Max(Math.Abs(start.X - end.X), Math.Abs(start.Y - end.Y));
            double dx = (double)(end.X - start.X) / len;
            double dy = (double)(end.Y - start.Y) / len;

            double x = start.X;
            double y = start.Y;

            for (int i = 0; i <= len; i++)
            {
                var displayX = (int)Math.Round(x);
                var displayY = (int)Math.Round(y);

                var point = new ColorPoint(new(displayX, displayY), color);
                var drawInfo = new CDADrawInfo
                {
                    Iteration = i,
                    X = x,
                    Y = y,
                    DisplayX = displayX,
                    DisplayY = displayY,
                };
                yield return (point, drawInfo);

                x += dx;
                y += dy;
            }
        }
    }
}

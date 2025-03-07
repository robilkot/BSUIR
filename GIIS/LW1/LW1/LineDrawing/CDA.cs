using LW1.Common;
using LW1.Common.Shapes;
using LW1.LineDrawing.Common;

namespace LW1.LineDrawing
{
    public class CDADrawInfo : DebugInfo
    {
        public int Iteration { get; set; }
        public double X { get; set; }
        public double Y { get; set; }
        public int DisplayX { get; set; }
        public int DisplayY { get; set; }
    }

    public class CDA : ILineDrawingAlgorithm
    {
        public IDrawingParameters EmptyParameters => new LineDrawingParameters();
        public string DisplayName => "ЦДА";

        public IEnumerable<DrawInfo> Draw(IParameters param)
        {
            if (param is not LineDrawingParameters parameters) yield break;

            var start = parameters.Start.Value;
            var end = parameters.End.Value;
            var color = parameters.Color;

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
                yield return new()
                {
                    Drawable = point,
                    DebugInfo = drawInfo,
                };

                x += dx;
                y += dy;
            }
        }
    }
}

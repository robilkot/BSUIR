using LW1.Common;
using LW1.Common.Shapes;
using LW1.LineDrawing.Common;

namespace LW1.LineDrawing
{
    public class BresenhamDrawInfo : DebugInfo
    {
        public required int Iteration { get; set; }
        public required double E { get; set; }
        public required double X { get; set; }
        public required double Y { get; set; }
        public required int DisplayX { get; set; }
        public required int DisplayY { get; set; }
    }

    public class Bresenham : ILineDrawingAlgorithm
    {
        public IDrawingParameters EmptyParameters => new LineDrawingParameters();
        public string DisplayName => "Брезенхем";

        public IEnumerable<DrawInfo> Draw(IParameters param)
        {
            if (param is not LineDrawingParameters parameters) yield break;

            var start = parameters.Start.Value;
            var end = parameters.End.Value;
            var color = parameters.Color;

            int dx = Math.Abs(end.X - start.X);
            int dy = Math.Abs(end.Y - start.Y);
            int sx = start.X < end.X ? 1 : -1;
            int sy = start.Y < end.Y ? 1 : -1;
            int err = dx - dy;

            int x = start.X;
            int y = start.Y;

            int i = 0;
            while (true)
            {
                var point = new ColorPoint(new(x, y), color);
                var drawInfo = new BresenhamDrawInfo
                {
                    Iteration = i++,
                    X = x,
                    Y = y,
                    E = err,
                    DisplayX = x,
                    DisplayY = y,
                };
                yield return new()
                {
                    Drawable = point,
                    DebugInfo = drawInfo,
                };

                if (x == end.X && y == end.Y) break;

                int e2 = err * 2;

                if (e2 > -dy)
                {
                    err -= dy;
                    x += sx;
                }

                if (e2 < dx)
                {
                    err += dx;
                    y += sy;
                }
            }
        }
    }
}

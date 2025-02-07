using LW1.Common;

namespace LW1.LineDrawing
{
    public class BresenhamDrawInfo : IDebugInfo
    {
        public required int Iteration { get; set; }
        public required double E { get; set; }
        public required double X { get; set; }
        public required double Y { get; set; }
        public required int DisplayX { get; set; }
        public required int DisplayY { get; set; }
        public IEnumerable<string> Columns => ["i", "e", "x", "y", "(x, y)"];
        public IEnumerable<string> Row => [$"{Iteration}", $"{E:F2}", $"{X:F2}", $"{Y:F2}", $"{DisplayX}, {DisplayY}"];
    }

    public class Bresenham : ILineDrawingAlgorithm
    {
        public string DisplayName => "Брезенхем";

        public IEnumerable<(ColorPoint point, IDebugInfo info)> Draw(LineDrawingParameters parameters)
        {
            var start = parameters.Start;
            var end = parameters.End;
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
                yield return (point, drawInfo);

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

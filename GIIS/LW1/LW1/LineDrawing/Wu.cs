using LW1.Common;
using LW1.LineDrawing.Common;

namespace LW1.LineDrawing
{
    public class WuDrawInfo : IDebugInfo
    {
        public required int Iteration { get; set; }
        public required double X { get; set; }
        public required double Y { get; set; }
        public required double V { get; set; }
        public required int DisplayX { get; set; }
        public required int DisplayY { get; set; }
        public IEnumerable<string> Columns => ["i", "x", "y", "Value", "(x, y)"];
        public IEnumerable<string> Row => [$"{Iteration}", $"{X:F2}", $"{Y:F2}", $"{V:F2}", $"{DisplayX}, {DisplayY}"];
    }

    public class Wu : ILineDrawingAlgorithm
    {
        public string DisplayName => "Ву";

        public IDrawingParameters EmptyParameters => new LineDrawingParameters();

        private static float FPart(float x) => x - (float)Math.Floor(x);

        public IEnumerable<(ColorPoint point, IDebugInfo info)> Draw(IDrawingParameters param)
        {
            if (param is not LineDrawingParameters parameters) yield break;

            var start = parameters.Start.Value;
            var end = parameters.End.Value;
            var color = parameters.Color;

            // Fallback to CDA
            if (start.X == end.X || start.Y == end.Y)
            {
                var cda = new CDA();
                foreach (var pair in cda.Draw(parameters))
                {
                    yield return pair;
                }
                yield break;
            }

            bool steep = Math.Abs(end.Y - start.Y) > Math.Abs(end.X - start.X);

            // Если линия крутая, меняем координаты местами
            if (steep)
            {
                start = new Point(start.Y, start.X);
                end = new Point(end.Y, end.X);
            }

            bool reverseX = start.X > end.X;
            if (reverseX)
            {
                (start.X, end.X) = (end.X, start.X);
                (start.Y, end.Y) = (end.Y, start.Y);
            }
            int dx = end.X - start.X;
            int dy = end.Y - start.Y;
            float gradient = (float)dy / dx;

            float xEnd = (float)Math.Round((double)start.X);
            float yEnd = start.Y + gradient * (xEnd - start.X);
            float xGap = 1 - FPart(start.X + 0.5f);

            int i = 0;
            while (true)
            {
                var x = steep ? (int)yEnd : (int)xEnd;
                var y = steep ? (int)xEnd : (int)yEnd;
                var fpart = FPart(yEnd);

                var (upperX, upperY) = (x, y);
                var (lowerX, lowerY) = (steep ? x + 1 : x, steep ? y : y + 1);

                var upper = new ColorPoint(new(upperX, upperY),
                    Color.FromArgb((int)((1 - fpart) * 255), color));
                var lower = new ColorPoint(new(lowerX, lowerY),
                    Color.FromArgb((int)(fpart * 255), color));

                yield return (
                    lower,
                    new WuDrawInfo
                    {
                        Iteration = i,
                        X = steep ? yEnd : xEnd,
                        Y = steep ? xEnd : yEnd,
                        DisplayX = lowerX,
                        DisplayY = lowerY,
                        V = fpart,
                    });
                yield return (
                    upper,
                    new WuDrawInfo
                    {
                        Iteration = i++,
                        X = steep ? yEnd : xEnd,
                        Y = steep ? xEnd : yEnd,
                        DisplayX = upperX,
                        DisplayY = upperY,
                        V = 1 - fpart,
                    });

                if (xEnd >= end.X)
                    break;

                xEnd += 1;
                yEnd += gradient;
                xGap = 1 - xGap;
            }
        }
    }
}

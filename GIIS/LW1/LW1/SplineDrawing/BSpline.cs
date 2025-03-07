using LW1.Common.Algorithms;
using LW1.Common.Parameters;
using LW1.Common.Shapes;
using LW1.LineDrawing;
using LW1.SplineDrawing.Common;

namespace LW1.SplineDrawing
{
    public class BSplineParameters : IDrawingParameters
    {
        public Parameter<Color> Color { get; init; } = new() { DisplayName = "Цвет", Value = System.Drawing.Color.Black };
        public Parameter<Point> P1 { get; init; } = new() { DisplayName = "P1", Value = new(0, 0) };
        public Parameter<Point> P2 { get; init; } = new() { DisplayName = "P2", Value = new(0, 15) };
        public Parameter<Point> P3 { get; init; } = new() { DisplayName = "P3", Value = new(31, 5) };
        public Parameter<Point> P4 { get; init; } = new() { DisplayName = "P4", Value = new(31, 31) };
        public Parameter<int> Iterations { get; init; } = new() { DisplayName = "Разрешение", Value = 20 };
    }

    public class BSpline : ISplineDrawingAlgorithm
    {
        public string DisplayName => "B-Сплайн";

        public IDrawingParameters EmptyParameters => new BSplineParameters();

        public IEnumerable<DrawInfo> Draw(IParameters param)
        {
            if (param is not BSplineParameters parameters) yield break;

            List<Point> controlPoints = [parameters.P1, parameters.P2, parameters.P3, parameters.P4];
            var n = controlPoints.Count - 1;
            var k = 3;

            var knotVector = CreateKnotVector(n, k);

            for (var i = 0; i < parameters.Iterations + 1; i++)
            {
                var t = i / (double)parameters.Iterations.Value;
                double x = 0;
                double y = 0;

                for (int j = 0; j < n + 1; j++)
                {
                    var N = BasisFunction(j, k, t, knotVector);
                    x += N * controlPoints[j].X;
                    y += N * controlPoints[j].Y;
                }

                var X = (int)Math.Round(x);
                var Y = (int)Math.Round(y);

                Point point = new(X, Y);
                SplineDebugInfo info = new()
                {
                    T = t,
                    X_T = X,
                    Y_T = Y,
                };
                yield return new()
                {
                    Drawable = new ColorPoint(point, parameters.Color),
                    DebugInfo = info,
                };
            }
        }

        private static double BasisFunction(int i, int k, double t, int[] knotVector)
        {
            if (k == 0)
            {
                return knotVector[i] <= t && t < knotVector[i + 1] ? 1 : 0;
            }

            double left = 0;
            double right = 0;

            if (knotVector[i + k] - knotVector[i] != 0)
            {
                left = ((t - knotVector[i]) / (knotVector[i + k] - knotVector[i])) * BasisFunction(i, k - 1, t, knotVector);
            }

            if (i + k + 1 < knotVector.Length && knotVector[i + k + 1] - knotVector[i + 1] != 0)
            {
                right = ((knotVector[i + k + 1] - t) / (knotVector[i + k + 1] - knotVector[i + 1])) * BasisFunction(i + 1, k - 1, t, knotVector);
            }

            return left + right;
        }

        private static int[] CreateKnotVector(int n, int k)
        {
            var m = n + k + 2;

            var first = new double[k].Select(i => 0);
            var second = Enumerable.Range(0, m - 2 * k);
            var third = new double[k].Select(i => m - 2 * k - 1);

            return first.Concat(second).Concat(third).ToArray();
        }
    }
}

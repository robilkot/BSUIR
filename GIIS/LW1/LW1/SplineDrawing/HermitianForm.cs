using LW1.Common.Algorithms;
using LW1.Common.Parameters;
using LW1.Common.Shapes;
using LW1.SplineDrawing.Common;
using MathNet.Numerics.LinearAlgebra.Complex;
using System.Numerics;

namespace LW1.SplineDrawing
{
    public class HermitianFormParameters : IDrawingParameters
    {
        public Parameter<Color> Color { get; init; } = new() { DisplayName = "Цвет", Value = System.Drawing.Color.Black };
        public Parameter<Point> P1 { get; init; } = new() { DisplayName = "P1", Value = new(0, 0) };
        public Parameter<Point> P4 { get; init; } = new() { DisplayName = "P4", Value = new(31, 31) };
        public Parameter<Point> R1 { get; init; } = new() { DisplayName = "R1", Value = new(31, 0) };
        public Parameter<Point> R4 { get; init; } = new() { DisplayName = "R4", Value = new(0, 15) };
        public Parameter<int> Iterations { get; init; } = new() { DisplayName = "Разрешение", Value = 20 };
    }

    public class HermitianForm : ISplineDrawingAlgorithm
    {
        public string DisplayName => "Форма Эрмита";

        public IDrawingParameters EmptyParameters => new HermitianFormParameters();

        public IEnumerable<DrawInfo> Draw(IParameters param)
        {
            if (param is not HermitianFormParameters parameters) yield break;

            for (var i = 0; i < parameters.Iterations + 1; i++)
            {
                var t = i / (double)parameters.Iterations.Value;

                var mtx = DenseMatrix.OfArray(new Complex[,] {
                    { parameters.P1.Value.X, parameters.P1.Value.Y },
                    { parameters.P4.Value.X, parameters.P4.Value.Y },
                    { parameters.R1.Value.X, parameters.R1.Value.Y },
                    { parameters.R4.Value.X, parameters.R4.Value.Y },
                });

                var default_mtx = DenseMatrix.OfArray(new Complex[,] {
                    { 2, -2, 1, 1 },
                    { -3, 3, -2, -1 },
                    { 0, 0, 1, 0 },
                    { 1, 0, 0, 0 },
                });

                var temp_mtx = default_mtx.Multiply(mtx);
                var t_mtx = DenseMatrix.OfArray(new Complex[,] {
                    { Math.Pow(t, 3), Math.Pow(t, 2), t, 1 }
                }).Multiply(temp_mtx);

                var X = (int)Math.Round(t_mtx[0, 0].Real);
                var Y = (int)Math.Round(t_mtx[0, 1].Real);

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
    }
}

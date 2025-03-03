using LW1.Common;
using LW1.LineDrawing;
using LW1.LineDrawing.Common;
using LW1.SplineDrawing.Common;
using MathNet.Numerics.LinearAlgebra.Complex;
using System.Numerics;

namespace LW1.SplineDrawing
{
    public class BezierCurveParameters : IDrawingParameters
    {
        public Parameter<Color> Color { get; init; } = new() { DisplayName = "Цвет", Value = System.Drawing.Color.Black };
        public Parameter<Point> P1 { get; init; } = new() { DisplayName = "P1", Value = new(0, 0) };
        public Parameter<Point> P2 { get; init; } = new() { DisplayName = "P2", Value = new(0, 15) };
        public Parameter<Point> P3 { get; init; } = new() { DisplayName = "P3", Value = new(31, 5) };
        public Parameter<Point> P4 { get; init; } = new() { DisplayName = "P4", Value = new(31, 31) };
        public Parameter<int> Iterations { get; init; } = new() { DisplayName = "Разрешение", Value = 10 };
    }

    public class BezierCurve : ISplineDrawingAlgorithm
    {
        public string DisplayName => "Кривая Безье";

        public IDrawingParameters EmptyParameters => new BezierCurveParameters();

        public IEnumerable<(ColorPoint point, DebugInfo info)> Draw(IDrawingParameters param)
        {
            if (param is not BezierCurveParameters parameters) yield break;

            var cda = new Wu();
            Point? previousPoint = null;

            for (var i = 0; i < parameters.Iterations + 1; i++)
            {
                var t = i / (double)parameters.Iterations.Value;

                var mtx = DenseMatrix.OfArray(new Complex[,] {
                    { parameters.P1.Value.X, parameters.P1.Value.Y },
                    { parameters.P2.Value.X, parameters.P2.Value.Y },
                    { parameters.P3.Value.X, parameters.P3.Value.Y },
                    { parameters.P4.Value.X, parameters.P4.Value.Y },
                });

                var default_mtx = DenseMatrix.OfArray(new Complex[,] {
                    { -1, 3, -3, 1 },
                    { 3, -6, 3, 0 },
                    { -3, 3, 0, 0 },
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
                yield return new(new(point, param.Color), info);
                
                if(previousPoint is not null)
                {
                    var lineParams = new LineDrawingParameters()
                    {
                        Color = parameters.Color,
                        Start = previousPoint!,
                        End = point,
                    };

                    foreach(var linePoint in cda.Draw(lineParams))
                    {
                        yield return linePoint;
                    }
                }

                previousPoint = point;
            }
        }
    }
}

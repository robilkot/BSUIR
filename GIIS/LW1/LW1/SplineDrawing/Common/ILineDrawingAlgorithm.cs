using LW1.LineDrawing;

namespace LW1.SplineDrawing.Common
{
    public interface ISplineDrawingAlgorithm : IDrawingAlgorithm
    {
        new string DisplayName { get; }
    }
}
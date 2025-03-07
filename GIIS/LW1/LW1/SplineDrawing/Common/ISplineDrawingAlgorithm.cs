using LW1.Common.Algorithms;

namespace LW1.SplineDrawing.Common
{
    public interface ISplineDrawingAlgorithm : IDrawingAlgorithm
    {
        new string DisplayName { get; }
    }
}
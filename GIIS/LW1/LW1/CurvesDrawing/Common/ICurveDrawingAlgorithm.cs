using LW1.Common.Algorithms;

namespace LW1.CurvesDrawing.Common
{
    public interface ICurveDrawingAlgorithm : IDrawingAlgorithm
    {
        new string DisplayName { get; }
    }
}
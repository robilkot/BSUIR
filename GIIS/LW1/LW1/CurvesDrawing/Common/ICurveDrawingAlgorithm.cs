using LW1.LineDrawing;

namespace LW1.CurvesDrawing.Common
{
    public interface ICurveDrawingAlgorithm : IDrawingAlgorithm
    {
        new string DisplayName { get; }
    }
}
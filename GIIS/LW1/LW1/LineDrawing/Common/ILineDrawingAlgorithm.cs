using LW1.Common;

namespace LW1.LineDrawing.Common
{
    public interface ILineDrawingAlgorithm : IDrawingAlgorithm
    {
        new string DisplayName { get; }
    }
}
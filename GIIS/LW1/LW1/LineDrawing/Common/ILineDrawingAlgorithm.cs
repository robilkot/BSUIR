using LW1.Common;
using LW1.Common.Algorithms;

namespace LW1.LineDrawing.Common
{
    public interface ILineDrawingAlgorithm : IDrawingAlgorithm
    {
        new string DisplayName { get; }
    }
}
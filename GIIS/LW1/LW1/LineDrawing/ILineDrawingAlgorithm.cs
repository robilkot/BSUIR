using LW1.Common;

namespace LW1.LineDrawing
{
    public interface ILineDrawingAlgorithm
    {
        string DisplayName { get; }
        IEnumerable<(ColorPoint point, IDebugInfo info)> DrawLine(Point start, Point end, Color color);
    }
}

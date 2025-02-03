namespace LW1.LineDrawing
{
    public interface ILineDrawingAlgorithm
    {
        string DisplayName { get; }
        IEnumerable<(ColorPoint point, IDrawInfo info)> DrawLine(Point start, Point end, Color color);
    }
}

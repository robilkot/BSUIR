namespace LW1.LineDrawing
{
    public class WuDrawInfo : IDrawInfo
    {
        public string DisplayString => throw new NotImplementedException();

        public IEnumerable<string> Columns => throw new NotImplementedException();

        public IEnumerable<string> Row => throw new NotImplementedException();
    }

    public class Wu : ILineDrawingAlgorithm
    {
        public string DisplayName => "Ву";

        public IEnumerable<(ColorPoint, IDrawInfo)> DrawLine(Point start, Point end, Color color)
        {
            throw new NotImplementedException();
        }
    }
}

using LW1.Common;

namespace LW1.LineDrawing.Common
{
    public class LineDrawingParameters : IDrawingParameters
    {
        public Point Start { get; set; }
        public Point End { get; set; }
        public Color Color { get; set; }
    }
}

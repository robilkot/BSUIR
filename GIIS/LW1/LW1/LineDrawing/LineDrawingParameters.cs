using LW1.Common;

namespace LW1.LineDrawing
{
    public record LineDrawingParameters(Point Start, Point End, Color Color) : IDrawingParameters;
}

using LW1.Common;

namespace LW1.LineDrawing
{
    public interface IDrawingAlgorithm : INamed
    {
        IDrawingParameters EmptyParameters { get; }
        string DisplayName { get; }
        IEnumerable<(ColorPoint point, IDebugInfo info)> Draw<T>(T parameters) where T : IDrawingParameters;
    }
}

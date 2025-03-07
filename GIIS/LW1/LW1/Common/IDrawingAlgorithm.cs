using LW1.Common;

namespace LW1.LineDrawing
{
    public interface IDrawingAlgorithm : INamed
    {
        IDrawingParameters EmptyParameters { get; }
        new string DisplayName { get; }
        IEnumerable<DrawInfo> Draw(IParameters parameters);
    }
}

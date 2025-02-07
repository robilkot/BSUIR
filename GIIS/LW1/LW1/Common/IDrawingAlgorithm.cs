using LW1.Common;

namespace LW1.LineDrawing
{
    public interface IDrawingAlgorithm : INamed
    {
        public string DisplayName { get; }
    }
    public interface IDrawingAlgorithm<T>: IDrawingAlgorithm  where T : IDrawingParameters
    {
        IEnumerable<(ColorPoint point, IDebugInfo info)> Draw(T parameters);
    }
}

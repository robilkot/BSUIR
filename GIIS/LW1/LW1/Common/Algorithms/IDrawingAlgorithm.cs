using LW1.Common.Parameters;

namespace LW1.Common.Algorithms
{
    public interface IDrawingAlgorithm : INamed
    {
        IDrawingParameters EmptyParameters { get; }
        new string DisplayName { get; }
        IEnumerable<DrawInfo> Draw(IParameters parameters);
    }
}

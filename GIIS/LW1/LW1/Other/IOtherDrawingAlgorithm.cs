using LW1.Common.Algorithms;

namespace LW1.Other
{
    public interface IOtherDrawingAlgorithm : IDrawingAlgorithm
    {
        new string DisplayName { get; }
    }
}
using LW1.Common.Algorithms;

namespace LW1.Polygons.Common
{
    public interface IPolygonDrawingAlgorithm : IDrawingAlgorithm
    {
        new string DisplayName { get; }
    }
}

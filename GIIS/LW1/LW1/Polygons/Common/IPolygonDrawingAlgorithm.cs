using LW1.LineDrawing;

namespace LW1.Polygons.Common
{
    public interface IPolygonDrawingAlgorithm : IDrawingAlgorithm
    {
        new string DisplayName { get; }
    }
}

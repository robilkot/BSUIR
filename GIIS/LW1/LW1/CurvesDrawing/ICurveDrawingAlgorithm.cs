namespace LW1.LineDrawing
{
    public interface ICurveDrawingAlgorithm<T> : IDrawingAlgorithm<T> where T : CurveDrawingParameters;
}
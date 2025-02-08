using LW1.LineDrawing;

namespace LW1.CurvesDrawing.Circle
{
    public class CircleDrawingParameters : CurveDrawingParameters
    {
        public override Color Color { get; set; }
        public int CenterX { get; set; }
        public int CenterY { get; set; }
        public int Radius { get; set; }
    }
}

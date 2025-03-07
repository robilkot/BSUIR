using LW1.Common.Algorithms;

namespace LW1.SplineDrawing.Common
{
    public class SplineDebugInfo : DebugInfo
    {
        public required double T { get; set; }
        public required int X_T { get; set; }
        public required int Y_T { get; set; }
    }
}
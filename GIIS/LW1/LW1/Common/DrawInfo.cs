using LW1.Common.Shapes;

namespace LW1.Common
{
    public class DrawInfo
    {
        public required IDrawable Drawable { get; set; }
        public DebugInfo? DebugInfo { get; set; } = null;
    }
}

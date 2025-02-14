namespace LW1.View
{
    public partial class Canvas : PictureBox
    {
        public int PixelSize = 8;
        public int CanvasWidth = 64;
        public int CanvasHeight = 64;

        public Canvas()
        {
            InitializeComponent();
        }
        public void DrawPoint(Graphics g, Point point, Color color)
        {
            using var brush = new SolidBrush(color);
                
            g.FillRectangle(brush, point.X * PixelSize, point.Y * PixelSize, PixelSize, PixelSize);

            Invalidate();
        }
    }
}

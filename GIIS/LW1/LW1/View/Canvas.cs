using LW1.Common.Shapes;

namespace LW1.View
{
    public partial class Canvas : PictureBox
    {
        public record CanvasConfig(int PixelSize, Size CanvasSize);

        public delegate void CanvasConfigChangeHandler(CanvasConfig value);
        public event CanvasConfigChangeHandler? CanvasConfigChanged;

        private Graphics _graphics;
        private CanvasConfig _config = new(2, new Size(256, 256));
        public CanvasConfig Config
        {
            get => _config;
            set 
            {
                if (_config != value 
                    && value.PixelSize > 0
                    && value.CanvasSize.Width > 0
                    && value.CanvasSize.Height > 0)
                {
                    _config = value;
                    CanvasConfigChanged?.Invoke(value);
                }
            }
        }
        private Size ActualSize => _config.CanvasSize * _config.PixelSize;

        public Canvas()
        {
            InitializeComponent();
            CanvasConfigChanged += (config) => ResizeCanvas();
        }
        
        private void ResizeCanvas()
        {
            Size = ActualSize;

            Center();
            Clear();
        }
        
        private void Center()
        {
            Left = (Parent?.Size.Width ?? 0) / 2 - Width / 2;
            Top = (Parent?.Size.Height ?? 0) / 2 - Height / 2;
        }

        protected override void OnSizeChanged(EventArgs e)
        {
            base.OnSizeChanged(e);

            ResizeCanvas();
        }

        public void Clear()
        {
            Image = new Bitmap(ActualSize.Width, ActualSize.Height);
        }

        public void BeginDraw()
        {
            _graphics = Graphics.FromImage(Image);
        }
        public void EndDraw()
        {
            Invalidate();
        }
        public void Draw(IDrawable drawable, bool immediatlyUpdate)
        {
            using var brush = new SolidBrush(drawable.Color);

            if (drawable is not ColorPoint point)
                return; // todo extend

            _graphics.FillRectangle(brush, point.Coordinates.X * _config.PixelSize, point.Coordinates.Y * _config.PixelSize, _config.PixelSize, _config.PixelSize);

            if(immediatlyUpdate)
            {
                Invalidate();
            }
        }
    }
}

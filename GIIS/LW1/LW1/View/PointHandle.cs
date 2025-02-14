using LW1.Common;

namespace LW1.View
{
    public partial class PointHandle : UserControl
    {
        private static readonly Size s_size = new(20, 20);
        private static readonly RectangleF s_shapeRectangle = new(new(0, 0), new(s_size.Width - 1, s_size.Height - 1));

        private Canvas? _canvas;
        private readonly Label _nameLabel;
        private readonly PictureBox _dot;

        private Parameter<Point>? _point = null;
        public Parameter<Point>? Point
        {
            get
            {
                return _point;
            }
            set
            {
                if (_point is not null)
                {
                    _point.ParameterChanged -= RelocatePoint;
                }

                _point = value;

                if (_point is not null)
                {
                    _nameLabel.Text = _point.DisplayName;
                    _point.ParameterChanged += RelocatePoint;
                }
            }
        }

        private void RelocatePoint(Point value)
        {
            if (_canvas is not null)
            {
                Location = new(
                            Point.Value.X * _canvas.PixelSize - s_size.Width / 2,
                            Point.Value.Y * _canvas.PixelSize - s_size.Height / 2
                            );
            }
        }

        protected override void OnParentChanged(EventArgs e)
        {
            _canvas = Parent as Canvas;
            RelocatePoint(Point);
        }
        public PointHandle()
        {
            InitializeComponent();

            AutoSize = true;
            AutoSizeMode = AutoSizeMode.GrowAndShrink;

            _nameLabel = new Label
            {
                AutoSize = true,
                TextAlign = System.Drawing.ContentAlignment.MiddleLeft,
            };

            _dot = new PictureBox
            {
                AutoSize = true,
                Size = s_size,
            };

            _dot.Paint += (sender, e) =>
            {
                using var brush = new Pen(Color.FromArgb(0, 0, 0), 2);

                e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;
                e.Graphics.DrawEllipse(brush, s_shapeRectangle);
            };

            var panel = new FlowLayoutPanel()
            {
                FlowDirection = FlowDirection.LeftToRight,
                Dock = DockStyle.Fill,
                AutoSize = true,
            };

            panel.Controls.Add(_dot);
            panel.Controls.Add(_nameLabel);

            InitHandlers(_dot);

            Controls.Add(panel);
        }

        private Point _mouseDownLocation;
        private void InitHandlers(PictureBox dot)
        {
            dot.MouseDown += (o, e) =>
            {
                if (e.Button == System.Windows.Forms.MouseButtons.Left)
                {
                    _mouseDownLocation = e.Location;
                }
            };
            dot.MouseMove += (o, e) =>
            {
                if (e.Button == System.Windows.Forms.MouseButtons.Left)
                {
                    int dx = e.X - _mouseDownLocation.X;
                    int dy = e.Y - _mouseDownLocation.Y;

                    int dx_canvas = dx / _canvas.PixelSize;
                    int dy_canvas = dy / _canvas.PixelSize;

                    if (dx_canvas != 0 || dy_canvas != 0)
                    {
                        var new_x = Math.Max(0, Math.Min(Point.Value.X + dx_canvas, _canvas.CanvasWidth - 1));
                        var new_y = Math.Max(0, Math.Min(Point.Value.Y + dy_canvas, _canvas.CanvasHeight - 1));
                        
                        Point.Value = new(new_x, new_y);
                    }
                }
            };
        }
    }
}

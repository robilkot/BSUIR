using LW1.LineDrawing;
using System.Collections.ObjectModel;

namespace LW1
{
    public partial class MainForm : Form
    {
        private CancellationTokenSource _cts = new();
        private static Bitmap _bitmap;
        private static int s_pixelSize = 16;
        private static int s_canvasWidth = 32;
        private static int s_canvasHeight = 32;

        public static List<Color> Colors = [
            Color.Orange,
            Color.DarkGreen,
            Color.Brown,
            Color.Gray,
            Color.Black,
            ];

        public static ObservableCollection<ILineDrawingAlgorithm> LineDrawAlgorithms { get; private set; } = [
            new CDA(),
            new Bresenham(),
            new Wu(),
            ];

        public MainForm()
        {
            InitializeComponent();

            var bindingSource = new BindingSource
            {
                DataSource = LineDrawAlgorithms
            };
            InitCanvas();

            DrawLineMethodCombobox.DataSource = bindingSource.DataSource;
            DrawLineMethodCombobox.DisplayMember = nameof(ILineDrawingAlgorithm.DisplayName);
            DrawLineMethodCombobox.ValueMember = nameof(ILineDrawingAlgorithm.DisplayName);

            DrawLineMethodCombobox.SelectedIndex = 1;
        }

        private void CancelCurrentTask()
        {
            _cts.Cancel();
            _cts.Dispose();
            _cts = new();
        }
        private async void DrawLineButton_Click(object sender, EventArgs e)
        {
            CancelCurrentTask();

            Point start = new((int)EntryX1.Value, (int)EntryY1.Value);
            Point end = new((int)EntryX2.Value, (int)EntryY2.Value);

            if (start == end)
            {
                MessageBox.Show("Координаты начала и конца совпадают. Измените их.");
                return;
            }

            ILineDrawingAlgorithm algorithm = (ILineDrawingAlgorithm)DrawLineMethodCombobox.SelectedItem!;

            using var g = Graphics.FromImage(_bitmap);
            var color = Colors.Random();
            var brush = new SolidBrush(color);

            ClearDebugTable();

            try
            {
                await Task.Run(async () =>
                {
                    foreach (var (point, info) in algorithm.DrawLine(start, end, color))
                    {
                        DrawPoint(g, point.Coordinates, brush);

                        if (EnableDebugButton.Checked)
                        {
                            if (DebugGridView.Columns.Count == 0)
                            {
                                InitDebugTable(info);
                            }

                            AddDebugSteps(info);
                            CanvasPictureBox.Image = _bitmap;
                            await Task.Delay(50, _cts.Token);
                        }

                        if(_cts.IsCancellationRequested)
                        {
                            return;
                        }
                    }
                }, _cts.Token);
            }
            catch(TaskCanceledException ex)
            {
            }

            CanvasPictureBox.Image = _bitmap;
        }
        private void DrawPoint(Graphics g, Point point, Brush brush)
        {
            g.FillRectangle(brush, point.X * s_pixelSize, point.Y * s_pixelSize, s_pixelSize, s_pixelSize);
        }
        private void InitCanvas()
        {
            var width = s_canvasWidth * s_pixelSize;
            var height = s_canvasHeight * s_pixelSize;

            CanvasPictureBox.Width = width;
            CanvasPictureBox.Height = height;

            CanvasPictureBox.Left = (CanvasPictureBox.Parent?.Size.Width ?? 0) / 2 - width / 2;
            CanvasPictureBox.Top = (CanvasPictureBox.Parent?.Size.Height ?? 0) / 2 - height / 2;

            _bitmap = new Bitmap(width, height);
            CanvasPictureBox.Image = _bitmap;
        }

        private void InitDebugTable(IDrawInfo info)
        {
            DebugGridView.Invoke(() =>
            {
                DebugGridView.Columns.Clear();
                foreach(var column in info.Columns)
                {
                    DebugGridView.Columns.Add(new() { HeaderText = column,
                    CellTemplate = new DataGridViewTextBoxCell(),
                    Width = 60});
                }
            });
        }
        private void AddDebugSteps(IDrawInfo drawInfo)
        {
            DebugGridView.Invoke(() =>
            {
                DebugGridView.Rows.Add(drawInfo.Row.ToArray());
            });
        }

        private void ClearDebugTable()
        {
            DebugGridView.Invoke(() =>
            {
                DebugGridView.Rows.Clear();
                DebugGridView.Columns.Clear();
            });
        }

        private void ClearAll_Click(object sender, EventArgs e)
        {
            CancelCurrentTask();
            ClearDebugTable();
            InitCanvas();
        }

        private void DebugListView_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
    }
}

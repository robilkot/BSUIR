using LW1.Common;
using LW1.CurvesDrawing;
using LW1.CurvesDrawing.Common;
using LW1.LineDrawing;
using LW1.LineDrawing.Common;
using System.Collections.Immutable;

namespace LW1
{
    public partial class MainForm : Form
    {
        private CancellationTokenSource _cts = new();
        private IDrawingParameters _parameters;
        private Dictionary<string, NumericUpDown> _numericParametersMapping = [];
        private static Bitmap _bitmap;
        private static int s_pixelSize = 16;
        private static int s_canvasWidth = 32;
        private static int s_canvasHeight = 32;

        public static ImmutableArray<Color> Colors { get; private set; } = [
            Color.Orange,
            Color.DarkGreen,
            Color.Brown,
            Color.Gray,
            Color.Black,
            ];

        public static ImmutableArray<IDrawingAlgorithm> LineDrawingAlgorithms { get; private set; } = [
            new CDA(),
            new Bresenham(),
            new Wu(),
            ];

        public static ImmutableArray<IDrawingAlgorithm> CurveDrawingAlgorithms { get; private set; } = [
            new CircleDrawingAlgorithm(),
            new EllipseDrawingAlgorithm(),
            new ParabolaDrawingAlgorithm(),
            new HyperbolaDrawingAlgorithm(),
            ];

        public MainForm()
        {
            InitializeComponent();

            InitCanvas();

            var lineBindingSource = new BindingSource()
            {
                DataSource = LineDrawingAlgorithms
            };
            LineDrawingMethodCombobox.DataSource = lineBindingSource.DataSource;
            LineDrawingMethodCombobox.DisplayMember = nameof(IDrawingAlgorithm.DisplayName);
            LineDrawingMethodCombobox.ValueMember = nameof(IDrawingAlgorithm.DisplayName);

            var curveBindingSource = new BindingSource()
            {
                DataSource = CurveDrawingAlgorithms
            };
            CurveTypeCombobox.DataSource = curveBindingSource.DataSource;
            CurveTypeCombobox.DisplayMember = nameof(IDrawingAlgorithm.DisplayName);
            CurveTypeCombobox.ValueMember = nameof(IDrawingAlgorithm.DisplayName);
        }

        private async Task Draw(IDrawingAlgorithm algorithm, IDrawingParameters parameters)
        {
            CancelCurrentTask();
            ClearDebugTable();

            using var g = Graphics.FromImage(_bitmap);

            try
            {
                await Task.Run(async () =>
                {
                    foreach (var (point, info) in algorithm.Draw(parameters))
                    {
                        DrawPoint(g, point.Coordinates, point.Color);

                        if (EnableDebugButton.Checked)
                        {
                            AddDebugSteps(info);
                            CanvasPictureBox.Image = _bitmap;
                            await Task.Delay(150, _cts.Token);
                        }

                        if (_cts.IsCancellationRequested)
                        {
                            return;
                        }
                    }
                }, _cts.Token);
            }
            catch (TaskCanceledException)
            {
            }

            CanvasPictureBox.Image = _bitmap;
        }
        private static void DrawPoint(Graphics g, Point point, Color color)
        {
            using var brush = new SolidBrush(color);
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
        private void InitDebugTable(IDebugInfo info)
        {
            DebugGridView.Invoke(() =>
            {
                DebugGridView.Columns.Clear();
                foreach (var column in info.Columns)
                {
                    DebugGridView.Columns.Add(new()
                    {
                        HeaderText = column,
                        CellTemplate = new DataGridViewTextBoxCell(),
                        Width = 60
                    });
                }
            });
        }
        private void AddDebugSteps(IDebugInfo drawInfo)
        {
            if (DebugGridView.Columns.Count == 0)
            {
                InitDebugTable(drawInfo);
            }

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
        private void CancelCurrentTask()
        {
            _cts.Cancel();
            _cts.Dispose();
            _cts = new();
        }

        private void CurveTypeCombobox_SelectedIndexChanged(object sender, EventArgs e)
        {
            IDrawingAlgorithm algorithm = (IDrawingAlgorithm)CurveTypeCombobox.SelectedItem!;

            _parameters = algorithm.EmptyParameters;
            var properties = _parameters.GetType().IntParameters();

            _numericParametersMapping.Clear();
            CurveParametersPanel.Controls.Clear();

            foreach (var parameter in properties)
            {
                CurveParametersPanel.Controls.Add(new Label() { Text = parameter });

                var textbox = new NumericUpDown() { };

                CurveParametersPanel.Controls.Add(textbox);

                _numericParametersMapping.Add(parameter, textbox);
            }
        }
        private async void DrawLineButton_ClickAsync(object sender, EventArgs e)
        {
            ILineDrawingAlgorithm algorithm = (ILineDrawingAlgorithm)LineDrawingMethodCombobox.SelectedItem!;
            IDrawingParameters parameters = new LineDrawingParameters()
            {
                Start = new((int)EntryX1.Value, (int)EntryY1.Value),
                End = new((int)EntryX2.Value, (int)EntryY2.Value),
                Color = Colors.Random(),
            };

            await Draw(algorithm, parameters);
        }

        private async void DrawCurveButton_ClickAsync(object sender, EventArgs e)
        {
            // Update params from UI
            foreach (var kvp in _numericParametersMapping)
            {
                int value = (int)kvp.Value.Value;
                _parameters.GetType()!.GetProperty(kvp.Key)!.SetValue(_parameters, value);
            }

            ICurveDrawingAlgorithm algorithm = (ICurveDrawingAlgorithm)CurveTypeCombobox.SelectedItem!;
            IDrawingParameters parameters = _parameters;
            parameters.Color = Colors.Random();

            await Draw(algorithm, parameters);
        }
    }
}

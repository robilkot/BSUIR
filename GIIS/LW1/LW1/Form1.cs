using LW1.Common;
using LW1.CurvesDrawing.Common;
using LW1.LineDrawing;
using LW1.LineDrawing.Common;
using LW1.SplineDrawing.Common;
using LW1.View;

namespace LW1
{
    public partial class MainForm : Form
    {
        private readonly ParametersWrapper _lineParametersWrapper;
        private readonly ParametersWrapper _curveParametersWrapper;
        private readonly ParametersWrapper _splineParametersWrapper;

        private CancellationTokenSource _cts = new();
        private static int s_pixelSize = 8;
        private static int s_canvasWidth = 64;
        private static int s_canvasHeight = 64;

        public MainForm()
        {
            InitializeComponent();

            InstrumentCluster.SelectedIndex = 2;

            _lineParametersWrapper = new(LineParametersLayoutPanel);
            _curveParametersWrapper = new(CurveParametersLayoutPanel);
            _splineParametersWrapper = new(SplineParametersLayoutPanel);

            _lineParametersWrapper.Parameters = new LineDrawingParameters();

            InitCanvas();

            LineDrawingAlgorithmCombobox.DataSource = new List<ILineDrawingAlgorithm>().FilledWithSubtypes();
            LineDrawingAlgorithmCombobox.DisplayMember = nameof(IDrawingAlgorithm.DisplayName);
            LineDrawingAlgorithmCombobox.ValueMember = nameof(IDrawingAlgorithm.DisplayName);

            CurveTypeCombobox.DataSource = new List<ICurveDrawingAlgorithm>().FilledWithSubtypes();
            CurveTypeCombobox.DisplayMember = nameof(IDrawingAlgorithm.DisplayName);
            CurveTypeCombobox.ValueMember = nameof(IDrawingAlgorithm.DisplayName);

            SplineTypeCombobox.DataSource = new List<ISplineDrawingAlgorithm>().FilledWithSubtypes();
            SplineTypeCombobox.DisplayMember = nameof(IDrawingAlgorithm.DisplayName);
            SplineTypeCombobox.ValueMember = nameof(IDrawingAlgorithm.DisplayName);

            SplineTypeCombobox.SelectedIndex = 2;
        }

        private async Task Draw(IDrawingAlgorithm algorithm, IDrawingParameters parameters)
        {
            CancelCurrentTask();
            ClearDebugTable();

            using var g = Graphics.FromImage(CanvasPictureBox.Image);

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
                            CanvasPictureBox.Invalidate();
                            await Task.Delay(75, _cts.Token);
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

            CanvasPictureBox.Invalidate();
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

            CanvasPictureBox.Image = new Bitmap(width, height);

            CanvasPictureBox.Width = width;
            CanvasPictureBox.Height = height;

            CanvasPictureBox.Left = (CanvasPictureBox.Parent?.Size.Width ?? 0) / 2 - width / 2;
            CanvasPictureBox.Top = (CanvasPictureBox.Parent?.Size.Height ?? 0) / 2 - height / 2;

        }
        private void InitDebugTable(DebugInfo info)
        {
            DebugGridView.Invoke(() =>
            {
                DebugGridView.Columns.Clear();
                foreach (var column in info.Keys)
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
        private void AddDebugSteps(DebugInfo drawInfo)
        {
            if (DebugGridView.Columns.Count == 0)
            {
                InitDebugTable(drawInfo);
            }

            DebugGridView.Invoke(() =>
            {
                DebugGridView.Rows.Add(drawInfo.Values.ToArray());
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

            _curveParametersWrapper.Parameters = algorithm.EmptyParameters;
        }

        private async void DrawCurveButton_ClickAsync(object sender, EventArgs e)
        {
            IDrawingAlgorithm algorithm = (IDrawingAlgorithm)CurveTypeCombobox.SelectedItem!;
            IDrawingParameters parameters = _curveParametersWrapper.Parameters;

            await Draw(algorithm, parameters);
        }

        private async void DrawLineButton_Click(object sender, EventArgs e)
        {
            ILineDrawingAlgorithm algorithm = (ILineDrawingAlgorithm)LineDrawingAlgorithmCombobox.SelectedItem!;
            IDrawingParameters parameters = _lineParametersWrapper.Parameters;

            await Draw(algorithm, parameters);
        }

        private void SplineTypeCombobox_SelectedIndexChanged(object sender, EventArgs e)
        {
            IDrawingAlgorithm algorithm = (IDrawingAlgorithm)SplineTypeCombobox.SelectedItem!;

            _splineParametersWrapper.Parameters = algorithm.EmptyParameters;
        }

        private async void DrawSplineButton_Click(object sender, EventArgs e)
        {
            ISplineDrawingAlgorithm algorithm = (ISplineDrawingAlgorithm)SplineTypeCombobox.SelectedItem!;
            IDrawingParameters parameters = _splineParametersWrapper.Parameters;

            await Draw(algorithm, parameters);
        }
    }
}

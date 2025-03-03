using LW1.Common;
using LW1.CurvesDrawing.Common;
using LW1.LineDrawing;
using LW1.LineDrawing.Common;
using LW1.Polygons;
using LW1.Polygons.Common;
using LW1.SplineDrawing.Common;
using LW1.View;
using MathNet.Numerics.LinearAlgebra.Factorization;

namespace LW1
{
    public partial class MainForm : Form
    {
        private readonly ParametersWrapper _lineParametersWrapper;
        private readonly ParametersWrapper _curveParametersWrapper;
        private readonly ParametersWrapper _splineParametersWrapper;

        private readonly ParametersWrapper _polygonParametersWrapper;
        private readonly ParametersWrapper _pointBelongingParametersWrapper;
        private readonly ParametersWrapper _lineIntersectionParametersWrapper;

        private CancellationTokenSource _cts = new();

        public MainForm()
        {
            InitializeComponent();

            _lineParametersWrapper = new(LineParametersLayoutPanel, CanvasPictureBox, InstrumentCluster, 0);
            _curveParametersWrapper = new(CurveParametersLayoutPanel, CanvasPictureBox, InstrumentCluster, 1);
            _splineParametersWrapper = new(SplineParametersLayoutPanel, CanvasPictureBox, InstrumentCluster, 2);

            _polygonParametersWrapper = new(PolygonParametersLayoutPanel, CanvasPictureBox, InstrumentCluster, 3);
            _pointBelongingParametersWrapper = new(PointBelongingLayoutPanel, CanvasPictureBox, InstrumentCluster, 3);
            _lineIntersectionParametersWrapper = new(LineIntersectionLayoutPanel, CanvasPictureBox, InstrumentCluster, 3);

            _lineParametersWrapper.Parameters = new LineDrawingParameters();
            
            var polygonParameters = new PolygonParameters();
            polygonParameters.Color.Value = Color.DarkGreen;
            _polygonParametersWrapper.Parameters = polygonParameters;

            var pointParams = new PointDrawingParameters();
            pointParams.Point.Value = new(37, 30);
            _pointBelongingParametersWrapper.Parameters = pointParams;

            var lineIntersectParam = new LineDrawingParameters();
            lineIntersectParam.Color.Value = Color.LightGray;
            lineIntersectParam.Start.Value = new Point(2, 48);
            lineIntersectParam.End.Value = new Point(53, 46);
            _lineIntersectionParametersWrapper.Parameters = lineIntersectParam;

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

            PolygonAlgorithmCombobox.DataSource = new List<IPolygonDrawingAlgorithm>().FilledWithSubtypes();
            PolygonAlgorithmCombobox.DisplayMember = nameof(IDrawingAlgorithm.DisplayName);
            PolygonAlgorithmCombobox.ValueMember = nameof(IDrawingAlgorithm.DisplayName);
        }

        protected override void OnLoad(EventArgs e)
        {
            InstrumentCluster.SelectedIndex = -1;
            InstrumentCluster.SelectedIndex = 0;
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
                        CanvasPictureBox.DrawPoint(g, point.Coordinates, point.Color);

                        if (EnableDebugButton.Checked)
                        {
                            AddDebugSteps(info);
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
        }

        private void InitCanvas()
        {
            var width = CanvasPictureBox.CanvasWidth * CanvasPictureBox.PixelSize;
            var height = CanvasPictureBox.CanvasHeight * CanvasPictureBox.PixelSize;

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

            await Draw(algorithm, _curveParametersWrapper.Parameters);
        }

        private async void DrawLineButton_Click(object sender, EventArgs e)
        {
            ILineDrawingAlgorithm algorithm = (ILineDrawingAlgorithm)LineDrawingAlgorithmCombobox.SelectedItem!;

            await Draw(algorithm, _lineParametersWrapper.Parameters);
        }

        private void SplineTypeCombobox_SelectedIndexChanged(object sender, EventArgs e)
        {
            IDrawingAlgorithm algorithm = (IDrawingAlgorithm)SplineTypeCombobox.SelectedItem!;

            _splineParametersWrapper.Parameters = algorithm.EmptyParameters;
        }

        private async void DrawSplineButton_Click(object sender, EventArgs e)
        {
            ISplineDrawingAlgorithm algorithm = (ISplineDrawingAlgorithm)SplineTypeCombobox.SelectedItem!;

            await Draw(algorithm, _splineParametersWrapper.Parameters);
        }

        private async void DrawPolygonButton_Click(object sender, EventArgs e)
        {
            IPolygonDrawingAlgorithm algorithm = (IPolygonDrawingAlgorithm)PolygonAlgorithmCombobox.SelectedItem!;

            await Draw(algorithm, _polygonParametersWrapper.Parameters);
        }

        private void CheckConvexButton_Click(object sender, EventArgs e)
        {
            var result = new ConvexCheck().Execute((PolygonParameters)_polygonParametersWrapper.Parameters);

            string text = result ? "Полигон выпуклый" : "Полигон не выпуклый";

            MessageBox.Show(text, "Результат проверки");
        }

        private async void IntersectLineButton_Click(object sender, EventArgs e)
        {
            var lineAlgorithm = new CDA();
            LineDrawingParameters lineParams = (LineDrawingParameters)_lineIntersectionParametersWrapper.Parameters;
            PolygonParameters polyParams = (PolygonParameters)_polygonParametersWrapper.Parameters;

            await Draw(lineAlgorithm, lineParams);

            var points = new IntersectionCheck().Execute((polyParams, lineParams));

            var crossAlgorithm = new CrossDrawingAlgorithm();

            foreach (var point in points)
            {
                var crossParams = new PointDrawingParameters()
                {
                    Point = point,
                    Color = Color.OrangeRed
                };

                await Draw(crossAlgorithm, crossParams);
            }
        }

        private async void CheckBelongingButton_Click(object sender, EventArgs e)
        {
            var polygonParam = (PolygonParameters)_polygonParametersWrapper.Parameters;
            var pointParam = (PointDrawingParameters)_pointBelongingParametersWrapper.Parameters;
            var pointAlgorithm = new PointDrawingAlgorithm();

            await Draw(pointAlgorithm, pointParam);

            var result = new BelongingCheck().Execute((polygonParam, pointParam));

            string text = result ? "Точка принадлежит полигону" : "Точка не принадлежит полигону";

            MessageBox.Show(text, "Результат проверки");
        }

        private async void DrawPolygonNormalsButton_Click(object sender, EventArgs e)
        {
            var normalsDrawingAlgorithm = new PolygonNormalsDrawingAlgorithm();

            await Draw(normalsDrawingAlgorithm, _polygonParametersWrapper.Parameters);
        }
    }
}

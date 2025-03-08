using LW1.Common;
using LW1.Common.Algorithms;
using LW1.Common.Parameters;
using LW1.CurvesDrawing.Common;
using LW1.LineDrawing;
using LW1.LineDrawing.Common;
using LW1.Other;
using LW1.Polygons;
using LW1.Polygons.Algorithms;
using LW1.Polygons.Common;
using LW1.SplineDrawing.Common;
using LW1.View;

namespace LW1
{
    public partial class MainForm : Form
    {
        private readonly Dictionary<TabPage, int> _tabsHeight;

        private readonly ParametersWrapper _appParametersWrapper;

        private readonly ParametersWrapper _lineParametersWrapper;
        private readonly ParametersWrapper _curveParametersWrapper;
        private readonly ParametersWrapper _splineParametersWrapper;

        private readonly ParametersWrapper _polygonParametersWrapper;
        private readonly ParametersWrapper _pointBelongingParametersWrapper;
        private readonly ParametersWrapper _lineIntersectionParametersWrapper;
        
        private readonly ParametersWrapper _otherParametersWrapper;

        private CancellationTokenSource _cts = new();

        public MainForm()
        {
            InitializeComponent();

            _tabsHeight = new()
            {
                { CommonTab, 200 },
                { LinesTab, 200},
                { SecondDegreeCurvesTab, 200},
                { SplinesTab, 200},
                { PolygonsTab, 300},
                { OtherAlgorithmsTab, 300},
            };

            var appParameters = new ApplicationParameters();
            appParameters.CanvasSize.ParameterChanged += (size) =>
            {
                CanvasPictureBox.Config = CanvasPictureBox.Config with { CanvasSize = size };
                WorkSpaceSplitContainer.Panel1.AutoScrollMinSize = CanvasPictureBox.Size + new Size(25, 25);
            };
            appParameters.CanvasPixelSize.ParameterChanged += (size) =>
            {
                CanvasPictureBox.Config = CanvasPictureBox.Config with { PixelSize = size };
                WorkSpaceSplitContainer.Panel1.AutoScrollMinSize = CanvasPictureBox.Size + new Size(25, 25);
            };

            _appParametersWrapper = new(CommonParametersLayoutPanel, CanvasPictureBox, CommonTab)
            {
                Parameters = appParameters
            };

            _lineParametersWrapper = new(LineParametersLayoutPanel, CanvasPictureBox, LinesTab)
            {
                Parameters = new LineDrawingParameters()
            };
            _curveParametersWrapper = new(CurveParametersLayoutPanel, CanvasPictureBox, SecondDegreeCurvesTab);
            _splineParametersWrapper = new(SplineParametersLayoutPanel, CanvasPictureBox, SplinesTab);

            _polygonParametersWrapper = new(PolygonParametersLayoutPanel, CanvasPictureBox, PolygonsTab);
            _pointBelongingParametersWrapper = new(PointBelongingLayoutPanel, CanvasPictureBox, PolygonsTab);
            _lineIntersectionParametersWrapper = new(LineIntersectionLayoutPanel, CanvasPictureBox, PolygonsTab);

            _otherParametersWrapper = new(OtherParametersPanel, CanvasPictureBox, OtherAlgorithmsTab);

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


            InstrumentCluster.Selected += (object? sender, TabControlEventArgs e) =>
            {
                FormSplitContainer.SplitterDistance = _tabsHeight[e.TabPage!];
            };
            InstrumentCluster.Deselected += (object? sender, TabControlEventArgs e) =>
            {
                _tabsHeight[e.TabPage!] = FormSplitContainer.SplitterDistance;
            };
            FormSplitContainer.SplitterDistance = _tabsHeight[InstrumentCluster.SelectedTab!];

            LineDrawingAlgorithmCombobox.InitWithSubtypes<ILineDrawingAlgorithm>();
            CurveTypeCombobox.InitWithSubtypes<ICurveDrawingAlgorithm>();
            SplineTypeCombobox.InitWithSubtypes<ISplineDrawingAlgorithm>();
            PolygonAlgorithmCombobox.InitWithSubtypes<IPolygonDrawingAlgorithm>();
            OtherAlgorithmCombobox.InitWithSubtypes<IOtherDrawingAlgorithm>();
        }

        private async Task Draw(IDrawingAlgorithm algorithm, IParameters parameters)
        {
            CancelCurrentTask();
            ClearDebugTable();

            CanvasPictureBox.BeginDraw();

            try
            {
                foreach (var step in algorithm.Draw(parameters))
                {
                    CanvasPictureBox.Draw(step.Drawable, EnableDebugButton.Checked);

                    if (EnableDebugButton.Checked && step.DebugInfo is not null)
                    {
                        AddDebugSteps(step.DebugInfo);
                        await Task.Delay(75, _cts.Token);
                    }
                }
            }
            catch (TaskCanceledException)
            {
            }

            CanvasPictureBox.EndDraw();
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

            if (!drawInfo.Values.Any())
            {
                return;
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
            CanvasPictureBox.Clear();
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

            var result = new BelongingCheck().Execute((polygonParam, pointParam.Point));

            string text = result ? "Точка принадлежит полигону" : "Точка не принадлежит полигону";

            MessageBox.Show(text, "Результат проверки");
        }

        private async void DrawPolygonNormalsButton_Click(object sender, EventArgs e)
        {
            var normalsDrawingAlgorithm = new PolygonNormalsDrawingAlgorithm();

            await Draw(normalsDrawingAlgorithm, _polygonParametersWrapper.Parameters);
        }

        private async void DrawOtherButton_Click(object sender, EventArgs e)
        {
            IOtherDrawingAlgorithm algorithm = (IOtherDrawingAlgorithm)OtherAlgorithmCombobox.SelectedItem!;

            await Draw(algorithm, _otherParametersWrapper.Parameters);
        }
        
        private void OtherAlgorithmCombobox_SelectedIndexChanged(object sender, EventArgs e)
        {
            IDrawingAlgorithm algorithm = (IDrawingAlgorithm)OtherAlgorithmCombobox.SelectedItem!;

            _otherParametersWrapper.Parameters = algorithm.EmptyParameters;
        }
    }
}

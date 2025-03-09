namespace LW1
{
    partial class MainForm
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainForm));
            FormSplitContainer = new SplitContainer();
            InstrumentCluster = new TabControl();
            CommonTab = new TabPage();
            groupBox9 = new GroupBox();
            CommonParametersLayoutPanel = new FlowLayoutPanel();
            LinesTab = new TabPage();
            groupBox1 = new GroupBox();
            LineParametersLayoutPanel = new FlowLayoutPanel();
            groupBox6 = new GroupBox();
            tableLayoutPanel1 = new TableLayoutPanel();
            LineDrawingAlgorithmCombobox = new ComboBox();
            DrawLineButton = new Button();
            SecondDegreeCurvesTab = new TabPage();
            CurveParametersGroupBox = new GroupBox();
            CurveParametersLayoutPanel = new FlowLayoutPanel();
            groupBox4 = new GroupBox();
            tableLayoutPanel2 = new TableLayoutPanel();
            CurveTypeCombobox = new ComboBox();
            DrawCurveButton = new Button();
            SplinesTab = new TabPage();
            groupBox3 = new GroupBox();
            SplineParametersLayoutPanel = new FlowLayoutPanel();
            groupBox5 = new GroupBox();
            tableLayoutPanel3 = new TableLayoutPanel();
            DrawSplineButton = new Button();
            SplineTypeCombobox = new ComboBox();
            PolygonsTab = new TabPage();
            groupBox8 = new GroupBox();
            LineIntersectionLayoutPanel = new FlowLayoutPanel();
            IntersectLineButton = new Button();
            groupBox7 = new GroupBox();
            CheckBelongingButton = new Button();
            PointBelongingLayoutPanel = new FlowLayoutPanel();
            PolygonParamsGroupbox = new GroupBox();
            PolygonParametersLayoutPanel = new FlowLayoutPanel();
            groupBox2 = new GroupBox();
            tableLayoutPanel4 = new TableLayoutPanel();
            DrawPolygonNormalsButton = new Button();
            CheckConvexButton = new Button();
            DrawPolygonButton = new Button();
            PolygonAlgorithmCombobox = new ComboBox();
            OtherAlgorithmsTab = new TabPage();
            groupBox11 = new GroupBox();
            OtherParametersPanel = new FlowLayoutPanel();
            groupBox10 = new GroupBox();
            tableLayoutPanel5 = new TableLayoutPanel();
            DrawOtherButton = new Button();
            OtherAlgorithmCombobox = new ComboBox();
            WorkSpaceSplitContainer = new SplitContainer();
            CanvasPictureBox = new View.Canvas();
            panel1 = new Panel();
            EnableDebugButton = new CheckBox();
            button2 = new Button();
            DebugGridView = new DataGridView();
            ((System.ComponentModel.ISupportInitialize)FormSplitContainer).BeginInit();
            FormSplitContainer.Panel1.SuspendLayout();
            FormSplitContainer.Panel2.SuspendLayout();
            FormSplitContainer.SuspendLayout();
            InstrumentCluster.SuspendLayout();
            CommonTab.SuspendLayout();
            groupBox9.SuspendLayout();
            LinesTab.SuspendLayout();
            groupBox1.SuspendLayout();
            groupBox6.SuspendLayout();
            tableLayoutPanel1.SuspendLayout();
            SecondDegreeCurvesTab.SuspendLayout();
            CurveParametersGroupBox.SuspendLayout();
            groupBox4.SuspendLayout();
            tableLayoutPanel2.SuspendLayout();
            SplinesTab.SuspendLayout();
            groupBox3.SuspendLayout();
            groupBox5.SuspendLayout();
            tableLayoutPanel3.SuspendLayout();
            PolygonsTab.SuspendLayout();
            groupBox8.SuspendLayout();
            groupBox7.SuspendLayout();
            PolygonParamsGroupbox.SuspendLayout();
            groupBox2.SuspendLayout();
            tableLayoutPanel4.SuspendLayout();
            OtherAlgorithmsTab.SuspendLayout();
            groupBox11.SuspendLayout();
            groupBox10.SuspendLayout();
            tableLayoutPanel5.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)WorkSpaceSplitContainer).BeginInit();
            WorkSpaceSplitContainer.Panel1.SuspendLayout();
            WorkSpaceSplitContainer.Panel2.SuspendLayout();
            WorkSpaceSplitContainer.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)CanvasPictureBox).BeginInit();
            panel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)DebugGridView).BeginInit();
            SuspendLayout();
            // 
            // FormSplitContainer
            // 
            FormSplitContainer.Dock = DockStyle.Fill;
            FormSplitContainer.FixedPanel = FixedPanel.Panel1;
            FormSplitContainer.Location = new Point(0, 0);
            FormSplitContainer.Name = "FormSplitContainer";
            FormSplitContainer.Orientation = Orientation.Horizontal;
            // 
            // FormSplitContainer.Panel1
            // 
            FormSplitContainer.Panel1.Controls.Add(InstrumentCluster);
            // 
            // FormSplitContainer.Panel2
            // 
            FormSplitContainer.Panel2.Controls.Add(WorkSpaceSplitContainer);
            FormSplitContainer.Size = new Size(1182, 753);
            FormSplitContainer.SplitterDistance = 185;
            FormSplitContainer.TabIndex = 0;
            // 
            // InstrumentCluster
            // 
            InstrumentCluster.Controls.Add(CommonTab);
            InstrumentCluster.Controls.Add(LinesTab);
            InstrumentCluster.Controls.Add(SecondDegreeCurvesTab);
            InstrumentCluster.Controls.Add(SplinesTab);
            InstrumentCluster.Controls.Add(PolygonsTab);
            InstrumentCluster.Controls.Add(OtherAlgorithmsTab);
            InstrumentCluster.Dock = DockStyle.Fill;
            InstrumentCluster.ItemSize = new Size(150, 25);
            InstrumentCluster.Location = new Point(0, 0);
            InstrumentCluster.Name = "InstrumentCluster";
            InstrumentCluster.SelectedIndex = 0;
            InstrumentCluster.Size = new Size(1182, 185);
            InstrumentCluster.TabIndex = 0;
            // 
            // CommonTab
            // 
            CommonTab.AutoScroll = true;
            CommonTab.Controls.Add(groupBox9);
            CommonTab.Location = new Point(4, 29);
            CommonTab.Margin = new Padding(2);
            CommonTab.Name = "CommonTab";
            CommonTab.Padding = new Padding(2);
            CommonTab.Size = new Size(1174, 152);
            CommonTab.TabIndex = 4;
            CommonTab.Text = "Главная";
            CommonTab.UseVisualStyleBackColor = true;
            // 
            // groupBox9
            // 
            groupBox9.AutoSize = true;
            groupBox9.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            groupBox9.Controls.Add(CommonParametersLayoutPanel);
            groupBox9.Dock = DockStyle.Fill;
            groupBox9.Location = new Point(2, 2);
            groupBox9.Name = "groupBox9";
            groupBox9.Size = new Size(1170, 148);
            groupBox9.TabIndex = 8;
            groupBox9.TabStop = false;
            groupBox9.Text = "Параметры";
            // 
            // CommonParametersLayoutPanel
            // 
            CommonParametersLayoutPanel.AutoSize = true;
            CommonParametersLayoutPanel.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            CommonParametersLayoutPanel.Dock = DockStyle.Fill;
            CommonParametersLayoutPanel.Location = new Point(3, 23);
            CommonParametersLayoutPanel.Name = "CommonParametersLayoutPanel";
            CommonParametersLayoutPanel.Size = new Size(1164, 122);
            CommonParametersLayoutPanel.TabIndex = 0;
            // 
            // LinesTab
            // 
            LinesTab.AutoScroll = true;
            LinesTab.Controls.Add(groupBox1);
            LinesTab.Controls.Add(groupBox6);
            LinesTab.Location = new Point(4, 29);
            LinesTab.Name = "LinesTab";
            LinesTab.Padding = new Padding(3);
            LinesTab.Size = new Size(1174, 152);
            LinesTab.TabIndex = 0;
            LinesTab.Text = "Отрезки";
            LinesTab.UseVisualStyleBackColor = true;
            // 
            // groupBox1
            // 
            groupBox1.AutoSize = true;
            groupBox1.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            groupBox1.Controls.Add(LineParametersLayoutPanel);
            groupBox1.Dock = DockStyle.Fill;
            groupBox1.Location = new Point(203, 3);
            groupBox1.Name = "groupBox1";
            groupBox1.Size = new Size(968, 146);
            groupBox1.TabIndex = 9;
            groupBox1.TabStop = false;
            groupBox1.Text = "Параметры отрезка";
            // 
            // LineParametersLayoutPanel
            // 
            LineParametersLayoutPanel.AutoSize = true;
            LineParametersLayoutPanel.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            LineParametersLayoutPanel.Dock = DockStyle.Fill;
            LineParametersLayoutPanel.Location = new Point(3, 23);
            LineParametersLayoutPanel.Name = "LineParametersLayoutPanel";
            LineParametersLayoutPanel.Size = new Size(962, 120);
            LineParametersLayoutPanel.TabIndex = 0;
            // 
            // groupBox6
            // 
            groupBox6.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            groupBox6.Controls.Add(tableLayoutPanel1);
            groupBox6.Dock = DockStyle.Left;
            groupBox6.Location = new Point(3, 3);
            groupBox6.Name = "groupBox6";
            groupBox6.Size = new Size(200, 146);
            groupBox6.TabIndex = 10;
            groupBox6.TabStop = false;
            groupBox6.Text = "Алгоритм";
            // 
            // tableLayoutPanel1
            // 
            tableLayoutPanel1.AutoSize = true;
            tableLayoutPanel1.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            tableLayoutPanel1.ColumnCount = 1;
            tableLayoutPanel1.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 100F));
            tableLayoutPanel1.Controls.Add(LineDrawingAlgorithmCombobox, 0, 0);
            tableLayoutPanel1.Controls.Add(DrawLineButton, 0, 1);
            tableLayoutPanel1.Dock = DockStyle.Fill;
            tableLayoutPanel1.GrowStyle = TableLayoutPanelGrowStyle.AddColumns;
            tableLayoutPanel1.Location = new Point(3, 23);
            tableLayoutPanel1.Name = "tableLayoutPanel1";
            tableLayoutPanel1.RowCount = 2;
            tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 50F));
            tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 50F));
            tableLayoutPanel1.Size = new Size(194, 120);
            tableLayoutPanel1.TabIndex = 7;
            // 
            // LineDrawingAlgorithmCombobox
            // 
            LineDrawingAlgorithmCombobox.Dock = DockStyle.Fill;
            LineDrawingAlgorithmCombobox.FormattingEnabled = true;
            LineDrawingAlgorithmCombobox.Location = new Point(3, 3);
            LineDrawingAlgorithmCombobox.Name = "LineDrawingAlgorithmCombobox";
            LineDrawingAlgorithmCombobox.Size = new Size(188, 28);
            LineDrawingAlgorithmCombobox.TabIndex = 0;
            // 
            // DrawLineButton
            // 
            DrawLineButton.AutoSize = true;
            DrawLineButton.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            DrawLineButton.Dock = DockStyle.Fill;
            DrawLineButton.Location = new Point(3, 63);
            DrawLineButton.Name = "DrawLineButton";
            DrawLineButton.Size = new Size(188, 54);
            DrawLineButton.TabIndex = 6;
            DrawLineButton.Text = "Построить";
            DrawLineButton.UseVisualStyleBackColor = true;
            DrawLineButton.Click += DrawLineButton_Click;
            // 
            // SecondDegreeCurvesTab
            // 
            SecondDegreeCurvesTab.AutoScroll = true;
            SecondDegreeCurvesTab.Controls.Add(CurveParametersGroupBox);
            SecondDegreeCurvesTab.Controls.Add(groupBox4);
            SecondDegreeCurvesTab.Location = new Point(4, 29);
            SecondDegreeCurvesTab.Name = "SecondDegreeCurvesTab";
            SecondDegreeCurvesTab.Padding = new Padding(3);
            SecondDegreeCurvesTab.Size = new Size(1174, 152);
            SecondDegreeCurvesTab.TabIndex = 1;
            SecondDegreeCurvesTab.Text = "Кривые 2-го порядка";
            SecondDegreeCurvesTab.UseVisualStyleBackColor = true;
            // 
            // CurveParametersGroupBox
            // 
            CurveParametersGroupBox.AutoSize = true;
            CurveParametersGroupBox.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            CurveParametersGroupBox.Controls.Add(CurveParametersLayoutPanel);
            CurveParametersGroupBox.Dock = DockStyle.Left;
            CurveParametersGroupBox.Location = new Point(203, 3);
            CurveParametersGroupBox.Name = "CurveParametersGroupBox";
            CurveParametersGroupBox.Size = new Size(6, 146);
            CurveParametersGroupBox.TabIndex = 7;
            CurveParametersGroupBox.TabStop = false;
            CurveParametersGroupBox.Text = "Параметры";
            // 
            // CurveParametersLayoutPanel
            // 
            CurveParametersLayoutPanel.AutoSize = true;
            CurveParametersLayoutPanel.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            CurveParametersLayoutPanel.Dock = DockStyle.Fill;
            CurveParametersLayoutPanel.Location = new Point(3, 23);
            CurveParametersLayoutPanel.Name = "CurveParametersLayoutPanel";
            CurveParametersLayoutPanel.Size = new Size(0, 120);
            CurveParametersLayoutPanel.TabIndex = 0;
            // 
            // groupBox4
            // 
            groupBox4.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            groupBox4.Controls.Add(tableLayoutPanel2);
            groupBox4.Dock = DockStyle.Left;
            groupBox4.Location = new Point(3, 3);
            groupBox4.Name = "groupBox4";
            groupBox4.Size = new Size(200, 146);
            groupBox4.TabIndex = 3;
            groupBox4.TabStop = false;
            groupBox4.Text = "Тип";
            // 
            // tableLayoutPanel2
            // 
            tableLayoutPanel2.AutoSize = true;
            tableLayoutPanel2.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            tableLayoutPanel2.ColumnCount = 1;
            tableLayoutPanel2.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 100F));
            tableLayoutPanel2.Controls.Add(CurveTypeCombobox, 0, 0);
            tableLayoutPanel2.Controls.Add(DrawCurveButton, 0, 1);
            tableLayoutPanel2.Dock = DockStyle.Fill;
            tableLayoutPanel2.GrowStyle = TableLayoutPanelGrowStyle.FixedSize;
            tableLayoutPanel2.Location = new Point(3, 23);
            tableLayoutPanel2.Name = "tableLayoutPanel2";
            tableLayoutPanel2.RowCount = 2;
            tableLayoutPanel2.RowStyles.Add(new RowStyle(SizeType.Percent, 50F));
            tableLayoutPanel2.RowStyles.Add(new RowStyle(SizeType.Percent, 50F));
            tableLayoutPanel2.Size = new Size(194, 120);
            tableLayoutPanel2.TabIndex = 8;
            // 
            // CurveTypeCombobox
            // 
            CurveTypeCombobox.Dock = DockStyle.Fill;
            CurveTypeCombobox.FormattingEnabled = true;
            CurveTypeCombobox.Location = new Point(3, 3);
            CurveTypeCombobox.Name = "CurveTypeCombobox";
            CurveTypeCombobox.Size = new Size(188, 28);
            CurveTypeCombobox.TabIndex = 0;
            CurveTypeCombobox.SelectedIndexChanged += CurveTypeCombobox_SelectedIndexChanged;
            // 
            // DrawCurveButton
            // 
            DrawCurveButton.AutoSize = true;
            DrawCurveButton.Dock = DockStyle.Fill;
            DrawCurveButton.Location = new Point(3, 63);
            DrawCurveButton.Name = "DrawCurveButton";
            DrawCurveButton.Size = new Size(188, 54);
            DrawCurveButton.TabIndex = 6;
            DrawCurveButton.Text = "Построить";
            DrawCurveButton.UseVisualStyleBackColor = true;
            DrawCurveButton.Click += DrawCurveButton_ClickAsync;
            // 
            // SplinesTab
            // 
            SplinesTab.AutoScroll = true;
            SplinesTab.Controls.Add(groupBox3);
            SplinesTab.Controls.Add(groupBox5);
            SplinesTab.Location = new Point(4, 29);
            SplinesTab.Name = "SplinesTab";
            SplinesTab.Padding = new Padding(3);
            SplinesTab.Size = new Size(1174, 152);
            SplinesTab.TabIndex = 2;
            SplinesTab.Text = "Параметрические кривые";
            SplinesTab.UseVisualStyleBackColor = true;
            // 
            // groupBox3
            // 
            groupBox3.AutoSize = true;
            groupBox3.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            groupBox3.Controls.Add(SplineParametersLayoutPanel);
            groupBox3.Dock = DockStyle.Left;
            groupBox3.Location = new Point(203, 3);
            groupBox3.Name = "groupBox3";
            groupBox3.Size = new Size(6, 146);
            groupBox3.TabIndex = 9;
            groupBox3.TabStop = false;
            groupBox3.Text = "Параметры";
            // 
            // SplineParametersLayoutPanel
            // 
            SplineParametersLayoutPanel.AutoSize = true;
            SplineParametersLayoutPanel.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            SplineParametersLayoutPanel.Dock = DockStyle.Fill;
            SplineParametersLayoutPanel.Location = new Point(3, 23);
            SplineParametersLayoutPanel.Name = "SplineParametersLayoutPanel";
            SplineParametersLayoutPanel.Size = new Size(0, 120);
            SplineParametersLayoutPanel.TabIndex = 0;
            // 
            // groupBox5
            // 
            groupBox5.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            groupBox5.Controls.Add(tableLayoutPanel3);
            groupBox5.Dock = DockStyle.Left;
            groupBox5.Location = new Point(3, 3);
            groupBox5.Name = "groupBox5";
            groupBox5.Size = new Size(200, 146);
            groupBox5.TabIndex = 8;
            groupBox5.TabStop = false;
            groupBox5.Text = "Тип";
            // 
            // tableLayoutPanel3
            // 
            tableLayoutPanel3.AutoSize = true;
            tableLayoutPanel3.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            tableLayoutPanel3.ColumnCount = 1;
            tableLayoutPanel3.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 100F));
            tableLayoutPanel3.Controls.Add(DrawSplineButton, 0, 1);
            tableLayoutPanel3.Controls.Add(SplineTypeCombobox, 0, 0);
            tableLayoutPanel3.Dock = DockStyle.Fill;
            tableLayoutPanel3.GrowStyle = TableLayoutPanelGrowStyle.FixedSize;
            tableLayoutPanel3.Location = new Point(3, 23);
            tableLayoutPanel3.Name = "tableLayoutPanel3";
            tableLayoutPanel3.RowCount = 2;
            tableLayoutPanel3.RowStyles.Add(new RowStyle(SizeType.Percent, 50F));
            tableLayoutPanel3.RowStyles.Add(new RowStyle(SizeType.Percent, 50F));
            tableLayoutPanel3.Size = new Size(194, 120);
            tableLayoutPanel3.TabIndex = 9;
            // 
            // DrawSplineButton
            // 
            DrawSplineButton.AutoSize = true;
            DrawSplineButton.Dock = DockStyle.Fill;
            DrawSplineButton.Location = new Point(3, 63);
            DrawSplineButton.Name = "DrawSplineButton";
            DrawSplineButton.Size = new Size(188, 54);
            DrawSplineButton.TabIndex = 6;
            DrawSplineButton.Text = "Построить";
            DrawSplineButton.UseVisualStyleBackColor = true;
            DrawSplineButton.Click += DrawSplineButton_Click;
            // 
            // SplineTypeCombobox
            // 
            SplineTypeCombobox.Dock = DockStyle.Fill;
            SplineTypeCombobox.FormattingEnabled = true;
            SplineTypeCombobox.Location = new Point(3, 3);
            SplineTypeCombobox.Name = "SplineTypeCombobox";
            SplineTypeCombobox.Size = new Size(188, 28);
            SplineTypeCombobox.TabIndex = 0;
            SplineTypeCombobox.SelectedIndexChanged += SplineTypeCombobox_SelectedIndexChanged;
            // 
            // PolygonsTab
            // 
            PolygonsTab.AutoScroll = true;
            PolygonsTab.Controls.Add(groupBox8);
            PolygonsTab.Controls.Add(groupBox7);
            PolygonsTab.Controls.Add(PolygonParamsGroupbox);
            PolygonsTab.Controls.Add(groupBox2);
            PolygonsTab.Location = new Point(4, 29);
            PolygonsTab.Name = "PolygonsTab";
            PolygonsTab.Padding = new Padding(3);
            PolygonsTab.Size = new Size(1174, 152);
            PolygonsTab.TabIndex = 3;
            PolygonsTab.Text = "Полигоны";
            PolygonsTab.UseVisualStyleBackColor = true;
            // 
            // groupBox8
            // 
            groupBox8.AutoSize = true;
            groupBox8.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            groupBox8.Controls.Add(LineIntersectionLayoutPanel);
            groupBox8.Controls.Add(IntersectLineButton);
            groupBox8.Dock = DockStyle.Left;
            groupBox8.Location = new Point(215, 3);
            groupBox8.Name = "groupBox8";
            groupBox8.Size = new Size(6, 146);
            groupBox8.TabIndex = 12;
            groupBox8.TabStop = false;
            groupBox8.Text = "Пересечение с прямой";
            // 
            // LineIntersectionLayoutPanel
            // 
            LineIntersectionLayoutPanel.AutoSize = true;
            LineIntersectionLayoutPanel.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            LineIntersectionLayoutPanel.Dock = DockStyle.Fill;
            LineIntersectionLayoutPanel.Location = new Point(3, 23);
            LineIntersectionLayoutPanel.Name = "LineIntersectionLayoutPanel";
            LineIntersectionLayoutPanel.Size = new Size(0, 90);
            LineIntersectionLayoutPanel.TabIndex = 0;
            // 
            // IntersectLineButton
            // 
            IntersectLineButton.AutoSize = true;
            IntersectLineButton.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            IntersectLineButton.Dock = DockStyle.Bottom;
            IntersectLineButton.Location = new Point(3, 113);
            IntersectLineButton.Name = "IntersectLineButton";
            IntersectLineButton.Size = new Size(0, 30);
            IntersectLineButton.TabIndex = 7;
            IntersectLineButton.Text = "Пересечь";
            IntersectLineButton.UseVisualStyleBackColor = true;
            IntersectLineButton.Click += IntersectLineButton_Click;
            // 
            // groupBox7
            // 
            groupBox7.AutoSize = true;
            groupBox7.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            groupBox7.Controls.Add(CheckBelongingButton);
            groupBox7.Controls.Add(PointBelongingLayoutPanel);
            groupBox7.Dock = DockStyle.Left;
            groupBox7.Location = new Point(209, 3);
            groupBox7.Name = "groupBox7";
            groupBox7.Size = new Size(6, 146);
            groupBox7.TabIndex = 11;
            groupBox7.TabStop = false;
            groupBox7.Text = "Принадлежность точки";
            // 
            // CheckBelongingButton
            // 
            CheckBelongingButton.AutoSize = true;
            CheckBelongingButton.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            CheckBelongingButton.Dock = DockStyle.Bottom;
            CheckBelongingButton.Location = new Point(3, 113);
            CheckBelongingButton.Name = "CheckBelongingButton";
            CheckBelongingButton.Size = new Size(0, 30);
            CheckBelongingButton.TabIndex = 8;
            CheckBelongingButton.Text = "Проверить принадлежность";
            CheckBelongingButton.UseVisualStyleBackColor = true;
            CheckBelongingButton.Click += CheckBelongingButton_Click;
            // 
            // PointBelongingLayoutPanel
            // 
            PointBelongingLayoutPanel.AutoSize = true;
            PointBelongingLayoutPanel.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            PointBelongingLayoutPanel.Dock = DockStyle.Fill;
            PointBelongingLayoutPanel.Location = new Point(3, 23);
            PointBelongingLayoutPanel.Name = "PointBelongingLayoutPanel";
            PointBelongingLayoutPanel.Size = new Size(0, 120);
            PointBelongingLayoutPanel.TabIndex = 0;
            // 
            // PolygonParamsGroupbox
            // 
            PolygonParamsGroupbox.AutoSize = true;
            PolygonParamsGroupbox.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            PolygonParamsGroupbox.Controls.Add(PolygonParametersLayoutPanel);
            PolygonParamsGroupbox.Dock = DockStyle.Left;
            PolygonParamsGroupbox.Location = new Point(203, 3);
            PolygonParamsGroupbox.Name = "PolygonParamsGroupbox";
            PolygonParamsGroupbox.Size = new Size(6, 146);
            PolygonParamsGroupbox.TabIndex = 10;
            PolygonParamsGroupbox.TabStop = false;
            PolygonParamsGroupbox.Text = "Параметры полигона";
            // 
            // PolygonParametersLayoutPanel
            // 
            PolygonParametersLayoutPanel.AutoSize = true;
            PolygonParametersLayoutPanel.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            PolygonParametersLayoutPanel.Dock = DockStyle.Fill;
            PolygonParametersLayoutPanel.Location = new Point(3, 23);
            PolygonParametersLayoutPanel.Name = "PolygonParametersLayoutPanel";
            PolygonParametersLayoutPanel.Size = new Size(0, 120);
            PolygonParametersLayoutPanel.TabIndex = 0;
            // 
            // groupBox2
            // 
            groupBox2.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            groupBox2.Controls.Add(tableLayoutPanel4);
            groupBox2.Dock = DockStyle.Left;
            groupBox2.Location = new Point(3, 3);
            groupBox2.Name = "groupBox2";
            groupBox2.Size = new Size(200, 146);
            groupBox2.TabIndex = 9;
            groupBox2.TabStop = false;
            groupBox2.Text = "Тип";
            // 
            // tableLayoutPanel4
            // 
            tableLayoutPanel4.AutoSize = true;
            tableLayoutPanel4.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            tableLayoutPanel4.ColumnCount = 1;
            tableLayoutPanel4.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 100F));
            tableLayoutPanel4.Controls.Add(DrawPolygonNormalsButton, 0, 2);
            tableLayoutPanel4.Controls.Add(CheckConvexButton, 0, 2);
            tableLayoutPanel4.Controls.Add(DrawPolygonButton, 0, 1);
            tableLayoutPanel4.Controls.Add(PolygonAlgorithmCombobox, 0, 0);
            tableLayoutPanel4.Dock = DockStyle.Fill;
            tableLayoutPanel4.GrowStyle = TableLayoutPanelGrowStyle.FixedSize;
            tableLayoutPanel4.Location = new Point(3, 23);
            tableLayoutPanel4.Name = "tableLayoutPanel4";
            tableLayoutPanel4.RowCount = 4;
            tableLayoutPanel4.RowStyles.Add(new RowStyle(SizeType.Percent, 25.0006237F));
            tableLayoutPanel4.RowStyles.Add(new RowStyle(SizeType.Percent, 25.0006275F));
            tableLayoutPanel4.RowStyles.Add(new RowStyle(SizeType.Percent, 25.0006237F));
            tableLayoutPanel4.RowStyles.Add(new RowStyle(SizeType.Percent, 24.9981289F));
            tableLayoutPanel4.Size = new Size(194, 120);
            tableLayoutPanel4.TabIndex = 9;
            // 
            // DrawPolygonNormalsButton
            // 
            DrawPolygonNormalsButton.AutoSize = true;
            DrawPolygonNormalsButton.Dock = DockStyle.Fill;
            DrawPolygonNormalsButton.Location = new Point(3, 63);
            DrawPolygonNormalsButton.Name = "DrawPolygonNormalsButton";
            DrawPolygonNormalsButton.Size = new Size(188, 24);
            DrawPolygonNormalsButton.TabIndex = 8;
            DrawPolygonNormalsButton.Text = "Построить нормали";
            DrawPolygonNormalsButton.UseVisualStyleBackColor = true;
            DrawPolygonNormalsButton.Click += DrawPolygonNormalsButton_Click;
            // 
            // CheckConvexButton
            // 
            CheckConvexButton.AutoSize = true;
            CheckConvexButton.Dock = DockStyle.Fill;
            CheckConvexButton.Location = new Point(3, 93);
            CheckConvexButton.Name = "CheckConvexButton";
            CheckConvexButton.Size = new Size(188, 24);
            CheckConvexButton.TabIndex = 7;
            CheckConvexButton.Text = "Проверка выпуклости";
            CheckConvexButton.UseVisualStyleBackColor = true;
            CheckConvexButton.Click += CheckConvexButton_Click;
            // 
            // DrawPolygonButton
            // 
            DrawPolygonButton.AutoSize = true;
            DrawPolygonButton.Dock = DockStyle.Fill;
            DrawPolygonButton.Location = new Point(3, 33);
            DrawPolygonButton.Name = "DrawPolygonButton";
            DrawPolygonButton.Size = new Size(188, 24);
            DrawPolygonButton.TabIndex = 6;
            DrawPolygonButton.Text = "Построить";
            DrawPolygonButton.UseVisualStyleBackColor = true;
            DrawPolygonButton.Click += DrawPolygonButton_Click;
            // 
            // PolygonAlgorithmCombobox
            // 
            PolygonAlgorithmCombobox.Dock = DockStyle.Fill;
            PolygonAlgorithmCombobox.FormattingEnabled = true;
            PolygonAlgorithmCombobox.Location = new Point(3, 3);
            PolygonAlgorithmCombobox.Name = "PolygonAlgorithmCombobox";
            PolygonAlgorithmCombobox.Size = new Size(188, 28);
            PolygonAlgorithmCombobox.TabIndex = 0;
            // 
            // OtherAlgorithmsTab
            // 
            OtherAlgorithmsTab.AutoScroll = true;
            OtherAlgorithmsTab.Controls.Add(groupBox11);
            OtherAlgorithmsTab.Controls.Add(groupBox10);
            OtherAlgorithmsTab.Location = new Point(4, 29);
            OtherAlgorithmsTab.Name = "OtherAlgorithmsTab";
            OtherAlgorithmsTab.Padding = new Padding(3);
            OtherAlgorithmsTab.Size = new Size(1174, 152);
            OtherAlgorithmsTab.TabIndex = 5;
            OtherAlgorithmsTab.Text = "Прочее";
            OtherAlgorithmsTab.UseVisualStyleBackColor = true;
            // 
            // groupBox11
            // 
            groupBox11.AutoSize = true;
            groupBox11.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            groupBox11.Controls.Add(OtherParametersPanel);
            groupBox11.Dock = DockStyle.Left;
            groupBox11.Location = new Point(203, 3);
            groupBox11.Name = "groupBox11";
            groupBox11.Size = new Size(6, 146);
            groupBox11.TabIndex = 10;
            groupBox11.TabStop = false;
            groupBox11.Text = "Параметры";
            // 
            // OtherParametersPanel
            // 
            OtherParametersPanel.AutoSize = true;
            OtherParametersPanel.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            OtherParametersPanel.Dock = DockStyle.Fill;
            OtherParametersPanel.Location = new Point(3, 23);
            OtherParametersPanel.Name = "OtherParametersPanel";
            OtherParametersPanel.Size = new Size(0, 120);
            OtherParametersPanel.TabIndex = 0;
            // 
            // groupBox10
            // 
            groupBox10.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            groupBox10.Controls.Add(tableLayoutPanel5);
            groupBox10.Dock = DockStyle.Left;
            groupBox10.Location = new Point(3, 3);
            groupBox10.Name = "groupBox10";
            groupBox10.Size = new Size(200, 146);
            groupBox10.TabIndex = 9;
            groupBox10.TabStop = false;
            groupBox10.Text = "Алгоритм";
            // 
            // tableLayoutPanel5
            // 
            tableLayoutPanel5.AutoSize = true;
            tableLayoutPanel5.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            tableLayoutPanel5.ColumnCount = 1;
            tableLayoutPanel5.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 100F));
            tableLayoutPanel5.Controls.Add(DrawOtherButton, 0, 1);
            tableLayoutPanel5.Controls.Add(OtherAlgorithmCombobox, 0, 0);
            tableLayoutPanel5.Dock = DockStyle.Fill;
            tableLayoutPanel5.GrowStyle = TableLayoutPanelGrowStyle.FixedSize;
            tableLayoutPanel5.Location = new Point(3, 23);
            tableLayoutPanel5.Name = "tableLayoutPanel5";
            tableLayoutPanel5.RowCount = 2;
            tableLayoutPanel5.RowStyles.Add(new RowStyle(SizeType.Percent, 50F));
            tableLayoutPanel5.RowStyles.Add(new RowStyle(SizeType.Percent, 50F));
            tableLayoutPanel5.Size = new Size(194, 120);
            tableLayoutPanel5.TabIndex = 9;
            // 
            // DrawOtherButton
            // 
            DrawOtherButton.AutoSize = true;
            DrawOtherButton.Dock = DockStyle.Fill;
            DrawOtherButton.Location = new Point(3, 63);
            DrawOtherButton.Name = "DrawOtherButton";
            DrawOtherButton.Size = new Size(188, 54);
            DrawOtherButton.TabIndex = 6;
            DrawOtherButton.Text = "Построить";
            DrawOtherButton.UseVisualStyleBackColor = true;
            DrawOtherButton.Click += DrawOtherButton_Click;
            // 
            // OtherAlgorithmCombobox
            // 
            OtherAlgorithmCombobox.Dock = DockStyle.Fill;
            OtherAlgorithmCombobox.FormattingEnabled = true;
            OtherAlgorithmCombobox.Location = new Point(3, 3);
            OtherAlgorithmCombobox.Name = "OtherAlgorithmCombobox";
            OtherAlgorithmCombobox.Size = new Size(188, 28);
            OtherAlgorithmCombobox.TabIndex = 0;
            // 
            // WorkSpaceSplitContainer
            // 
            WorkSpaceSplitContainer.Dock = DockStyle.Fill;
            WorkSpaceSplitContainer.FixedPanel = FixedPanel.Panel2;
            WorkSpaceSplitContainer.Location = new Point(0, 0);
            WorkSpaceSplitContainer.Name = "WorkSpaceSplitContainer";
            // 
            // WorkSpaceSplitContainer.Panel1
            // 
            WorkSpaceSplitContainer.Panel1.AutoScroll = true;
            WorkSpaceSplitContainer.Panel1.AutoScrollMinSize = new Size(525, 525);
            WorkSpaceSplitContainer.Panel1.BackColor = SystemColors.ControlDark;
            WorkSpaceSplitContainer.Panel1.Controls.Add(CanvasPictureBox);
            // 
            // WorkSpaceSplitContainer.Panel2
            // 
            WorkSpaceSplitContainer.Panel2.Controls.Add(panel1);
            WorkSpaceSplitContainer.Panel2.Controls.Add(DebugGridView);
            WorkSpaceSplitContainer.Size = new Size(1182, 564);
            WorkSpaceSplitContainer.SplitterDistance = 846;
            WorkSpaceSplitContainer.TabIndex = 0;
            // 
            // CanvasPictureBox
            // 
            CanvasPictureBox.Anchor = AnchorStyles.None;
            CanvasPictureBox.BackColor = Color.White;
            CanvasPictureBox.BorderStyle = BorderStyle.FixedSingle;
            CanvasPictureBox.Cursor = Cursors.Cross;
            CanvasPictureBox.Image = (Image)resources.GetObject("CanvasPictureBox.Image");
            CanvasPictureBox.Location = new Point(-256, -256);
            CanvasPictureBox.Margin = new Padding(2);
            CanvasPictureBox.Name = "CanvasPictureBox";
            CanvasPictureBox.Size = new Size(512, 512);
            CanvasPictureBox.TabIndex = 1;
            CanvasPictureBox.TabStop = false;
            // 
            // panel1
            // 
            panel1.Controls.Add(EnableDebugButton);
            panel1.Controls.Add(button2);
            panel1.Dock = DockStyle.Top;
            panel1.Location = new Point(0, 0);
            panel1.Margin = new Padding(2);
            panel1.Name = "panel1";
            panel1.Size = new Size(332, 32);
            panel1.TabIndex = 4;
            // 
            // EnableDebugButton
            // 
            EnableDebugButton.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left;
            EnableDebugButton.AutoSize = true;
            EnableDebugButton.Location = new Point(5, 5);
            EnableDebugButton.Name = "EnableDebugButton";
            EnableDebugButton.Size = new Size(137, 24);
            EnableDebugButton.TabIndex = 0;
            EnableDebugButton.Text = "Режим отладки";
            EnableDebugButton.UseVisualStyleBackColor = true;
            // 
            // button2
            // 
            button2.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Right;
            button2.Location = new Point(175, 2);
            button2.Name = "button2";
            button2.Size = new Size(157, 29);
            button2.TabIndex = 2;
            button2.Text = "Очистить все";
            button2.UseVisualStyleBackColor = true;
            button2.Click += ClearAll_Click;
            // 
            // DebugGridView
            // 
            DebugGridView.AllowUserToAddRows = false;
            DebugGridView.AllowUserToDeleteRows = false;
            DebugGridView.AllowUserToResizeRows = false;
            DebugGridView.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
            DebugGridView.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.AllCells;
            DebugGridView.BorderStyle = BorderStyle.None;
            DebugGridView.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            DebugGridView.Location = new Point(0, 34);
            DebugGridView.Margin = new Padding(0);
            DebugGridView.Name = "DebugGridView";
            DebugGridView.RowHeadersWidth = 51;
            DebugGridView.Size = new Size(323, 530);
            DebugGridView.TabIndex = 3;
            // 
            // MainForm
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(1182, 753);
            Controls.Add(FormSplitContainer);
            Name = "MainForm";
            ShowIcon = false;
            StartPosition = FormStartPosition.CenterScreen;
            Text = "GIIS LW";
            FormSplitContainer.Panel1.ResumeLayout(false);
            FormSplitContainer.Panel2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)FormSplitContainer).EndInit();
            FormSplitContainer.ResumeLayout(false);
            InstrumentCluster.ResumeLayout(false);
            CommonTab.ResumeLayout(false);
            CommonTab.PerformLayout();
            groupBox9.ResumeLayout(false);
            groupBox9.PerformLayout();
            LinesTab.ResumeLayout(false);
            LinesTab.PerformLayout();
            groupBox1.ResumeLayout(false);
            groupBox1.PerformLayout();
            groupBox6.ResumeLayout(false);
            groupBox6.PerformLayout();
            tableLayoutPanel1.ResumeLayout(false);
            tableLayoutPanel1.PerformLayout();
            SecondDegreeCurvesTab.ResumeLayout(false);
            SecondDegreeCurvesTab.PerformLayout();
            CurveParametersGroupBox.ResumeLayout(false);
            CurveParametersGroupBox.PerformLayout();
            groupBox4.ResumeLayout(false);
            groupBox4.PerformLayout();
            tableLayoutPanel2.ResumeLayout(false);
            tableLayoutPanel2.PerformLayout();
            SplinesTab.ResumeLayout(false);
            SplinesTab.PerformLayout();
            groupBox3.ResumeLayout(false);
            groupBox3.PerformLayout();
            groupBox5.ResumeLayout(false);
            groupBox5.PerformLayout();
            tableLayoutPanel3.ResumeLayout(false);
            tableLayoutPanel3.PerformLayout();
            PolygonsTab.ResumeLayout(false);
            PolygonsTab.PerformLayout();
            groupBox8.ResumeLayout(false);
            groupBox8.PerformLayout();
            groupBox7.ResumeLayout(false);
            groupBox7.PerformLayout();
            PolygonParamsGroupbox.ResumeLayout(false);
            PolygonParamsGroupbox.PerformLayout();
            groupBox2.ResumeLayout(false);
            groupBox2.PerformLayout();
            tableLayoutPanel4.ResumeLayout(false);
            tableLayoutPanel4.PerformLayout();
            OtherAlgorithmsTab.ResumeLayout(false);
            OtherAlgorithmsTab.PerformLayout();
            groupBox11.ResumeLayout(false);
            groupBox11.PerformLayout();
            groupBox10.ResumeLayout(false);
            groupBox10.PerformLayout();
            tableLayoutPanel5.ResumeLayout(false);
            tableLayoutPanel5.PerformLayout();
            WorkSpaceSplitContainer.Panel1.ResumeLayout(false);
            WorkSpaceSplitContainer.Panel2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)WorkSpaceSplitContainer).EndInit();
            WorkSpaceSplitContainer.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)CanvasPictureBox).EndInit();
            panel1.ResumeLayout(false);
            panel1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)DebugGridView).EndInit();
            ResumeLayout(false);
        }

        #endregion

        private SplitContainer FormSplitContainer;
        private TabControl InstrumentCluster;
        private TabPage LinesTab;
        private TabPage SecondDegreeCurvesTab;
        private SplitContainer WorkSpaceSplitContainer;
        private CheckBox EnableDebugButton;
        private Button button2;
        private DataGridView DebugGridView;
        private GroupBox groupBox4;
        private ComboBox CurveTypeCombobox;
        private Button DrawCurveButton;
        private GroupBox CurveParametersGroupBox;
        private FlowLayoutPanel CurveParametersLayoutPanel;
        private GroupBox groupBox1;
        private FlowLayoutPanel LineParametersLayoutPanel;
        private TabPage SplinesTab;
        private GroupBox groupBox3;
        private FlowLayoutPanel SplineParametersLayoutPanel;
        private GroupBox groupBox5;
        private Button DrawSplineButton;
        private ComboBox SplineTypeCombobox;
        private View.Canvas CanvasPictureBox;
        private TableLayoutPanel tableLayoutPanel1;
        private Button DrawLineButton;
        private ComboBox LineDrawingAlgorithmCombobox;
        private TableLayoutPanel tableLayoutPanel2;
        private TableLayoutPanel tableLayoutPanel3;
        private GroupBox groupBox6;
        private TabPage PolygonsTab;
        private GroupBox PolygonParamsGroupbox;
        private FlowLayoutPanel PolygonParametersLayoutPanel;
        private GroupBox groupBox2;
        private TableLayoutPanel tableLayoutPanel4;
        private Button DrawPolygonButton;
        private ComboBox PolygonAlgorithmCombobox;
        private GroupBox groupBox7;
        private FlowLayoutPanel PointBelongingLayoutPanel;
        private GroupBox groupBox8;
        private FlowLayoutPanel LineIntersectionLayoutPanel;
        private Button IntersectLineButton;
        private Button CheckBelongingButton;
        private Button CheckConvexButton;
        private Button DrawPolygonNormalsButton;
        private Panel panel1;
        private TabPage CommonTab;
        private GroupBox groupBox9;
        private FlowLayoutPanel CommonParametersLayoutPanel;
        private TabPage OtherAlgorithmsTab;
        private GroupBox groupBox11;
        private FlowLayoutPanel OtherParametersPanel;
        private GroupBox groupBox10;
        private TableLayoutPanel tableLayoutPanel5;
        private Button DrawOtherButton;
        private ComboBox OtherAlgorithmCombobox;
    }
}

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
            WorkSpaceSplitContainer = new SplitContainer();
            CanvasPictureBox = new View.Canvas();
            panel1 = new Panel();
            EnableDebugButton = new CheckBox();
            button2 = new Button();
            DebugGridView = new DataGridView();
            groupBox9 = new GroupBox();
            CommonParametersLayoutPanel = new FlowLayoutPanel();
            ((System.ComponentModel.ISupportInitialize)FormSplitContainer).BeginInit();
            FormSplitContainer.Panel1.SuspendLayout();
            FormSplitContainer.Panel2.SuspendLayout();
            FormSplitContainer.SuspendLayout();
            InstrumentCluster.SuspendLayout();
            CommonTab.SuspendLayout();
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
            ((System.ComponentModel.ISupportInitialize)WorkSpaceSplitContainer).BeginInit();
            WorkSpaceSplitContainer.Panel1.SuspendLayout();
            WorkSpaceSplitContainer.Panel2.SuspendLayout();
            WorkSpaceSplitContainer.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)CanvasPictureBox).BeginInit();
            panel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)DebugGridView).BeginInit();
            groupBox9.SuspendLayout();
            SuspendLayout();
            // 
            // FormSplitContainer
            // 
            FormSplitContainer.Dock = DockStyle.Fill;
            FormSplitContainer.FixedPanel = FixedPanel.Panel1;
            FormSplitContainer.Location = new Point(0, 0);
            FormSplitContainer.Margin = new Padding(4);
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
            FormSplitContainer.Size = new Size(1478, 941);
            FormSplitContainer.SplitterDistance = 231;
            FormSplitContainer.SplitterWidth = 5;
            FormSplitContainer.TabIndex = 0;
            // 
            // InstrumentCluster
            // 
            InstrumentCluster.Controls.Add(CommonTab);
            InstrumentCluster.Controls.Add(LinesTab);
            InstrumentCluster.Controls.Add(SecondDegreeCurvesTab);
            InstrumentCluster.Controls.Add(SplinesTab);
            InstrumentCluster.Controls.Add(PolygonsTab);
            InstrumentCluster.Dock = DockStyle.Fill;
            InstrumentCluster.ItemSize = new Size(150, 25);
            InstrumentCluster.Location = new Point(0, 0);
            InstrumentCluster.Margin = new Padding(4);
            InstrumentCluster.Name = "InstrumentCluster";
            InstrumentCluster.SelectedIndex = 0;
            InstrumentCluster.Size = new Size(1478, 231);
            InstrumentCluster.TabIndex = 0;
            // 
            // CommonTab
            // 
            CommonTab.Controls.Add(groupBox9);
            CommonTab.Location = new Point(4, 29);
            CommonTab.Name = "CommonTab";
            CommonTab.Padding = new Padding(3);
            CommonTab.Size = new Size(1470, 198);
            CommonTab.TabIndex = 4;
            CommonTab.Text = "Главная";
            CommonTab.UseVisualStyleBackColor = true;
            // 
            // LinesTab
            // 
            LinesTab.AutoScroll = true;
            LinesTab.Controls.Add(groupBox1);
            LinesTab.Controls.Add(groupBox6);
            LinesTab.Location = new Point(4, 29);
            LinesTab.Margin = new Padding(4);
            LinesTab.Name = "LinesTab";
            LinesTab.Padding = new Padding(4);
            LinesTab.Size = new Size(1470, 198);
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
            groupBox1.Location = new Point(254, 4);
            groupBox1.Margin = new Padding(4);
            groupBox1.Name = "groupBox1";
            groupBox1.Padding = new Padding(4);
            groupBox1.Size = new Size(1212, 190);
            groupBox1.TabIndex = 9;
            groupBox1.TabStop = false;
            groupBox1.Text = "Параметры отрезка";
            // 
            // LineParametersLayoutPanel
            // 
            LineParametersLayoutPanel.AutoScroll = true;
            LineParametersLayoutPanel.AutoSize = true;
            LineParametersLayoutPanel.Dock = DockStyle.Fill;
            LineParametersLayoutPanel.Location = new Point(4, 28);
            LineParametersLayoutPanel.Margin = new Padding(4);
            LineParametersLayoutPanel.Name = "LineParametersLayoutPanel";
            LineParametersLayoutPanel.Size = new Size(1204, 158);
            LineParametersLayoutPanel.TabIndex = 0;
            // 
            // groupBox6
            // 
            groupBox6.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            groupBox6.Controls.Add(tableLayoutPanel1);
            groupBox6.Dock = DockStyle.Left;
            groupBox6.Location = new Point(4, 4);
            groupBox6.Margin = new Padding(4);
            groupBox6.Name = "groupBox6";
            groupBox6.Padding = new Padding(4);
            groupBox6.Size = new Size(250, 190);
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
            tableLayoutPanel1.Location = new Point(4, 28);
            tableLayoutPanel1.Margin = new Padding(4);
            tableLayoutPanel1.Name = "tableLayoutPanel1";
            tableLayoutPanel1.RowCount = 2;
            tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 50F));
            tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 50F));
            tableLayoutPanel1.Size = new Size(242, 158);
            tableLayoutPanel1.TabIndex = 7;
            // 
            // LineDrawingAlgorithmCombobox
            // 
            LineDrawingAlgorithmCombobox.Dock = DockStyle.Fill;
            LineDrawingAlgorithmCombobox.FormattingEnabled = true;
            LineDrawingAlgorithmCombobox.Location = new Point(4, 4);
            LineDrawingAlgorithmCombobox.Margin = new Padding(4);
            LineDrawingAlgorithmCombobox.Name = "LineDrawingAlgorithmCombobox";
            LineDrawingAlgorithmCombobox.Size = new Size(234, 33);
            LineDrawingAlgorithmCombobox.TabIndex = 0;
            // 
            // DrawLineButton
            // 
            DrawLineButton.AutoSize = true;
            DrawLineButton.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            DrawLineButton.Dock = DockStyle.Fill;
            DrawLineButton.Location = new Point(4, 83);
            DrawLineButton.Margin = new Padding(4);
            DrawLineButton.Name = "DrawLineButton";
            DrawLineButton.Size = new Size(234, 71);
            DrawLineButton.TabIndex = 6;
            DrawLineButton.Text = "Построить";
            DrawLineButton.UseVisualStyleBackColor = true;
            DrawLineButton.Click += DrawLineButton_Click;
            // 
            // SecondDegreeCurvesTab
            // 
            SecondDegreeCurvesTab.Controls.Add(CurveParametersGroupBox);
            SecondDegreeCurvesTab.Controls.Add(groupBox4);
            SecondDegreeCurvesTab.Location = new Point(4, 29);
            SecondDegreeCurvesTab.Margin = new Padding(4);
            SecondDegreeCurvesTab.Name = "SecondDegreeCurvesTab";
            SecondDegreeCurvesTab.Padding = new Padding(4);
            SecondDegreeCurvesTab.Size = new Size(1470, 198);
            SecondDegreeCurvesTab.TabIndex = 1;
            SecondDegreeCurvesTab.Text = "Кривые 2-го порядка";
            SecondDegreeCurvesTab.UseVisualStyleBackColor = true;
            // 
            // CurveParametersGroupBox
            // 
            CurveParametersGroupBox.AutoSize = true;
            CurveParametersGroupBox.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            CurveParametersGroupBox.Controls.Add(CurveParametersLayoutPanel);
            CurveParametersGroupBox.Dock = DockStyle.Fill;
            CurveParametersGroupBox.Location = new Point(254, 4);
            CurveParametersGroupBox.Margin = new Padding(4);
            CurveParametersGroupBox.Name = "CurveParametersGroupBox";
            CurveParametersGroupBox.Padding = new Padding(4);
            CurveParametersGroupBox.Size = new Size(1212, 190);
            CurveParametersGroupBox.TabIndex = 7;
            CurveParametersGroupBox.TabStop = false;
            CurveParametersGroupBox.Text = "Параметры";
            // 
            // CurveParametersLayoutPanel
            // 
            CurveParametersLayoutPanel.AutoScroll = true;
            CurveParametersLayoutPanel.AutoSize = true;
            CurveParametersLayoutPanel.Dock = DockStyle.Fill;
            CurveParametersLayoutPanel.Location = new Point(4, 28);
            CurveParametersLayoutPanel.Margin = new Padding(4);
            CurveParametersLayoutPanel.Name = "CurveParametersLayoutPanel";
            CurveParametersLayoutPanel.Size = new Size(1204, 158);
            CurveParametersLayoutPanel.TabIndex = 0;
            // 
            // groupBox4
            // 
            groupBox4.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            groupBox4.Controls.Add(tableLayoutPanel2);
            groupBox4.Dock = DockStyle.Left;
            groupBox4.Location = new Point(4, 4);
            groupBox4.Margin = new Padding(4);
            groupBox4.Name = "groupBox4";
            groupBox4.Padding = new Padding(4);
            groupBox4.Size = new Size(250, 190);
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
            tableLayoutPanel2.Location = new Point(4, 28);
            tableLayoutPanel2.Margin = new Padding(4);
            tableLayoutPanel2.Name = "tableLayoutPanel2";
            tableLayoutPanel2.RowCount = 2;
            tableLayoutPanel2.RowStyles.Add(new RowStyle(SizeType.Percent, 50F));
            tableLayoutPanel2.RowStyles.Add(new RowStyle(SizeType.Percent, 50F));
            tableLayoutPanel2.Size = new Size(242, 158);
            tableLayoutPanel2.TabIndex = 8;
            // 
            // CurveTypeCombobox
            // 
            CurveTypeCombobox.Dock = DockStyle.Fill;
            CurveTypeCombobox.FormattingEnabled = true;
            CurveTypeCombobox.Location = new Point(4, 4);
            CurveTypeCombobox.Margin = new Padding(4);
            CurveTypeCombobox.Name = "CurveTypeCombobox";
            CurveTypeCombobox.Size = new Size(234, 33);
            CurveTypeCombobox.TabIndex = 0;
            CurveTypeCombobox.SelectedIndexChanged += CurveTypeCombobox_SelectedIndexChanged;
            // 
            // DrawCurveButton
            // 
            DrawCurveButton.AutoSize = true;
            DrawCurveButton.Dock = DockStyle.Fill;
            DrawCurveButton.Location = new Point(4, 83);
            DrawCurveButton.Margin = new Padding(4);
            DrawCurveButton.Name = "DrawCurveButton";
            DrawCurveButton.Size = new Size(234, 71);
            DrawCurveButton.TabIndex = 6;
            DrawCurveButton.Text = "Построить";
            DrawCurveButton.UseVisualStyleBackColor = true;
            DrawCurveButton.Click += DrawCurveButton_ClickAsync;
            // 
            // SplinesTab
            // 
            SplinesTab.Controls.Add(groupBox3);
            SplinesTab.Controls.Add(groupBox5);
            SplinesTab.Location = new Point(4, 29);
            SplinesTab.Margin = new Padding(4);
            SplinesTab.Name = "SplinesTab";
            SplinesTab.Padding = new Padding(4);
            SplinesTab.Size = new Size(1470, 198);
            SplinesTab.TabIndex = 2;
            SplinesTab.Text = "Параметрические кривые";
            SplinesTab.UseVisualStyleBackColor = true;
            // 
            // groupBox3
            // 
            groupBox3.AutoSize = true;
            groupBox3.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            groupBox3.Controls.Add(SplineParametersLayoutPanel);
            groupBox3.Dock = DockStyle.Fill;
            groupBox3.Location = new Point(254, 4);
            groupBox3.Margin = new Padding(4);
            groupBox3.Name = "groupBox3";
            groupBox3.Padding = new Padding(4);
            groupBox3.Size = new Size(1212, 190);
            groupBox3.TabIndex = 9;
            groupBox3.TabStop = false;
            groupBox3.Text = "Параметры";
            // 
            // SplineParametersLayoutPanel
            // 
            SplineParametersLayoutPanel.AutoScroll = true;
            SplineParametersLayoutPanel.AutoSize = true;
            SplineParametersLayoutPanel.Dock = DockStyle.Fill;
            SplineParametersLayoutPanel.Location = new Point(4, 28);
            SplineParametersLayoutPanel.Margin = new Padding(4);
            SplineParametersLayoutPanel.Name = "SplineParametersLayoutPanel";
            SplineParametersLayoutPanel.Size = new Size(1204, 158);
            SplineParametersLayoutPanel.TabIndex = 0;
            // 
            // groupBox5
            // 
            groupBox5.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            groupBox5.Controls.Add(tableLayoutPanel3);
            groupBox5.Dock = DockStyle.Left;
            groupBox5.Location = new Point(4, 4);
            groupBox5.Margin = new Padding(4);
            groupBox5.Name = "groupBox5";
            groupBox5.Padding = new Padding(4);
            groupBox5.Size = new Size(250, 190);
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
            tableLayoutPanel3.Location = new Point(4, 28);
            tableLayoutPanel3.Margin = new Padding(4);
            tableLayoutPanel3.Name = "tableLayoutPanel3";
            tableLayoutPanel3.RowCount = 2;
            tableLayoutPanel3.RowStyles.Add(new RowStyle(SizeType.Percent, 50F));
            tableLayoutPanel3.RowStyles.Add(new RowStyle(SizeType.Percent, 50F));
            tableLayoutPanel3.Size = new Size(242, 158);
            tableLayoutPanel3.TabIndex = 9;
            // 
            // DrawSplineButton
            // 
            DrawSplineButton.AutoSize = true;
            DrawSplineButton.Dock = DockStyle.Fill;
            DrawSplineButton.Location = new Point(4, 83);
            DrawSplineButton.Margin = new Padding(4);
            DrawSplineButton.Name = "DrawSplineButton";
            DrawSplineButton.Size = new Size(234, 71);
            DrawSplineButton.TabIndex = 6;
            DrawSplineButton.Text = "Построить";
            DrawSplineButton.UseVisualStyleBackColor = true;
            DrawSplineButton.Click += DrawSplineButton_Click;
            // 
            // SplineTypeCombobox
            // 
            SplineTypeCombobox.Dock = DockStyle.Fill;
            SplineTypeCombobox.FormattingEnabled = true;
            SplineTypeCombobox.Location = new Point(4, 4);
            SplineTypeCombobox.Margin = new Padding(4);
            SplineTypeCombobox.Name = "SplineTypeCombobox";
            SplineTypeCombobox.Size = new Size(234, 33);
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
            PolygonsTab.Margin = new Padding(4);
            PolygonsTab.Name = "PolygonsTab";
            PolygonsTab.Padding = new Padding(4);
            PolygonsTab.Size = new Size(1470, 198);
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
            groupBox8.Location = new Point(270, 4);
            groupBox8.Margin = new Padding(4);
            groupBox8.Name = "groupBox8";
            groupBox8.Padding = new Padding(4);
            groupBox8.Size = new Size(8, 190);
            groupBox8.TabIndex = 12;
            groupBox8.TabStop = false;
            groupBox8.Text = "Пересечение с прямой";
            // 
            // LineIntersectionLayoutPanel
            // 
            LineIntersectionLayoutPanel.AutoSize = true;
            LineIntersectionLayoutPanel.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            LineIntersectionLayoutPanel.Dock = DockStyle.Fill;
            LineIntersectionLayoutPanel.Location = new Point(4, 28);
            LineIntersectionLayoutPanel.Margin = new Padding(4);
            LineIntersectionLayoutPanel.Name = "LineIntersectionLayoutPanel";
            LineIntersectionLayoutPanel.Size = new Size(0, 123);
            LineIntersectionLayoutPanel.TabIndex = 0;
            // 
            // IntersectLineButton
            // 
            IntersectLineButton.AutoSize = true;
            IntersectLineButton.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            IntersectLineButton.Dock = DockStyle.Bottom;
            IntersectLineButton.Location = new Point(4, 151);
            IntersectLineButton.Margin = new Padding(4);
            IntersectLineButton.Name = "IntersectLineButton";
            IntersectLineButton.Size = new Size(0, 35);
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
            groupBox7.Location = new Point(262, 4);
            groupBox7.Margin = new Padding(4);
            groupBox7.Name = "groupBox7";
            groupBox7.Padding = new Padding(4);
            groupBox7.Size = new Size(8, 190);
            groupBox7.TabIndex = 11;
            groupBox7.TabStop = false;
            groupBox7.Text = "Принадлежность точки";
            // 
            // CheckBelongingButton
            // 
            CheckBelongingButton.AutoSize = true;
            CheckBelongingButton.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            CheckBelongingButton.Dock = DockStyle.Bottom;
            CheckBelongingButton.Location = new Point(4, 151);
            CheckBelongingButton.Margin = new Padding(4);
            CheckBelongingButton.Name = "CheckBelongingButton";
            CheckBelongingButton.Size = new Size(0, 35);
            CheckBelongingButton.TabIndex = 8;
            CheckBelongingButton.Text = "Проверить принадлежность";
            CheckBelongingButton.UseVisualStyleBackColor = true;
            CheckBelongingButton.Click += CheckBelongingButton_Click;
            // 
            // PointBelongingLayoutPanel
            // 
            PointBelongingLayoutPanel.AutoScroll = true;
            PointBelongingLayoutPanel.AutoSize = true;
            PointBelongingLayoutPanel.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            PointBelongingLayoutPanel.Dock = DockStyle.Fill;
            PointBelongingLayoutPanel.Location = new Point(4, 28);
            PointBelongingLayoutPanel.Margin = new Padding(4);
            PointBelongingLayoutPanel.Name = "PointBelongingLayoutPanel";
            PointBelongingLayoutPanel.Size = new Size(0, 158);
            PointBelongingLayoutPanel.TabIndex = 0;
            // 
            // PolygonParamsGroupbox
            // 
            PolygonParamsGroupbox.AutoSize = true;
            PolygonParamsGroupbox.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            PolygonParamsGroupbox.Controls.Add(PolygonParametersLayoutPanel);
            PolygonParamsGroupbox.Dock = DockStyle.Left;
            PolygonParamsGroupbox.Location = new Point(254, 4);
            PolygonParamsGroupbox.Margin = new Padding(4);
            PolygonParamsGroupbox.Name = "PolygonParamsGroupbox";
            PolygonParamsGroupbox.Padding = new Padding(4);
            PolygonParamsGroupbox.Size = new Size(8, 190);
            PolygonParamsGroupbox.TabIndex = 10;
            PolygonParamsGroupbox.TabStop = false;
            PolygonParamsGroupbox.Text = "Параметры полигона";
            // 
            // PolygonParametersLayoutPanel
            // 
            PolygonParametersLayoutPanel.AutoSize = true;
            PolygonParametersLayoutPanel.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            PolygonParametersLayoutPanel.Dock = DockStyle.Fill;
            PolygonParametersLayoutPanel.Location = new Point(4, 28);
            PolygonParametersLayoutPanel.Margin = new Padding(4);
            PolygonParametersLayoutPanel.Name = "PolygonParametersLayoutPanel";
            PolygonParametersLayoutPanel.Size = new Size(0, 158);
            PolygonParametersLayoutPanel.TabIndex = 0;
            // 
            // groupBox2
            // 
            groupBox2.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            groupBox2.Controls.Add(tableLayoutPanel4);
            groupBox2.Dock = DockStyle.Left;
            groupBox2.Location = new Point(4, 4);
            groupBox2.Margin = new Padding(4);
            groupBox2.Name = "groupBox2";
            groupBox2.Padding = new Padding(4);
            groupBox2.Size = new Size(250, 190);
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
            tableLayoutPanel4.Location = new Point(4, 28);
            tableLayoutPanel4.Margin = new Padding(4);
            tableLayoutPanel4.Name = "tableLayoutPanel4";
            tableLayoutPanel4.RowCount = 4;
            tableLayoutPanel4.RowStyles.Add(new RowStyle(SizeType.Percent, 25.0006237F));
            tableLayoutPanel4.RowStyles.Add(new RowStyle(SizeType.Percent, 25.0006275F));
            tableLayoutPanel4.RowStyles.Add(new RowStyle(SizeType.Percent, 25.0006237F));
            tableLayoutPanel4.RowStyles.Add(new RowStyle(SizeType.Percent, 24.9981289F));
            tableLayoutPanel4.Size = new Size(242, 158);
            tableLayoutPanel4.TabIndex = 9;
            // 
            // DrawPolygonNormalsButton
            // 
            DrawPolygonNormalsButton.AutoSize = true;
            DrawPolygonNormalsButton.Dock = DockStyle.Fill;
            DrawPolygonNormalsButton.Location = new Point(4, 82);
            DrawPolygonNormalsButton.Margin = new Padding(4);
            DrawPolygonNormalsButton.Name = "DrawPolygonNormalsButton";
            DrawPolygonNormalsButton.Size = new Size(234, 31);
            DrawPolygonNormalsButton.TabIndex = 8;
            DrawPolygonNormalsButton.Text = "Построить нормали";
            DrawPolygonNormalsButton.UseVisualStyleBackColor = true;
            DrawPolygonNormalsButton.Click += DrawPolygonNormalsButton_Click;
            // 
            // CheckConvexButton
            // 
            CheckConvexButton.AutoSize = true;
            CheckConvexButton.Dock = DockStyle.Fill;
            CheckConvexButton.Location = new Point(4, 121);
            CheckConvexButton.Margin = new Padding(4);
            CheckConvexButton.Name = "CheckConvexButton";
            CheckConvexButton.Size = new Size(234, 33);
            CheckConvexButton.TabIndex = 7;
            CheckConvexButton.Text = "Проверка выпуклости";
            CheckConvexButton.UseVisualStyleBackColor = true;
            CheckConvexButton.Click += CheckConvexButton_Click;
            // 
            // DrawPolygonButton
            // 
            DrawPolygonButton.AutoSize = true;
            DrawPolygonButton.Dock = DockStyle.Fill;
            DrawPolygonButton.Location = new Point(4, 43);
            DrawPolygonButton.Margin = new Padding(4);
            DrawPolygonButton.Name = "DrawPolygonButton";
            DrawPolygonButton.Size = new Size(234, 31);
            DrawPolygonButton.TabIndex = 6;
            DrawPolygonButton.Text = "Построить";
            DrawPolygonButton.UseVisualStyleBackColor = true;
            DrawPolygonButton.Click += DrawPolygonButton_Click;
            // 
            // PolygonAlgorithmCombobox
            // 
            PolygonAlgorithmCombobox.Dock = DockStyle.Fill;
            PolygonAlgorithmCombobox.FormattingEnabled = true;
            PolygonAlgorithmCombobox.Location = new Point(4, 4);
            PolygonAlgorithmCombobox.Margin = new Padding(4);
            PolygonAlgorithmCombobox.Name = "PolygonAlgorithmCombobox";
            PolygonAlgorithmCombobox.Size = new Size(234, 33);
            PolygonAlgorithmCombobox.TabIndex = 0;
            // 
            // WorkSpaceSplitContainer
            // 
            WorkSpaceSplitContainer.Dock = DockStyle.Fill;
            WorkSpaceSplitContainer.FixedPanel = FixedPanel.Panel2;
            WorkSpaceSplitContainer.Location = new Point(0, 0);
            WorkSpaceSplitContainer.Margin = new Padding(4);
            WorkSpaceSplitContainer.Name = "WorkSpaceSplitContainer";
            // 
            // WorkSpaceSplitContainer.Panel1
            // 
            WorkSpaceSplitContainer.Panel1.AutoScroll = true;
            WorkSpaceSplitContainer.Panel1.AutoScrollMinSize = new Size(550, 550);
            WorkSpaceSplitContainer.Panel1.BackColor = SystemColors.ControlDark;
            WorkSpaceSplitContainer.Panel1.Controls.Add(CanvasPictureBox);
            // 
            // WorkSpaceSplitContainer.Panel2
            // 
            WorkSpaceSplitContainer.Panel2.Controls.Add(panel1);
            WorkSpaceSplitContainer.Panel2.Controls.Add(DebugGridView);
            WorkSpaceSplitContainer.Size = new Size(1478, 705);
            WorkSpaceSplitContainer.SplitterDistance = 1059;
            WorkSpaceSplitContainer.SplitterWidth = 5;
            WorkSpaceSplitContainer.TabIndex = 0;
            // 
            // CanvasPictureBox
            // 
            CanvasPictureBox.Anchor = AnchorStyles.None;
            CanvasPictureBox.BackColor = Color.White;
            CanvasPictureBox.BorderStyle = BorderStyle.FixedSingle;
            CanvasPictureBox.Cursor = Cursors.Cross;
            CanvasPictureBox.Image = (Image)resources.GetObject("CanvasPictureBox.Image");
            CanvasPictureBox.Location = new Point(229, 31);
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
            panel1.Name = "panel1";
            panel1.Size = new Size(414, 40);
            panel1.TabIndex = 4;
            // 
            // EnableDebugButton
            // 
            EnableDebugButton.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left;
            EnableDebugButton.AutoSize = true;
            EnableDebugButton.Location = new Point(6, 6);
            EnableDebugButton.Margin = new Padding(4);
            EnableDebugButton.Name = "EnableDebugButton";
            EnableDebugButton.Size = new Size(163, 29);
            EnableDebugButton.TabIndex = 0;
            EnableDebugButton.Text = "Режим отладки";
            EnableDebugButton.UseVisualStyleBackColor = true;
            // 
            // button2
            // 
            button2.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Right;
            button2.Location = new Point(218, 3);
            button2.Margin = new Padding(4);
            button2.Name = "button2";
            button2.Size = new Size(196, 36);
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
            DebugGridView.Location = new Point(0, 43);
            DebugGridView.Margin = new Padding(0);
            DebugGridView.Name = "DebugGridView";
            DebugGridView.RowHeadersWidth = 51;
            DebugGridView.Size = new Size(404, 662);
            DebugGridView.TabIndex = 3;
            // 
            // groupBox9
            // 
            groupBox9.AutoSize = true;
            groupBox9.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            groupBox9.Controls.Add(CommonParametersLayoutPanel);
            groupBox9.Dock = DockStyle.Fill;
            groupBox9.Location = new Point(3, 3);
            groupBox9.Margin = new Padding(4);
            groupBox9.Name = "groupBox9";
            groupBox9.Padding = new Padding(4);
            groupBox9.Size = new Size(1464, 192);
            groupBox9.TabIndex = 8;
            groupBox9.TabStop = false;
            groupBox9.Text = "Параметры";
            // 
            // CommonParametersLayoutPanel
            // 
            CommonParametersLayoutPanel.AutoScroll = true;
            CommonParametersLayoutPanel.AutoSize = true;
            CommonParametersLayoutPanel.Dock = DockStyle.Fill;
            CommonParametersLayoutPanel.Location = new Point(4, 28);
            CommonParametersLayoutPanel.Margin = new Padding(4);
            CommonParametersLayoutPanel.Name = "CommonParametersLayoutPanel";
            CommonParametersLayoutPanel.Size = new Size(1456, 160);
            CommonParametersLayoutPanel.TabIndex = 0;
            // 
            // MainForm
            // 
            AutoScaleDimensions = new SizeF(10F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(1478, 941);
            Controls.Add(FormSplitContainer);
            Margin = new Padding(4);
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
            WorkSpaceSplitContainer.Panel1.ResumeLayout(false);
            WorkSpaceSplitContainer.Panel2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)WorkSpaceSplitContainer).EndInit();
            WorkSpaceSplitContainer.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)CanvasPictureBox).EndInit();
            panel1.ResumeLayout(false);
            panel1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)DebugGridView).EndInit();
            groupBox9.ResumeLayout(false);
            groupBox9.PerformLayout();
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
    }
}

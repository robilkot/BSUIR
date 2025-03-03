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
            FormSplitContainer = new SplitContainer();
            InstrumentCluster = new TabControl();
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
            PolygonsPage = new TabPage();
            PolygonParamsGroupbox = new GroupBox();
            PolygonParametersLayoutPanel = new FlowLayoutPanel();
            groupBox2 = new GroupBox();
            tableLayoutPanel4 = new TableLayoutPanel();
            DrawPolygonButton = new Button();
            PolygonAlgorithmCombobox = new ComboBox();
            WorkSpaceSplitContainer = new SplitContainer();
            CanvasPictureBox = new View.Canvas();
            DebugGridView = new DataGridView();
            button2 = new Button();
            EnableDebugButton = new CheckBox();
            ((System.ComponentModel.ISupportInitialize)FormSplitContainer).BeginInit();
            FormSplitContainer.Panel1.SuspendLayout();
            FormSplitContainer.Panel2.SuspendLayout();
            FormSplitContainer.SuspendLayout();
            InstrumentCluster.SuspendLayout();
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
            PolygonsPage.SuspendLayout();
            PolygonParamsGroupbox.SuspendLayout();
            groupBox2.SuspendLayout();
            tableLayoutPanel4.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)WorkSpaceSplitContainer).BeginInit();
            WorkSpaceSplitContainer.Panel1.SuspendLayout();
            WorkSpaceSplitContainer.Panel2.SuspendLayout();
            WorkSpaceSplitContainer.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)CanvasPictureBox).BeginInit();
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
            InstrumentCluster.Controls.Add(LinesTab);
            InstrumentCluster.Controls.Add(SecondDegreeCurvesTab);
            InstrumentCluster.Controls.Add(SplinesTab);
            InstrumentCluster.Controls.Add(PolygonsPage);
            InstrumentCluster.Dock = DockStyle.Fill;
            InstrumentCluster.ItemSize = new Size(150, 25);
            InstrumentCluster.Location = new Point(0, 0);
            InstrumentCluster.Name = "InstrumentCluster";
            InstrumentCluster.SelectedIndex = 0;
            InstrumentCluster.Size = new Size(1182, 185);
            InstrumentCluster.TabIndex = 0;
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
            LineParametersLayoutPanel.AutoScroll = true;
            LineParametersLayoutPanel.AutoSize = true;
            LineParametersLayoutPanel.Dock = DockStyle.Fill;
            LineParametersLayoutPanel.FlowDirection = FlowDirection.TopDown;
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
            CurveParametersGroupBox.Dock = DockStyle.Fill;
            CurveParametersGroupBox.Location = new Point(203, 3);
            CurveParametersGroupBox.Name = "CurveParametersGroupBox";
            CurveParametersGroupBox.Size = new Size(968, 146);
            CurveParametersGroupBox.TabIndex = 7;
            CurveParametersGroupBox.TabStop = false;
            CurveParametersGroupBox.Text = "Параметры";
            // 
            // CurveParametersLayoutPanel
            // 
            CurveParametersLayoutPanel.AutoScroll = true;
            CurveParametersLayoutPanel.AutoSize = true;
            CurveParametersLayoutPanel.Dock = DockStyle.Fill;
            CurveParametersLayoutPanel.FlowDirection = FlowDirection.TopDown;
            CurveParametersLayoutPanel.Location = new Point(3, 23);
            CurveParametersLayoutPanel.Name = "CurveParametersLayoutPanel";
            CurveParametersLayoutPanel.Size = new Size(962, 120);
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
            groupBox3.Dock = DockStyle.Fill;
            groupBox3.Location = new Point(203, 3);
            groupBox3.Name = "groupBox3";
            groupBox3.Size = new Size(968, 146);
            groupBox3.TabIndex = 9;
            groupBox3.TabStop = false;
            groupBox3.Text = "Параметры";
            // 
            // SplineParametersLayoutPanel
            // 
            SplineParametersLayoutPanel.AutoScroll = true;
            SplineParametersLayoutPanel.AutoSize = true;
            SplineParametersLayoutPanel.Dock = DockStyle.Fill;
            SplineParametersLayoutPanel.FlowDirection = FlowDirection.TopDown;
            SplineParametersLayoutPanel.Location = new Point(3, 23);
            SplineParametersLayoutPanel.Name = "SplineParametersLayoutPanel";
            SplineParametersLayoutPanel.Size = new Size(962, 120);
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
            // PolygonsPage
            // 
            PolygonsPage.Controls.Add(PolygonParamsGroupbox);
            PolygonsPage.Controls.Add(groupBox2);
            PolygonsPage.Location = new Point(4, 29);
            PolygonsPage.Name = "PolygonsPage";
            PolygonsPage.Padding = new Padding(3);
            PolygonsPage.Size = new Size(1174, 152);
            PolygonsPage.TabIndex = 3;
            PolygonsPage.Text = "Полигоны";
            PolygonsPage.UseVisualStyleBackColor = true;
            // 
            // PolygonParamsGroupbox
            // 
            PolygonParamsGroupbox.AutoSize = true;
            PolygonParamsGroupbox.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            PolygonParamsGroupbox.Controls.Add(PolygonParametersLayoutPanel);
            PolygonParamsGroupbox.Dock = DockStyle.Fill;
            PolygonParamsGroupbox.Location = new Point(203, 3);
            PolygonParamsGroupbox.Name = "PolygonParamsGroupbox";
            PolygonParamsGroupbox.Size = new Size(968, 146);
            PolygonParamsGroupbox.TabIndex = 10;
            PolygonParamsGroupbox.TabStop = false;
            PolygonParamsGroupbox.Text = "Параметры полигона";
            // 
            // PolygonParametersLayoutPanel
            // 
            PolygonParametersLayoutPanel.AutoScroll = true;
            PolygonParametersLayoutPanel.AutoSize = true;
            PolygonParametersLayoutPanel.Dock = DockStyle.Fill;
            PolygonParametersLayoutPanel.FlowDirection = FlowDirection.TopDown;
            PolygonParametersLayoutPanel.Location = new Point(3, 23);
            PolygonParametersLayoutPanel.Name = "PolygonParametersLayoutPanel";
            PolygonParametersLayoutPanel.Size = new Size(962, 120);
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
            tableLayoutPanel4.Controls.Add(DrawPolygonButton, 0, 1);
            tableLayoutPanel4.Controls.Add(PolygonAlgorithmCombobox, 0, 0);
            tableLayoutPanel4.Dock = DockStyle.Fill;
            tableLayoutPanel4.GrowStyle = TableLayoutPanelGrowStyle.FixedSize;
            tableLayoutPanel4.Location = new Point(3, 23);
            tableLayoutPanel4.Name = "tableLayoutPanel4";
            tableLayoutPanel4.RowCount = 2;
            tableLayoutPanel4.RowStyles.Add(new RowStyle(SizeType.Percent, 50F));
            tableLayoutPanel4.RowStyles.Add(new RowStyle(SizeType.Percent, 50F));
            tableLayoutPanel4.Size = new Size(194, 120);
            tableLayoutPanel4.TabIndex = 9;
            // 
            // DrawPolygonButton
            // 
            DrawPolygonButton.AutoSize = true;
            DrawPolygonButton.Dock = DockStyle.Fill;
            DrawPolygonButton.Location = new Point(3, 63);
            DrawPolygonButton.Name = "DrawPolygonButton";
            DrawPolygonButton.Size = new Size(188, 54);
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
            WorkSpaceSplitContainer.Panel1.AutoScrollMinSize = new Size(550, 550);
            WorkSpaceSplitContainer.Panel1.BackColor = SystemColors.ControlDark;
            WorkSpaceSplitContainer.Panel1.Controls.Add(CanvasPictureBox);
            // 
            // WorkSpaceSplitContainer.Panel2
            // 
            WorkSpaceSplitContainer.Panel2.Controls.Add(DebugGridView);
            WorkSpaceSplitContainer.Panel2.Controls.Add(button2);
            WorkSpaceSplitContainer.Panel2.Controls.Add(EnableDebugButton);
            WorkSpaceSplitContainer.Size = new Size(1182, 564);
            WorkSpaceSplitContainer.SplitterDistance = 736;
            WorkSpaceSplitContainer.TabIndex = 0;
            // 
            // CanvasPictureBox
            // 
            CanvasPictureBox.Anchor = AnchorStyles.None;
            CanvasPictureBox.BackColor = Color.White;
            CanvasPictureBox.BorderStyle = BorderStyle.FixedSingle;
            CanvasPictureBox.Location = new Point(115, 21);
            CanvasPictureBox.Margin = new Padding(2);
            CanvasPictureBox.Name = "CanvasPictureBox";
            CanvasPictureBox.Size = new Size(512, 512);
            CanvasPictureBox.TabIndex = 1;
            CanvasPictureBox.TabStop = false;
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
            DebugGridView.Size = new Size(436, 530);
            DebugGridView.TabIndex = 3;
            // 
            // button2
            // 
            button2.Anchor = AnchorStyles.Top | AnchorStyles.Right;
            button2.Location = new Point(273, 2);
            button2.Name = "button2";
            button2.Size = new Size(157, 29);
            button2.TabIndex = 2;
            button2.Text = "Очистить все";
            button2.UseVisualStyleBackColor = true;
            button2.Click += ClearAll_Click;
            // 
            // EnableDebugButton
            // 
            EnableDebugButton.AutoSize = true;
            EnableDebugButton.Location = new Point(5, 5);
            EnableDebugButton.Name = "EnableDebugButton";
            EnableDebugButton.Size = new Size(137, 24);
            EnableDebugButton.TabIndex = 0;
            EnableDebugButton.Text = "Режим отладки";
            EnableDebugButton.UseVisualStyleBackColor = true;
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
            PolygonsPage.ResumeLayout(false);
            PolygonsPage.PerformLayout();
            PolygonParamsGroupbox.ResumeLayout(false);
            PolygonParamsGroupbox.PerformLayout();
            groupBox2.ResumeLayout(false);
            groupBox2.PerformLayout();
            tableLayoutPanel4.ResumeLayout(false);
            tableLayoutPanel4.PerformLayout();
            WorkSpaceSplitContainer.Panel1.ResumeLayout(false);
            WorkSpaceSplitContainer.Panel2.ResumeLayout(false);
            WorkSpaceSplitContainer.Panel2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)WorkSpaceSplitContainer).EndInit();
            WorkSpaceSplitContainer.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)CanvasPictureBox).EndInit();
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
        private TabPage PolygonsPage;
        private GroupBox PolygonParamsGroupbox;
        private FlowLayoutPanel PolygonParametersLayoutPanel;
        private GroupBox groupBox2;
        private TableLayoutPanel tableLayoutPanel4;
        private Button DrawPolygonButton;
        private ComboBox PolygonAlgorithmCombobox;
    }
}

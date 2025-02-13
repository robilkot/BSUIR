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
            groupBox2 = new GroupBox();
            DrawLineButton = new Button();
            LineDrawingAlgorithmCombobox = new ComboBox();
            SecondDegreeCurvesTab = new TabPage();
            CurveParametersGroupBox = new GroupBox();
            CurveParametersLayoutPanel = new FlowLayoutPanel();
            groupBox4 = new GroupBox();
            DrawCurveButton = new Button();
            CurveTypeCombobox = new ComboBox();
            SplinesTab = new TabPage();
            groupBox3 = new GroupBox();
            SplineParametersLayoutPanel = new FlowLayoutPanel();
            groupBox5 = new GroupBox();
            DrawSplineButton = new Button();
            SplineTypeCombobox = new ComboBox();
            WorkSpaceSplitContainer = new SplitContainer();
            CanvasPictureBox = new PictureBox();
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
            groupBox2.SuspendLayout();
            SecondDegreeCurvesTab.SuspendLayout();
            CurveParametersGroupBox.SuspendLayout();
            groupBox4.SuspendLayout();
            SplinesTab.SuspendLayout();
            groupBox3.SuspendLayout();
            groupBox5.SuspendLayout();
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
            FormSplitContainer.IsSplitterFixed = true;
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
            FormSplitContainer.SplitterDistance = 198;
            FormSplitContainer.SplitterWidth = 5;
            FormSplitContainer.TabIndex = 0;
            // 
            // InstrumentCluster
            // 
            InstrumentCluster.Controls.Add(LinesTab);
            InstrumentCluster.Controls.Add(SecondDegreeCurvesTab);
            InstrumentCluster.Controls.Add(SplinesTab);
            InstrumentCluster.Dock = DockStyle.Fill;
            InstrumentCluster.ItemSize = new Size(150, 25);
            InstrumentCluster.Location = new Point(0, 0);
            InstrumentCluster.Margin = new Padding(4);
            InstrumentCluster.Name = "InstrumentCluster";
            InstrumentCluster.SelectedIndex = 0;
            InstrumentCluster.Size = new Size(1478, 198);
            InstrumentCluster.TabIndex = 0;
            // 
            // LinesTab
            // 
            LinesTab.AutoScroll = true;
            LinesTab.Controls.Add(groupBox1);
            LinesTab.Controls.Add(groupBox2);
            LinesTab.Location = new Point(4, 29);
            LinesTab.Margin = new Padding(4);
            LinesTab.Name = "LinesTab";
            LinesTab.Padding = new Padding(4);
            LinesTab.Size = new Size(1470, 165);
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
            groupBox1.Location = new Point(250, 4);
            groupBox1.Margin = new Padding(4);
            groupBox1.Name = "groupBox1";
            groupBox1.Padding = new Padding(4);
            groupBox1.Size = new Size(1216, 157);
            groupBox1.TabIndex = 9;
            groupBox1.TabStop = false;
            groupBox1.Text = "Параметры отрезка";
            // 
            // LineParametersLayoutPanel
            // 
            LineParametersLayoutPanel.AutoSize = true;
            LineParametersLayoutPanel.Dock = DockStyle.Fill;
            LineParametersLayoutPanel.FlowDirection = FlowDirection.TopDown;
            LineParametersLayoutPanel.Location = new Point(4, 28);
            LineParametersLayoutPanel.Margin = new Padding(4);
            LineParametersLayoutPanel.Name = "LineParametersLayoutPanel";
            LineParametersLayoutPanel.Size = new Size(1208, 125);
            LineParametersLayoutPanel.TabIndex = 0;
            // 
            // groupBox2
            // 
            groupBox2.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            groupBox2.Controls.Add(DrawLineButton);
            groupBox2.Controls.Add(LineDrawingAlgorithmCombobox);
            groupBox2.Dock = DockStyle.Left;
            groupBox2.Location = new Point(4, 4);
            groupBox2.Margin = new Padding(4);
            groupBox2.Name = "groupBox2";
            groupBox2.Padding = new Padding(4);
            groupBox2.Size = new Size(246, 157);
            groupBox2.TabIndex = 8;
            groupBox2.TabStop = false;
            groupBox2.Text = "Алгоритм построения";
            // 
            // DrawLineButton
            // 
            DrawLineButton.Anchor = AnchorStyles.Left;
            DrawLineButton.Location = new Point(26, 96);
            DrawLineButton.Margin = new Padding(4);
            DrawLineButton.Name = "DrawLineButton";
            DrawLineButton.Size = new Size(194, 36);
            DrawLineButton.TabIndex = 6;
            DrawLineButton.Text = "Построить";
            DrawLineButton.UseVisualStyleBackColor = true;
            DrawLineButton.Click += DrawLineButton_Click;
            // 
            // LineDrawingAlgorithmCombobox
            // 
            LineDrawingAlgorithmCombobox.FormattingEnabled = true;
            LineDrawingAlgorithmCombobox.Location = new Point(26, 39);
            LineDrawingAlgorithmCombobox.Margin = new Padding(4);
            LineDrawingAlgorithmCombobox.Name = "LineDrawingAlgorithmCombobox";
            LineDrawingAlgorithmCombobox.Size = new Size(193, 33);
            LineDrawingAlgorithmCombobox.TabIndex = 0;
            // 
            // SecondDegreeCurvesTab
            // 
            SecondDegreeCurvesTab.Controls.Add(CurveParametersGroupBox);
            SecondDegreeCurvesTab.Controls.Add(groupBox4);
            SecondDegreeCurvesTab.Location = new Point(4, 29);
            SecondDegreeCurvesTab.Margin = new Padding(4);
            SecondDegreeCurvesTab.Name = "SecondDegreeCurvesTab";
            SecondDegreeCurvesTab.Padding = new Padding(4);
            SecondDegreeCurvesTab.Size = new Size(1468, 163);
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
            CurveParametersGroupBox.Location = new Point(250, 4);
            CurveParametersGroupBox.Margin = new Padding(4);
            CurveParametersGroupBox.Name = "CurveParametersGroupBox";
            CurveParametersGroupBox.Padding = new Padding(4);
            CurveParametersGroupBox.Size = new Size(1214, 155);
            CurveParametersGroupBox.TabIndex = 7;
            CurveParametersGroupBox.TabStop = false;
            CurveParametersGroupBox.Text = "Параметры";
            // 
            // CurveParametersLayoutPanel
            // 
            CurveParametersLayoutPanel.AutoSize = true;
            CurveParametersLayoutPanel.Dock = DockStyle.Fill;
            CurveParametersLayoutPanel.FlowDirection = FlowDirection.TopDown;
            CurveParametersLayoutPanel.Location = new Point(4, 28);
            CurveParametersLayoutPanel.Margin = new Padding(4);
            CurveParametersLayoutPanel.Name = "CurveParametersLayoutPanel";
            CurveParametersLayoutPanel.Size = new Size(1206, 123);
            CurveParametersLayoutPanel.TabIndex = 0;
            // 
            // groupBox4
            // 
            groupBox4.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            groupBox4.Controls.Add(DrawCurveButton);
            groupBox4.Controls.Add(CurveTypeCombobox);
            groupBox4.Dock = DockStyle.Left;
            groupBox4.Location = new Point(4, 4);
            groupBox4.Margin = new Padding(4);
            groupBox4.Name = "groupBox4";
            groupBox4.Padding = new Padding(4);
            groupBox4.Size = new Size(246, 155);
            groupBox4.TabIndex = 3;
            groupBox4.TabStop = false;
            groupBox4.Text = "Тип";
            // 
            // DrawCurveButton
            // 
            DrawCurveButton.Anchor = AnchorStyles.Left;
            DrawCurveButton.Location = new Point(26, 97);
            DrawCurveButton.Margin = new Padding(4);
            DrawCurveButton.Name = "DrawCurveButton";
            DrawCurveButton.Size = new Size(194, 36);
            DrawCurveButton.TabIndex = 6;
            DrawCurveButton.Text = "Построить";
            DrawCurveButton.UseVisualStyleBackColor = true;
            DrawCurveButton.Click += DrawCurveButton_ClickAsync;
            // 
            // CurveTypeCombobox
            // 
            CurveTypeCombobox.FormattingEnabled = true;
            CurveTypeCombobox.Location = new Point(26, 39);
            CurveTypeCombobox.Margin = new Padding(4);
            CurveTypeCombobox.Name = "CurveTypeCombobox";
            CurveTypeCombobox.Size = new Size(193, 33);
            CurveTypeCombobox.TabIndex = 0;
            CurveTypeCombobox.SelectedIndexChanged += CurveTypeCombobox_SelectedIndexChanged;
            // 
            // SplinesTab
            // 
            SplinesTab.Controls.Add(groupBox3);
            SplinesTab.Controls.Add(groupBox5);
            SplinesTab.Location = new Point(4, 29);
            SplinesTab.Margin = new Padding(4);
            SplinesTab.Name = "SplinesTab";
            SplinesTab.Padding = new Padding(4);
            SplinesTab.Size = new Size(1468, 163);
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
            groupBox3.Location = new Point(250, 4);
            groupBox3.Margin = new Padding(4);
            groupBox3.Name = "groupBox3";
            groupBox3.Padding = new Padding(4);
            groupBox3.Size = new Size(1214, 155);
            groupBox3.TabIndex = 9;
            groupBox3.TabStop = false;
            groupBox3.Text = "Параметры";
            // 
            // SplineParametersLayoutPanel
            // 
            SplineParametersLayoutPanel.AutoSize = true;
            SplineParametersLayoutPanel.Dock = DockStyle.Fill;
            SplineParametersLayoutPanel.FlowDirection = FlowDirection.TopDown;
            SplineParametersLayoutPanel.Location = new Point(4, 28);
            SplineParametersLayoutPanel.Margin = new Padding(4);
            SplineParametersLayoutPanel.Name = "SplineParametersLayoutPanel";
            SplineParametersLayoutPanel.Size = new Size(1206, 123);
            SplineParametersLayoutPanel.TabIndex = 0;
            // 
            // groupBox5
            // 
            groupBox5.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            groupBox5.Controls.Add(DrawSplineButton);
            groupBox5.Controls.Add(SplineTypeCombobox);
            groupBox5.Dock = DockStyle.Left;
            groupBox5.Location = new Point(4, 4);
            groupBox5.Margin = new Padding(4);
            groupBox5.Name = "groupBox5";
            groupBox5.Padding = new Padding(4);
            groupBox5.Size = new Size(246, 155);
            groupBox5.TabIndex = 8;
            groupBox5.TabStop = false;
            groupBox5.Text = "Тип";
            // 
            // DrawSplineButton
            // 
            DrawSplineButton.Anchor = AnchorStyles.Left;
            DrawSplineButton.Location = new Point(26, 95);
            DrawSplineButton.Margin = new Padding(4);
            DrawSplineButton.Name = "DrawSplineButton";
            DrawSplineButton.Size = new Size(194, 36);
            DrawSplineButton.TabIndex = 6;
            DrawSplineButton.Text = "Построить";
            DrawSplineButton.UseVisualStyleBackColor = true;
            DrawSplineButton.Click += DrawSplineButton_Click;
            // 
            // SplineTypeCombobox
            // 
            SplineTypeCombobox.FormattingEnabled = true;
            SplineTypeCombobox.Location = new Point(26, 39);
            SplineTypeCombobox.Margin = new Padding(4);
            SplineTypeCombobox.Name = "SplineTypeCombobox";
            SplineTypeCombobox.Size = new Size(193, 33);
            SplineTypeCombobox.TabIndex = 0;
            SplineTypeCombobox.SelectedIndexChanged += SplineTypeCombobox_SelectedIndexChanged;
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
            WorkSpaceSplitContainer.Panel2.Controls.Add(DebugGridView);
            WorkSpaceSplitContainer.Panel2.Controls.Add(button2);
            WorkSpaceSplitContainer.Panel2.Controls.Add(EnableDebugButton);
            WorkSpaceSplitContainer.Size = new Size(1478, 738);
            WorkSpaceSplitContainer.SplitterDistance = 922;
            WorkSpaceSplitContainer.SplitterWidth = 5;
            WorkSpaceSplitContainer.TabIndex = 0;
            // 
            // CanvasPictureBox
            // 
            CanvasPictureBox.Anchor = AnchorStyles.None;
            CanvasPictureBox.BackColor = Color.White;
            CanvasPictureBox.BorderStyle = BorderStyle.FixedSingle;
            CanvasPictureBox.Location = new Point(134, 50);
            CanvasPictureBox.Margin = new Padding(4);
            CanvasPictureBox.Name = "CanvasPictureBox";
            CanvasPictureBox.Size = new Size(640, 640);
            CanvasPictureBox.TabIndex = 0;
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
            DebugGridView.Location = new Point(0, 43);
            DebugGridView.Margin = new Padding(0);
            DebugGridView.Name = "DebugGridView";
            DebugGridView.RowHeadersWidth = 51;
            DebugGridView.Size = new Size(546, 695);
            DebugGridView.TabIndex = 3;
            // 
            // button2
            // 
            button2.Anchor = AnchorStyles.Top | AnchorStyles.Right;
            button2.Location = new Point(342, 2);
            button2.Margin = new Padding(4);
            button2.Name = "button2";
            button2.Size = new Size(196, 36);
            button2.TabIndex = 2;
            button2.Text = "Очистить все";
            button2.UseVisualStyleBackColor = true;
            button2.Click += ClearAll_Click;
            // 
            // EnableDebugButton
            // 
            EnableDebugButton.AutoSize = true;
            EnableDebugButton.Location = new Point(6, 6);
            EnableDebugButton.Margin = new Padding(4);
            EnableDebugButton.Name = "EnableDebugButton";
            EnableDebugButton.Size = new Size(163, 29);
            EnableDebugButton.TabIndex = 0;
            EnableDebugButton.Text = "Режим отладки";
            EnableDebugButton.UseVisualStyleBackColor = true;
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
            LinesTab.ResumeLayout(false);
            LinesTab.PerformLayout();
            groupBox1.ResumeLayout(false);
            groupBox1.PerformLayout();
            groupBox2.ResumeLayout(false);
            SecondDegreeCurvesTab.ResumeLayout(false);
            SecondDegreeCurvesTab.PerformLayout();
            CurveParametersGroupBox.ResumeLayout(false);
            CurveParametersGroupBox.PerformLayout();
            groupBox4.ResumeLayout(false);
            SplinesTab.ResumeLayout(false);
            SplinesTab.PerformLayout();
            groupBox3.ResumeLayout(false);
            groupBox3.PerformLayout();
            groupBox5.ResumeLayout(false);
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
        private PictureBox CanvasPictureBox;
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
        private GroupBox groupBox2;
        private Button DrawLineButton;
        private ComboBox LineDrawingAlgorithmCombobox;
        private TabPage SplinesTab;
        private GroupBox groupBox3;
        private FlowLayoutPanel SplineParametersLayoutPanel;
        private GroupBox groupBox5;
        private Button DrawSplineButton;
        private ComboBox SplineTypeCombobox;
    }
}

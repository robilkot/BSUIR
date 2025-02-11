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
            splitContainer1 = new SplitContainer();
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
            splitContainer2 = new SplitContainer();
            CanvasPictureBox = new PictureBox();
            DebugGridView = new DataGridView();
            button2 = new Button();
            EnableDebugButton = new CheckBox();
            groupBox3 = new GroupBox();
            SplineParametersLayoutPanel = new FlowLayoutPanel();
            groupBox5 = new GroupBox();
            DrawSplineButton = new Button();
            SplineTypeCombobox = new ComboBox();
            ((System.ComponentModel.ISupportInitialize)splitContainer1).BeginInit();
            splitContainer1.Panel1.SuspendLayout();
            splitContainer1.Panel2.SuspendLayout();
            splitContainer1.SuspendLayout();
            InstrumentCluster.SuspendLayout();
            LinesTab.SuspendLayout();
            groupBox1.SuspendLayout();
            groupBox2.SuspendLayout();
            SecondDegreeCurvesTab.SuspendLayout();
            CurveParametersGroupBox.SuspendLayout();
            groupBox4.SuspendLayout();
            SplinesTab.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)splitContainer2).BeginInit();
            splitContainer2.Panel1.SuspendLayout();
            splitContainer2.Panel2.SuspendLayout();
            splitContainer2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)CanvasPictureBox).BeginInit();
            ((System.ComponentModel.ISupportInitialize)DebugGridView).BeginInit();
            groupBox3.SuspendLayout();
            groupBox5.SuspendLayout();
            SuspendLayout();
            // 
            // splitContainer1
            // 
            splitContainer1.Dock = DockStyle.Fill;
            splitContainer1.FixedPanel = FixedPanel.Panel1;
            splitContainer1.Location = new Point(0, 0);
            splitContainer1.Name = "splitContainer1";
            splitContainer1.Orientation = Orientation.Horizontal;
            // 
            // splitContainer1.Panel1
            // 
            splitContainer1.Panel1.Controls.Add(InstrumentCluster);
            // 
            // splitContainer1.Panel2
            // 
            splitContainer1.Panel2.Controls.Add(splitContainer2);
            splitContainer1.Size = new Size(1182, 753);
            splitContainer1.SplitterDistance = 158;
            splitContainer1.TabIndex = 0;
            // 
            // InstrumentCluster
            // 
            InstrumentCluster.Controls.Add(LinesTab);
            InstrumentCluster.Controls.Add(SecondDegreeCurvesTab);
            InstrumentCluster.Controls.Add(SplinesTab);
            InstrumentCluster.Dock = DockStyle.Fill;
            InstrumentCluster.ItemSize = new Size(150, 25);
            InstrumentCluster.Location = new Point(0, 0);
            InstrumentCluster.Name = "InstrumentCluster";
            InstrumentCluster.SelectedIndex = 0;
            InstrumentCluster.Size = new Size(1182, 158);
            InstrumentCluster.TabIndex = 0;
            // 
            // LinesTab
            // 
            LinesTab.AutoScroll = true;
            LinesTab.Controls.Add(groupBox1);
            LinesTab.Controls.Add(groupBox2);
            LinesTab.Location = new Point(4, 29);
            LinesTab.Name = "LinesTab";
            LinesTab.Padding = new Padding(3);
            LinesTab.Size = new Size(1174, 125);
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
            groupBox1.Location = new Point(200, 3);
            groupBox1.Name = "groupBox1";
            groupBox1.Size = new Size(971, 119);
            groupBox1.TabIndex = 9;
            groupBox1.TabStop = false;
            groupBox1.Text = "Параметры отрезка";
            // 
            // LineParametersLayoutPanel
            // 
            LineParametersLayoutPanel.AutoSize = true;
            LineParametersLayoutPanel.Dock = DockStyle.Fill;
            LineParametersLayoutPanel.FlowDirection = FlowDirection.TopDown;
            LineParametersLayoutPanel.Location = new Point(3, 23);
            LineParametersLayoutPanel.Name = "LineParametersLayoutPanel";
            LineParametersLayoutPanel.Size = new Size(965, 93);
            LineParametersLayoutPanel.TabIndex = 0;
            // 
            // groupBox2
            // 
            groupBox2.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            groupBox2.Controls.Add(DrawLineButton);
            groupBox2.Controls.Add(LineDrawingAlgorithmCombobox);
            groupBox2.Dock = DockStyle.Left;
            groupBox2.Location = new Point(3, 3);
            groupBox2.Name = "groupBox2";
            groupBox2.Size = new Size(197, 119);
            groupBox2.TabIndex = 8;
            groupBox2.TabStop = false;
            groupBox2.Text = "Алгоритм построения";
            // 
            // DrawLineButton
            // 
            DrawLineButton.Anchor = AnchorStyles.Left;
            DrawLineButton.Location = new Point(21, 74);
            DrawLineButton.Name = "DrawLineButton";
            DrawLineButton.Size = new Size(155, 29);
            DrawLineButton.TabIndex = 6;
            DrawLineButton.Text = "Построить";
            DrawLineButton.UseVisualStyleBackColor = true;
            DrawLineButton.Click += DrawLineButton_Click;
            // 
            // LineDrawingAlgorithmCombobox
            // 
            LineDrawingAlgorithmCombobox.FormattingEnabled = true;
            LineDrawingAlgorithmCombobox.Location = new Point(21, 31);
            LineDrawingAlgorithmCombobox.Name = "LineDrawingAlgorithmCombobox";
            LineDrawingAlgorithmCombobox.Size = new Size(155, 28);
            LineDrawingAlgorithmCombobox.TabIndex = 0;
            // 
            // SecondDegreeCurvesTab
            // 
            SecondDegreeCurvesTab.Controls.Add(CurveParametersGroupBox);
            SecondDegreeCurvesTab.Controls.Add(groupBox4);
            SecondDegreeCurvesTab.Location = new Point(4, 29);
            SecondDegreeCurvesTab.Name = "SecondDegreeCurvesTab";
            SecondDegreeCurvesTab.Padding = new Padding(3);
            SecondDegreeCurvesTab.Size = new Size(1174, 125);
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
            CurveParametersGroupBox.Location = new Point(200, 3);
            CurveParametersGroupBox.Name = "CurveParametersGroupBox";
            CurveParametersGroupBox.Size = new Size(971, 119);
            CurveParametersGroupBox.TabIndex = 7;
            CurveParametersGroupBox.TabStop = false;
            CurveParametersGroupBox.Text = "Параметры";
            // 
            // CurveParametersLayoutPanel
            // 
            CurveParametersLayoutPanel.AutoSize = true;
            CurveParametersLayoutPanel.Dock = DockStyle.Fill;
            CurveParametersLayoutPanel.FlowDirection = FlowDirection.TopDown;
            CurveParametersLayoutPanel.Location = new Point(3, 23);
            CurveParametersLayoutPanel.Name = "CurveParametersLayoutPanel";
            CurveParametersLayoutPanel.Size = new Size(965, 93);
            CurveParametersLayoutPanel.TabIndex = 0;
            // 
            // groupBox4
            // 
            groupBox4.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            groupBox4.Controls.Add(DrawCurveButton);
            groupBox4.Controls.Add(CurveTypeCombobox);
            groupBox4.Dock = DockStyle.Left;
            groupBox4.Location = new Point(3, 3);
            groupBox4.Name = "groupBox4";
            groupBox4.Size = new Size(197, 119);
            groupBox4.TabIndex = 3;
            groupBox4.TabStop = false;
            groupBox4.Text = "Тип";
            // 
            // DrawCurveButton
            // 
            DrawCurveButton.Anchor = AnchorStyles.Left;
            DrawCurveButton.Location = new Point(21, 75);
            DrawCurveButton.Name = "DrawCurveButton";
            DrawCurveButton.Size = new Size(155, 29);
            DrawCurveButton.TabIndex = 6;
            DrawCurveButton.Text = "Построить";
            DrawCurveButton.UseVisualStyleBackColor = true;
            DrawCurveButton.Click += DrawCurveButton_ClickAsync;
            // 
            // CurveTypeCombobox
            // 
            CurveTypeCombobox.FormattingEnabled = true;
            CurveTypeCombobox.Location = new Point(21, 31);
            CurveTypeCombobox.Name = "CurveTypeCombobox";
            CurveTypeCombobox.Size = new Size(155, 28);
            CurveTypeCombobox.TabIndex = 0;
            CurveTypeCombobox.SelectedIndexChanged += CurveTypeCombobox_SelectedIndexChanged;
            // 
            // SplinesTab
            // 
            SplinesTab.Controls.Add(groupBox3);
            SplinesTab.Controls.Add(groupBox5);
            SplinesTab.Location = new Point(4, 29);
            SplinesTab.Name = "SplinesTab";
            SplinesTab.Padding = new Padding(3);
            SplinesTab.Size = new Size(1174, 125);
            SplinesTab.TabIndex = 2;
            SplinesTab.Text = "Параметрические кривые";
            SplinesTab.UseVisualStyleBackColor = true;
            // 
            // splitContainer2
            // 
            splitContainer2.Dock = DockStyle.Fill;
            splitContainer2.FixedPanel = FixedPanel.Panel2;
            splitContainer2.Location = new Point(0, 0);
            splitContainer2.Name = "splitContainer2";
            // 
            // splitContainer2.Panel1
            // 
            splitContainer2.Panel1.AutoScroll = true;
            splitContainer2.Panel1.AutoScrollMinSize = new Size(550, 550);
            splitContainer2.Panel1.BackColor = SystemColors.ControlDark;
            splitContainer2.Panel1.Controls.Add(CanvasPictureBox);
            // 
            // splitContainer2.Panel2
            // 
            splitContainer2.Panel2.Controls.Add(DebugGridView);
            splitContainer2.Panel2.Controls.Add(button2);
            splitContainer2.Panel2.Controls.Add(EnableDebugButton);
            splitContainer2.Size = new Size(1182, 591);
            splitContainer2.SplitterDistance = 741;
            splitContainer2.TabIndex = 0;
            // 
            // CanvasPictureBox
            // 
            CanvasPictureBox.Anchor = AnchorStyles.None;
            CanvasPictureBox.BackColor = Color.White;
            CanvasPictureBox.BorderStyle = BorderStyle.FixedSingle;
            CanvasPictureBox.Location = new Point(109, 40);
            CanvasPictureBox.Name = "CanvasPictureBox";
            CanvasPictureBox.Size = new Size(512, 512);
            CanvasPictureBox.TabIndex = 0;
            CanvasPictureBox.TabStop = false;
            // 
            // DebugGridView
            // 
            DebugGridView.AllowUserToAddRows = false;
            DebugGridView.AllowUserToDeleteRows = false;
            DebugGridView.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
            DebugGridView.BorderStyle = BorderStyle.None;
            DebugGridView.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            DebugGridView.Location = new Point(0, 35);
            DebugGridView.Margin = new Padding(0);
            DebugGridView.Name = "DebugGridView";
            DebugGridView.RowHeadersWidth = 51;
            DebugGridView.Size = new Size(435, 556);
            DebugGridView.TabIndex = 3;
            // 
            // button2
            // 
            button2.Anchor = AnchorStyles.Top | AnchorStyles.Right;
            button2.Location = new Point(274, 2);
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
            // groupBox3
            // 
            groupBox3.AutoSize = true;
            groupBox3.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            groupBox3.Controls.Add(SplineParametersLayoutPanel);
            groupBox3.Dock = DockStyle.Fill;
            groupBox3.Location = new Point(200, 3);
            groupBox3.Name = "groupBox3";
            groupBox3.Size = new Size(971, 119);
            groupBox3.TabIndex = 9;
            groupBox3.TabStop = false;
            groupBox3.Text = "Параметры";
            // 
            // SplineParametersLayoutPanel
            // 
            SplineParametersLayoutPanel.AutoSize = true;
            SplineParametersLayoutPanel.Dock = DockStyle.Fill;
            SplineParametersLayoutPanel.FlowDirection = FlowDirection.TopDown;
            SplineParametersLayoutPanel.Location = new Point(3, 23);
            SplineParametersLayoutPanel.Name = "SplineParametersLayoutPanel";
            SplineParametersLayoutPanel.Size = new Size(965, 93);
            SplineParametersLayoutPanel.TabIndex = 0;
            // 
            // groupBox5
            // 
            groupBox5.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            groupBox5.Controls.Add(DrawSplineButton);
            groupBox5.Controls.Add(SplineTypeCombobox);
            groupBox5.Dock = DockStyle.Left;
            groupBox5.Location = new Point(3, 3);
            groupBox5.Name = "groupBox5";
            groupBox5.Size = new Size(197, 119);
            groupBox5.TabIndex = 8;
            groupBox5.TabStop = false;
            groupBox5.Text = "Тип";
            // 
            // DrawSplineButton
            // 
            DrawSplineButton.Anchor = AnchorStyles.Left;
            DrawSplineButton.Location = new Point(21, 74);
            DrawSplineButton.Name = "DrawSplineButton";
            DrawSplineButton.Size = new Size(155, 29);
            DrawSplineButton.TabIndex = 6;
            DrawSplineButton.Text = "Построить";
            DrawSplineButton.UseVisualStyleBackColor = true;
            DrawSplineButton.Click += DrawSplineButton_Click;
            // 
            // SplineTypeCombobox
            // 
            SplineTypeCombobox.FormattingEnabled = true;
            SplineTypeCombobox.Location = new Point(21, 31);
            SplineTypeCombobox.Name = "SplineTypeCombobox";
            SplineTypeCombobox.Size = new Size(155, 28);
            SplineTypeCombobox.TabIndex = 0;
            SplineTypeCombobox.SelectedIndexChanged += SplineTypeCombobox_SelectedIndexChanged;
            // 
            // MainForm
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(1182, 753);
            Controls.Add(splitContainer1);
            Name = "MainForm";
            ShowIcon = false;
            StartPosition = FormStartPosition.CenterScreen;
            Text = "GIIS LW";
            splitContainer1.Panel1.ResumeLayout(false);
            splitContainer1.Panel2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)splitContainer1).EndInit();
            splitContainer1.ResumeLayout(false);
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
            splitContainer2.Panel1.ResumeLayout(false);
            splitContainer2.Panel2.ResumeLayout(false);
            splitContainer2.Panel2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)splitContainer2).EndInit();
            splitContainer2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)CanvasPictureBox).EndInit();
            ((System.ComponentModel.ISupportInitialize)DebugGridView).EndInit();
            groupBox3.ResumeLayout(false);
            groupBox3.PerformLayout();
            groupBox5.ResumeLayout(false);
            ResumeLayout(false);
        }

        #endregion

        private SplitContainer splitContainer1;
        private TabControl InstrumentCluster;
        private TabPage LinesTab;
        private TabPage SecondDegreeCurvesTab;
        private SplitContainer splitContainer2;
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

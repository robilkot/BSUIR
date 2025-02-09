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
            LinesInstrumentCluster = new TabPage();
            groupBox3 = new GroupBox();
            LineDrawingMethodCombobox = new ComboBox();
            DrawLineButton = new Button();
            groupBox2 = new GroupBox();
            label3 = new Label();
            EntryX2 = new NumericUpDown();
            EntryY2 = new NumericUpDown();
            label4 = new Label();
            groupBox1 = new GroupBox();
            label2 = new Label();
            EntryY1 = new NumericUpDown();
            label1 = new Label();
            EntryX1 = new NumericUpDown();
            tabPage2 = new TabPage();
            DrawCurveButton = new Button();
            CurveParametersPanel = new FlowLayoutPanel();
            groupBox4 = new GroupBox();
            CurveTypeCombobox = new ComboBox();
            splitContainer2 = new SplitContainer();
            CanvasPictureBox = new PictureBox();
            DebugGridView = new DataGridView();
            button2 = new Button();
            EnableDebugButton = new CheckBox();
            ((System.ComponentModel.ISupportInitialize)splitContainer1).BeginInit();
            splitContainer1.Panel1.SuspendLayout();
            splitContainer1.Panel2.SuspendLayout();
            splitContainer1.SuspendLayout();
            InstrumentCluster.SuspendLayout();
            LinesInstrumentCluster.SuspendLayout();
            groupBox3.SuspendLayout();
            groupBox2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)EntryX2).BeginInit();
            ((System.ComponentModel.ISupportInitialize)EntryY2).BeginInit();
            groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)EntryY1).BeginInit();
            ((System.ComponentModel.ISupportInitialize)EntryX1).BeginInit();
            tabPage2.SuspendLayout();
            groupBox4.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)splitContainer2).BeginInit();
            splitContainer2.Panel1.SuspendLayout();
            splitContainer2.Panel2.SuspendLayout();
            splitContainer2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)CanvasPictureBox).BeginInit();
            ((System.ComponentModel.ISupportInitialize)DebugGridView).BeginInit();
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
            splitContainer1.SplitterDistance = 141;
            splitContainer1.TabIndex = 0;
            // 
            // InstrumentCluster
            // 
            InstrumentCluster.Controls.Add(LinesInstrumentCluster);
            InstrumentCluster.Controls.Add(tabPage2);
            InstrumentCluster.Dock = DockStyle.Fill;
            InstrumentCluster.ItemSize = new Size(150, 20);
            InstrumentCluster.Location = new Point(0, 0);
            InstrumentCluster.Name = "InstrumentCluster";
            InstrumentCluster.SelectedIndex = 0;
            InstrumentCluster.Size = new Size(1182, 141);
            InstrumentCluster.SizeMode = TabSizeMode.Fixed;
            InstrumentCluster.TabIndex = 0;
            // 
            // LinesInstrumentCluster
            // 
            LinesInstrumentCluster.AutoScroll = true;
            LinesInstrumentCluster.Controls.Add(groupBox3);
            LinesInstrumentCluster.Controls.Add(DrawLineButton);
            LinesInstrumentCluster.Controls.Add(groupBox2);
            LinesInstrumentCluster.Controls.Add(groupBox1);
            LinesInstrumentCluster.Location = new Point(4, 24);
            LinesInstrumentCluster.Name = "LinesInstrumentCluster";
            LinesInstrumentCluster.Padding = new Padding(3);
            LinesInstrumentCluster.Size = new Size(1174, 113);
            LinesInstrumentCluster.TabIndex = 0;
            LinesInstrumentCluster.Text = "Отрезки";
            LinesInstrumentCluster.UseVisualStyleBackColor = true;
            // 
            // groupBox3
            // 
            groupBox3.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            groupBox3.Controls.Add(LineDrawingMethodCombobox);
            groupBox3.Dock = DockStyle.Left;
            groupBox3.Location = new Point(418, 3);
            groupBox3.Name = "groupBox3";
            groupBox3.Size = new Size(197, 107);
            groupBox3.TabIndex = 2;
            groupBox3.TabStop = false;
            groupBox3.Text = "Метод построения";
            // 
            // LineDrawingMethodCombobox
            // 
            LineDrawingMethodCombobox.FormattingEnabled = true;
            LineDrawingMethodCombobox.Location = new Point(21, 31);
            LineDrawingMethodCombobox.Name = "LineDrawingMethodCombobox";
            LineDrawingMethodCombobox.Size = new Size(155, 28);
            LineDrawingMethodCombobox.TabIndex = 0;
            // 
            // DrawLineButton
            // 
            DrawLineButton.Anchor = AnchorStyles.Left;
            DrawLineButton.Location = new Point(764, 44);
            DrawLineButton.Name = "DrawLineButton";
            DrawLineButton.Size = new Size(128, 29);
            DrawLineButton.TabIndex = 2;
            DrawLineButton.Text = "Построить";
            DrawLineButton.UseVisualStyleBackColor = true;
            DrawLineButton.Click += DrawLineButton_ClickAsync;
            // 
            // groupBox2
            // 
            groupBox2.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            groupBox2.Controls.Add(label3);
            groupBox2.Controls.Add(EntryX2);
            groupBox2.Controls.Add(EntryY2);
            groupBox2.Controls.Add(label4);
            groupBox2.Dock = DockStyle.Left;
            groupBox2.Location = new Point(209, 3);
            groupBox2.Name = "groupBox2";
            groupBox2.Size = new Size(209, 107);
            groupBox2.TabIndex = 1;
            groupBox2.TabStop = false;
            groupBox2.Text = "Координаты конца";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(11, 66);
            label3.Name = "label3";
            label3.Size = new Size(25, 20);
            label3.TabIndex = 7;
            label3.Text = "Y2";
            // 
            // EntryX2
            // 
            EntryX2.Location = new Point(40, 31);
            EntryX2.Name = "EntryX2";
            EntryX2.Size = new Size(149, 27);
            EntryX2.TabIndex = 4;
            EntryX2.Value = new decimal(new int[] { 9, 0, 0, 0 });
            // 
            // EntryY2
            // 
            EntryY2.Location = new Point(40, 64);
            EntryY2.Name = "EntryY2";
            EntryY2.Size = new Size(149, 27);
            EntryY2.TabIndex = 6;
            EntryY2.Value = new decimal(new int[] { 4, 0, 0, 0 });
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Location = new Point(11, 33);
            label4.Name = "label4";
            label4.Size = new Size(26, 20);
            label4.TabIndex = 5;
            label4.Text = "X2";
            // 
            // groupBox1
            // 
            groupBox1.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            groupBox1.Controls.Add(label2);
            groupBox1.Controls.Add(EntryY1);
            groupBox1.Controls.Add(label1);
            groupBox1.Controls.Add(EntryX1);
            groupBox1.Dock = DockStyle.Left;
            groupBox1.Location = new Point(3, 3);
            groupBox1.Name = "groupBox1";
            groupBox1.Size = new Size(206, 107);
            groupBox1.TabIndex = 0;
            groupBox1.TabStop = false;
            groupBox1.Text = "Координаты начала";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(7, 66);
            label2.Name = "label2";
            label2.Size = new Size(25, 20);
            label2.TabIndex = 3;
            label2.Text = "Y1";
            // 
            // EntryY1
            // 
            EntryY1.Location = new Point(36, 64);
            EntryY1.Name = "EntryY1";
            EntryY1.Size = new Size(149, 27);
            EntryY1.TabIndex = 2;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(7, 33);
            label1.Name = "label1";
            label1.Size = new Size(26, 20);
            label1.TabIndex = 1;
            label1.Text = "X1";
            // 
            // EntryX1
            // 
            EntryX1.Location = new Point(36, 31);
            EntryX1.Name = "EntryX1";
            EntryX1.Size = new Size(149, 27);
            EntryX1.TabIndex = 0;
            // 
            // tabPage2
            // 
            tabPage2.Controls.Add(DrawCurveButton);
            tabPage2.Controls.Add(CurveParametersPanel);
            tabPage2.Controls.Add(groupBox4);
            tabPage2.Location = new Point(4, 24);
            tabPage2.Name = "tabPage2";
            tabPage2.Padding = new Padding(3);
            tabPage2.Size = new Size(1174, 113);
            tabPage2.TabIndex = 1;
            tabPage2.Text = "Кривые";
            tabPage2.UseVisualStyleBackColor = true;
            // 
            // DrawCurveButton
            // 
            DrawCurveButton.Anchor = AnchorStyles.Left;
            DrawCurveButton.Location = new Point(523, 42);
            DrawCurveButton.Name = "DrawCurveButton";
            DrawCurveButton.Size = new Size(128, 29);
            DrawCurveButton.TabIndex = 6;
            DrawCurveButton.Text = "Построить";
            DrawCurveButton.UseVisualStyleBackColor = true;
            DrawCurveButton.Click += DrawCurveButton_ClickAsync;
            // 
            // CurveParametersPanel
            // 
            CurveParametersPanel.Dock = DockStyle.Left;
            CurveParametersPanel.Location = new Point(200, 3);
            CurveParametersPanel.Name = "CurveParametersPanel";
            CurveParametersPanel.Size = new Size(241, 107);
            CurveParametersPanel.TabIndex = 5;
            // 
            // groupBox4
            // 
            groupBox4.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            groupBox4.Controls.Add(CurveTypeCombobox);
            groupBox4.Dock = DockStyle.Left;
            groupBox4.Location = new Point(3, 3);
            groupBox4.Name = "groupBox4";
            groupBox4.Size = new Size(197, 107);
            groupBox4.TabIndex = 3;
            groupBox4.TabStop = false;
            groupBox4.Text = "Тип кривой";
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
            splitContainer2.Panel1.AutoScrollMinSize = new Size(600, 600);
            splitContainer2.Panel1.BackColor = SystemColors.ControlDark;
            splitContainer2.Panel1.Controls.Add(CanvasPictureBox);
            // 
            // splitContainer2.Panel2
            // 
            splitContainer2.Panel2.Controls.Add(DebugGridView);
            splitContainer2.Panel2.Controls.Add(button2);
            splitContainer2.Panel2.Controls.Add(EnableDebugButton);
            splitContainer2.Size = new Size(1182, 608);
            splitContainer2.SplitterDistance = 741;
            splitContainer2.TabIndex = 0;
            // 
            // CanvasPictureBox
            // 
            CanvasPictureBox.Anchor = AnchorStyles.None;
            CanvasPictureBox.BackColor = Color.White;
            CanvasPictureBox.BorderStyle = BorderStyle.FixedSingle;
            CanvasPictureBox.Location = new Point(119, 49);
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
            DebugGridView.Size = new Size(435, 573);
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
            LinesInstrumentCluster.ResumeLayout(false);
            groupBox3.ResumeLayout(false);
            groupBox2.ResumeLayout(false);
            groupBox2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)EntryX2).EndInit();
            ((System.ComponentModel.ISupportInitialize)EntryY2).EndInit();
            groupBox1.ResumeLayout(false);
            groupBox1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)EntryY1).EndInit();
            ((System.ComponentModel.ISupportInitialize)EntryX1).EndInit();
            tabPage2.ResumeLayout(false);
            groupBox4.ResumeLayout(false);
            splitContainer2.Panel1.ResumeLayout(false);
            splitContainer2.Panel2.ResumeLayout(false);
            splitContainer2.Panel2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)splitContainer2).EndInit();
            splitContainer2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)CanvasPictureBox).EndInit();
            ((System.ComponentModel.ISupportInitialize)DebugGridView).EndInit();
            ResumeLayout(false);
        }

        #endregion

        private SplitContainer splitContainer1;
        private TabControl InstrumentCluster;
        private TabPage LinesInstrumentCluster;
        private TabPage tabPage2;
        private SplitContainer splitContainer2;
        private PictureBox CanvasPictureBox;
        private CheckBox EnableDebugButton;
        private GroupBox groupBox1;
        private Button DrawLineButton;
        private GroupBox groupBox2;
        private GroupBox groupBox3;
        private Button button2;
        private ComboBox LineDrawingMethodCombobox;
        private Label label3;
        private NumericUpDown EntryX2;
        private NumericUpDown EntryY2;
        private Label label4;
        private Label label2;
        private NumericUpDown EntryY1;
        private Label label1;
        private NumericUpDown EntryX1;
        private DataGridView DebugGridView;
        private GroupBox groupBox4;
        private ComboBox CurveTypeCombobox;
        private Button DrawCurveButton;
        private FlowLayoutPanel CurveParametersPanel;
    }
}

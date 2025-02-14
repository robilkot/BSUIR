using LW1.Common;

namespace LW1.View
{
    public static class ParameterViewWrapper
    {
        public static Control CreateView(IParameter parameter) => parameter switch
        {
            Parameter<int> param => CreateView(param),
            Parameter<Point> param => CreateView(param),
            Parameter<Color> param => CreateView(param),
            _ => throw new NotSupportedException()
        };

        private static Control CreateView(Parameter<int> parameter)
        {
            var numericUpDown = new NumericUpDown() { Value = parameter.Value };
            numericUpDown.ValueChanged += (sender, args) =>
            {
                var updown = sender as NumericUpDown;
                parameter.Value = (int)updown!.Value;
            };

            parameter.ParameterChanged += (value) => { numericUpDown.Value = value; };

            var panel = new FlowLayoutPanel()
            {
                FlowDirection = FlowDirection.LeftToRight,
                AutoSize = true,
            }
                .With(CreateLabel(parameter.DisplayName))
                .With(numericUpDown);

            return panel;
        }
        private static Control CreateView(Parameter<Point> parameter)
        {
            var xControl = new NumericUpDown() { Value = parameter.Value.X };
            xControl.ValueChanged += (sender, args) =>
            {
                parameter.Value = parameter.Value with { X = (int)(sender as NumericUpDown)!.Value };
            };

            var yControl = new NumericUpDown() { Value = parameter.Value.Y };
            yControl.ValueChanged += (sender, args) =>
            {
                parameter.Value = parameter.Value with { Y = (int)(sender as NumericUpDown)!.Value };
            };

            parameter.ParameterChanged += (value) =>
            {
                xControl.Value = value.X;
                yControl.Value = value.Y;
            };

            var panel = new FlowLayoutPanel()
            {
                FlowDirection = FlowDirection.TopDown,
                AutoSize = true,
                Dock = DockStyle.Fill
            };

            var panel_X = new FlowLayoutPanel()
            {
                FlowDirection = FlowDirection.LeftToRight,
                AutoSize = true,
            };
            panel_X.Controls.Add(CreateLabel("X"));
            panel_X.Controls.Add(xControl);


            var panel_Y = new FlowLayoutPanel()
            {
                FlowDirection = FlowDirection.LeftToRight,
                AutoSize = true,
            };
            panel_Y.Controls.Add(CreateLabel("Y"));
            panel_Y.Controls.Add(yControl);


            panel.Controls.Add(panel_X);
            panel.Controls.Add(panel_Y);

            return panel.Grouped(parameter.DisplayName);
        }
        private static Control CreateView(Parameter<Color> parameter)
        {
            var pictureBox = new PictureBox() { BackColor = parameter.Value, BorderStyle = BorderStyle.FixedSingle };

            pictureBox.Click += (sender, args) =>
            {
                ColorDialog dialog = new()
                {
                    AllowFullOpen = true,
                    Color = parameter.Value
                };

                if (dialog.ShowDialog() == DialogResult.OK)
                    pictureBox.BackColor = dialog.Color;
                parameter.Value = dialog.Color;
            };

            var panel = new FlowLayoutPanel()
            {
                FlowDirection = FlowDirection.TopDown,
                AutoSize = true,
                Dock = DockStyle.Fill
            }
            .With(pictureBox);

            return panel.Grouped(parameter.DisplayName);
        }

        private static T With<T>(this T control, Control another) where T : Control
        {
            control.Controls.Add(another);
            return control;
        }

        private static GroupBox Grouped<T>(this T control, string name) where T : Control
        {
            var groupBox = new GroupBox() { Text = name, AutoSize = true };
            groupBox.Controls.Add(control);

            return groupBox;
        }

        private static Label CreateLabel(string text) => new()
        {
            Dock = DockStyle.Left,
            TextAlign = ContentAlignment.MiddleLeft,
            AutoSize = true,
            Text = text,
        };
    }
}

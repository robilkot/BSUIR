using LW1.Common;

namespace LW1
{
    public class UIParametersWrapper
    {
        private readonly FlowLayoutPanel _panel;
        private Dictionary<NumericUpDown, Parameter<int>> _numericParametersMapping = [];

        private IDrawingParameters _parameters;
        public IDrawingParameters Parameters { get => _parameters;
            set
            {
                _parameters = value;

                var properties = _parameters?.Properties<int>() ?? [];

                // Unsubscribe to avoid memory leak
                foreach(var control in _numericParametersMapping.Keys)
                {
                    control.ValueChanged -= NumericUpDown_ValueChanged;
                }
                _numericParametersMapping.Clear();
                _panel.Controls.Clear();

                foreach (var parameter in properties)
                {
                    var new_panel = new FlowLayoutPanel()
                    {
                        FlowDirection = FlowDirection.LeftToRight,
                        AutoSize = true,
                    };

                    new_panel.Controls.Add(new Label()
                    {
                        Dock = DockStyle.Fill,
                        TextAlign = ContentAlignment.MiddleLeft,
                        AutoSize = true,
                        Text = parameter.DisplayName,
                    });
                    var numericUpDown = new NumericUpDown()
                    {
                        Value = parameter.Value,
                    };
                    numericUpDown.ValueChanged += NumericUpDown_ValueChanged;

                    new_panel.Controls.Add(numericUpDown);

                    _numericParametersMapping.Add(numericUpDown, parameter);

                    _panel.Controls.Add(new_panel);
                }
            }
        }

        public UIParametersWrapper(FlowLayoutPanel panel)
        {
            _panel = panel;
        }

        private void NumericUpDown_ValueChanged(object? sender, EventArgs e)
        {
            var numeridUpDown = ((NumericUpDown)sender!);
            _numericParametersMapping[numeridUpDown].Value = (int)numeridUpDown.Value;
        }
    }
}

using LW1.Common;

namespace LW1.View
{
    public class ParametersWrapper
    {
        private readonly FlowLayoutPanel _panel;

        private IDrawingParameters _parameters;
        public IDrawingParameters Parameters
        {
            get => _parameters;
            set
            {
                _parameters = value;
                _panel.Controls.Clear();

                foreach (var parameter in _parameters.Properties())
                {
                    _panel.Controls.Add(ParameterViewWrapper.CreateView(parameter));
                }
            }
        }

#pragma warning disable CS8618 // Non-nullable field must contain a non-null value when exiting constructor. Consider declaring as nullable.
        public ParametersWrapper(FlowLayoutPanel panel)
        {
            _panel = panel;
        }
#pragma warning restore CS8618 // Non-nullable field must contain a non-null value when exiting constructor. Consider declaring as nullable.
    }
}

using LW1.Common;
using LW1.View;

namespace LW1
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

                var properties = _parameters.Properties().ToList();

                _panel.Controls.Clear();

                foreach (var parameter in properties)
                {
                    var control = ParameterViewWrapper.CreateView(parameter);
                    _panel.Controls.Add(control);
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

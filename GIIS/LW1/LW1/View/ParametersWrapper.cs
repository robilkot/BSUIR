using LW1.Common;

namespace LW1.View
{
    public class ParametersWrapper
    {
        private readonly Canvas _workspace;
        private readonly FlowLayoutPanel _panel;

        private readonly List<PointHandle> _handles = [];
        private readonly List<Control> _views = [];

        private IDrawingParameters _parameters;
        public IDrawingParameters Parameters
        {
            get => _parameters;
            set
            {
                _parameters = value;

                ClearViews();
                ClearHandles();

                CreateViews();
                CreateHandles();
            }
        }

        private void ClearViews()
        {
            foreach (var control in _views)
            {
                _panel.Controls.Remove(control);
            }

            _views.Clear();
        }
        private void CreateViews()
        {
            foreach (var parameter in _parameters.Properties())
            {
                var view = ParameterViewWrapper.CreateView(parameter);
                _panel.Controls.Add(view);

                if (view is not null)
                {
                    _views.Add(view);
                }
            }
        }
        private void CreateHandles()
        {
            foreach (var parameter in _parameters.Properties().OfType<Parameter<Point>>())
            {
                var handle = new PointHandle()
                {
                    Point = parameter
                };

                _handles.Add(handle);
                _workspace.Controls.Add(handle);
            }
        }
        private void ClearHandles()
        {
            foreach (var control in _handles)
            {
                _workspace.Controls.Remove(control);
            }

            _handles.Clear();
        }

#pragma warning disable CS8618 // Non-nullable field must contain a non-null value when exiting constructor. Consider declaring as nullable.
        public ParametersWrapper(FlowLayoutPanel panel, Canvas workspace, TabControl instrumentCluster, int v)
        {
            _panel = panel;
            _workspace = workspace;

            instrumentCluster.SelectedIndexChanged += (o, e) =>
            {
                if (instrumentCluster.SelectedIndex == v)
                {
                    CreateHandles();
                }
                else
                {
                    ClearHandles();
                }
            };
        }
#pragma warning restore CS8618 // Non-nullable field must contain a non-null value when exiting constructor. Consider declaring as nullable.
    }
}

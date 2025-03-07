using LW1.Common;
using LW1.Common.Parameters;

namespace LW1.View
{
    public class ParametersWrapper
    {
        private readonly Canvas _workspace;
        private readonly FlowLayoutPanel _panel;

        private bool _tabSelected = false;
        private readonly List<PointHandle> _handles = [];
        private readonly List<Control> _views = [];

        private IParameters _parameters;
        public IParameters Parameters
        {
            get => _parameters;
            set
            {
                _parameters = value;
                
                ClearViews();
                CreateViews();
            
                if(_tabSelected)
                {
                    ClearHandles();
                    CreateHandles();
                }
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
        private void createHandle(Parameter<Point> param)
        {
            var handle = new PointHandle()
            {
                Point = param
            };

            _handles.Add(handle);
            _workspace.Controls.Add(handle);
        }
        private void removeHandle(Parameter<Point> param)
        {
            var handle = _handles.First(h => h.Point == param);

            _handles.Remove(handle);
            _workspace.Controls.Remove(handle);
        }

        private void CreateHandles()
        {
            var parameters = _parameters.Properties().ToList();
            var pointParameters = parameters.OfType<Parameter<Point>>().ToList();
            var listPointParameters = parameters.OfType<ParametersList<Point>>().ToList();

            foreach (var parameter in pointParameters)
            {
                createHandle(parameter);
            }
            foreach (var parametersList in listPointParameters)
            {
                parametersList.ParameterAdded += createHandle;
                parametersList.ParameterRemoved += removeHandle;

                foreach(var pointParam in parametersList)
                {
                    createHandle(pointParam);
                }
            }
        }
        private void ClearHandles()
        {
            var parameters = _parameters.Properties().ToList();
            var listPointParameters = parameters.OfType<ParametersList<Point>>().ToList();

            foreach (var parametersList in listPointParameters)
            {
                parametersList.ParameterAdded -= createHandle;
                parametersList.ParameterRemoved -= removeHandle;
            }

            foreach (var control in _handles)
            {
                _workspace.Controls.Remove(control);
            }

            _handles.Clear();
        }

#pragma warning disable CS8618 // Non-nullable field must contain a non-null value when exiting constructor. Consider declaring as nullable.
        public ParametersWrapper(FlowLayoutPanel panel, Canvas workspace, TabPage tab)
        {
            _panel = panel;
            _workspace = workspace;

            var tabControl = (TabControl)tab.Parent!;

            tabControl.Selected += (o, e) =>
            {
                if (e.TabPage == tab)
                {
                    _tabSelected = true;
                    CreateHandles();
                }
            };
            tabControl.Deselected += (o, e) =>
            {
                if(e.TabPage == tab)
                {
                    _tabSelected = false;
                    ClearHandles();
                }
            };
        }
#pragma warning restore CS8618 // Non-nullable field must contain a non-null value when exiting constructor. Consider declaring as nullable.
    }
}

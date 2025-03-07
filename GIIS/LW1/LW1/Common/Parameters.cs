namespace LW1.Common
{
    public interface IParameter : INamed;
    public class Parameter<T> : IParameter
    {
        public delegate void ParameterChangeHandler(T value);
        public event ParameterChangeHandler? ParameterChanged;

        private T _value;
        public required T Value { get => _value; set
            {
                if(!(_value?.Equals(value) ?? false))
                {
                    _value = value;
                    ParameterChanged?.Invoke(_value);
                }
            }
        }
        public required string DisplayName { get; init; }

        public static implicit operator T(Parameter<T> param) => param.Value;
        public static implicit operator Parameter<T>(T param) => new() { DisplayName = "New parameter", Value = param };
    }

    public class ParametersList<T> : List<Parameter<T>>, IParameter
    {
        public delegate void ParameterChangedHandler(Parameter<T> value);
        public event ParameterChangedHandler? ParameterAdded;
        public event ParameterChangedHandler? ParameterRemoved;
        public string DisplayName { get; init; }
        public ParametersList(string name)
        {
            DisplayName = name;
        }
        new public void Add(Parameter<T> param)
        {
            base.Add(param);
            ParameterAdded?.Invoke(param);
        }
        new public void Remove(Parameter<T> param)
        {
            base.Remove(param);
            ParameterRemoved?.Invoke(param);
        }
    }

    public interface IParameters;

    public interface IDrawingParameters : IParameters
    {
        public Parameter<Color> Color { get; init; }
    }
}

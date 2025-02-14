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

    public interface IDrawingParameters
    {
        public Parameter<Color> Color { get; init; }
    }
}

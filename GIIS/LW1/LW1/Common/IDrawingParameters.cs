namespace LW1.Common
{
    public interface IParameter : INamed;
    
    public class Parameter<T> : IParameter
    {
        public required string DisplayName { get; init; }
        public required T Value { get; set; }

        public static implicit operator T(Parameter<T> param) => param.Value;
        public static implicit operator Parameter<T>(T param) => new() { DisplayName = "New parameter", Value = param };
    }

    public interface IDrawingParameters
    {
        public Parameter<Color> Color { get; init; }
    }
}

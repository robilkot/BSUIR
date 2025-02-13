namespace LW1.Common
{
    public interface IParameter : INamed;
    public class Parameter<T> : IParameter
    {
        public required string DisplayName { get; init; }
        public required T Value { get; set; }
    }
}

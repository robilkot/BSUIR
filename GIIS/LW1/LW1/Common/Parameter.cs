namespace LW1.Common
{
    public class Parameter<T> : INamed
    {
        public required string DisplayName { get; init; }
        public required T Value { get; set; }
    }
}

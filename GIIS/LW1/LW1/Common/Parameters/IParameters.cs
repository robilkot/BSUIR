namespace LW1.Common.Parameters
{
    public interface IParameters;

    public interface IDrawingParameters : IParameters
    {
        public Parameter<Color> Color { get; init; }
    }
}

namespace LW1.Common.Algorithms
{
    public interface IAlgorithm;

    public interface IAlgorithm<in I, out O>
    {
        O Execute(I param);
    }
}

namespace LW1.Common
{
    public interface IAlgorithm;

    public interface IAlgorithm<in I, out O>
    {
        O Execute(I param);
    }
}

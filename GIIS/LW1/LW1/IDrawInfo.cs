namespace LW1
{
    public interface IDrawInfo
    {
        public IEnumerable<string> Columns { get; }
        public IEnumerable<string> Row { get; }
    }
}

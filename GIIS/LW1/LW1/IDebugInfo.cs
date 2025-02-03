namespace LW1
{
    public interface IDebugInfo
    {
        public IEnumerable<string> Columns { get; }
        public IEnumerable<string> Row { get; }
    }
}

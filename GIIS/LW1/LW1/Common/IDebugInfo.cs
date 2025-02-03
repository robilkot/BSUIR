namespace LW1.Common
{
    public interface IDebugInfo
    {
        public IEnumerable<string> Columns { get; }
        public IEnumerable<string> Row { get; }
    }
}

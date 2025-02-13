namespace LW1.Common
{
    public abstract class DebugInfo
    {
        // skipping these two properties with skiplast(2). not ideal, but let it be
        public IEnumerable<string> Keys => GetType().GetProperties().SkipLast(2).Select(x => x.Name);
        public IEnumerable<string> Values => GetType().GetProperties().SkipLast(2).Select(x => $"{x.GetValue(this)}");
    }
}

namespace LW1.Common
{
    public abstract class DebugInfo
    {
        // skipping these two properties with skiplast(2). not ideal, but let it be
        public List<string> Keys => GetType().GetProperties().SkipLast(2).Select(x => x.Name).ToList();
        public List<string> Values => GetType().GetProperties().SkipLast(2).Select(x => $"{x.GetValue(this)}").ToList();
    }

    public sealed class EmptyDebugInfo : DebugInfo { }
}

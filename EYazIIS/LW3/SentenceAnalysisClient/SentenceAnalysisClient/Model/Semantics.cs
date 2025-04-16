namespace SentenceAnalysisClient.Model
{
    public class Semantics
    {
        public NERClass Class { get; set; }
    }

    public record NamedEntity(string Text, NERClass Class, string? NormalForm);
}

namespace backend.Model
{
    public class LexemeMetadata
    {
        public required string Text { get; set; }
        public int ContainingDocuments { get; set; }
    }
}

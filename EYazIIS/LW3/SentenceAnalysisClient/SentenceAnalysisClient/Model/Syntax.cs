namespace SentenceAnalysisClient.Model
{
    public class Syntax
    {
        public required string Id { get; set; }
        public required string HeadId { get; set; }
        public required GrammaticalRelation Relation { get; set; }
    }
}
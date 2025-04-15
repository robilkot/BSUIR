using SentenceAnalysisClient.Model;

namespace SentenceAnalysisClient.ViewModels
{
    public class SyntaxViewModel : ViewModelBase
    {
        public required SentenceTokenViewModel Token { get; set; }
        public SentenceTokenViewModel? HeadToken { get; set; }
        public GrammaticalRelation Relation { get; set; }
    }
}
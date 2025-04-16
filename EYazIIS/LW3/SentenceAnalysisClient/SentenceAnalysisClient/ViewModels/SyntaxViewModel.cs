using ReactiveUI;
using SentenceAnalysisClient.Model;

namespace SentenceAnalysisClient.ViewModels
{
    public class SyntaxViewModel : ViewModelBase
    {
        public required SentenceTokenViewModel Token { get; set; }
        public SentenceTokenViewModel? HeadToken { get; set; }

        private SyntaxRole _relation;
        public SyntaxRole Relation
        {
            get => _relation;
            set => this.RaiseAndSetIfChanged(ref _relation, value);
        }
    }
}
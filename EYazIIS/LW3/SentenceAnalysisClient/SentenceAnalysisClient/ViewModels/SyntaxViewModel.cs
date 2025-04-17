using Newtonsoft.Json;
using ReactiveUI;
using SentenceAnalysisClient.Model;

namespace SentenceAnalysisClient.ViewModels
{
    public class SyntaxViewModel : ViewModelBase
    {
        [JsonProperty]
        public required SentenceTokenViewModel Token { get; set; }
        [JsonProperty]
        public SentenceTokenViewModel? HeadToken { get; set; }

        private SyntaxRole _relation;
        [JsonProperty]
        public SyntaxRole Relation
        {
            get => _relation;
            set => this.RaiseAndSetIfChanged(ref _relation, value);
        }
    }
}
using Newtonsoft.Json;
using ReactiveUI;
using SentenceAnalysisClient.ViewModels.Semantics;

namespace SentenceAnalysisClient.ViewModels
{
    public class SentenceTokenViewModel : ViewModelBase
    {
        [JsonProperty]
        public required string Text { get; set; }

        private MorphologyViewModel? _morphology;
        [JsonProperty]
        public MorphologyViewModel? Morphology
        {
            get => _morphology;
            set => this.RaiseAndSetIfChanged(ref _morphology, value);
        }

        private SyntaxViewModel? _syntax;
        [JsonProperty]
        public SyntaxViewModel? Syntax
        {
            get => _syntax;
            set => this.RaiseAndSetIfChanged(ref _syntax, value);
        }

        private SemanticsViewModel? _semantics;
        [JsonProperty]
        public SemanticsViewModel? Semantics
        {
            get => _semantics;
            set => this.RaiseAndSetIfChanged(ref _semantics, value);
        }
    }
}
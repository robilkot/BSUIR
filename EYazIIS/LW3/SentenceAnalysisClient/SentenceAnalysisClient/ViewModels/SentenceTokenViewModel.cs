using ReactiveUI;

namespace SentenceAnalysisClient.ViewModels
{
    public class SentenceTokenViewModel : ViewModelBase
    {
        public required string Text { get; set; }

        private MorphologyViewModel? _morphology;
        public MorphologyViewModel? Morphology
        {
            get => _morphology;
            set => this.RaiseAndSetIfChanged(ref _morphology, value);
        }

        private SyntaxViewModel? _syntax;
        public SyntaxViewModel? Syntax
        {
            get => _syntax;
            set => this.RaiseAndSetIfChanged(ref _syntax, value);
        }

        private SemanticsViewModel? _semantics;
        public SemanticsViewModel? Semantics
        {
            get => _semantics;
            set => this.RaiseAndSetIfChanged(ref _semantics, value);
        }
    }
}
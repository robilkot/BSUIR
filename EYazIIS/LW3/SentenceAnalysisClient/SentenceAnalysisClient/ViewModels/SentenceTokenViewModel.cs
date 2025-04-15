using ReactiveUI;

namespace SentenceAnalysisClient.ViewModels
{
    public class SentenceTokenViewModel : ViewModelBase
    {
        public string Text { get; set; }
        public int StartIdx { get; set; }
        public int EndIdx { get; set; }

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
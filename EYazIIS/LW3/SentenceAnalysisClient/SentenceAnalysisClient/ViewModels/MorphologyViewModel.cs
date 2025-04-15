using SentenceAnalysisClient.Model;
using System.Collections.Generic;

namespace SentenceAnalysisClient.ViewModels
{
    public class MorphologyViewModel : ViewModelBase
    {
        public PartOfSpeech Pos { get; set; }
        public required string Lemma { get; set; }
        public required Dictionary<string, string> MorphInfo { get; set; }
    }
}

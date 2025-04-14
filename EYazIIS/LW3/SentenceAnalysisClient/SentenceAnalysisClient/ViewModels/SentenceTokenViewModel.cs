using SentenceAnalysisClient.Model;
using System.Collections.Generic;

namespace SentenceAnalysisClient.ViewModels
{
    public class SentenceTokenViewModel : ViewModelBase
    {
        public required string Text { get; set; }
        public int StartIdx { get; set; }
        public int EndIdx { get; set; }
        public PartOfSpeech? Pos { get; set; }
        public string? Lemma { get; set; }
        public Dictionary<string, string>? MorphInfo { get; set; }
    }
}
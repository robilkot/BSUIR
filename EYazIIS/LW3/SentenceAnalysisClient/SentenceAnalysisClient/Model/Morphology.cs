using System.Collections.Generic;

namespace SentenceAnalysisClient.Model
{
    public class Morphology
    {
        public PartOfSpeech? Pos { get; set; }
        public string? Lemma { get; set; }
        public Dictionary<string, string>? MorphInfo { get; set; }
    }
}

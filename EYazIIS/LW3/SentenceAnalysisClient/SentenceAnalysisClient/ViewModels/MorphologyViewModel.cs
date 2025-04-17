using Newtonsoft.Json;
using SentenceAnalysisClient.Model;
using System.Collections.Generic;

namespace SentenceAnalysisClient.ViewModels
{
    public class MorphologyViewModel : ViewModelBase
    {
        [JsonProperty]
        public PartOfSpeech Pos { get; set; }
        [JsonProperty]
        public required string Lemma { get; set; }
        [JsonProperty]
        public required Dictionary<string, string> MorphInfo { get; set; }
    }
}

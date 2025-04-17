using Newtonsoft.Json;
using ReactiveUI;
using SentenceAnalysisClient.Model;

namespace SentenceAnalysisClient.ViewModels
{
    public class NamedEntityViewModel : ViewModelBase
    {
        private string _text = string.Empty;
        [JsonProperty]
        public string Text
        {
            get => _text;
            set => this.RaiseAndSetIfChanged(ref _text, value);
        }

        private NERClass _nerClass;
        [JsonProperty]
        public NERClass NerClass
        {
            get => _nerClass;
            set => this.RaiseAndSetIfChanged(ref _nerClass, value);
        }

        private string? _normalForm = string.Empty;
        [JsonProperty]
        public string? NormalForm
        {
            get => _normalForm;
            set => this.RaiseAndSetIfChanged(ref _normalForm, value);
        }
    }
}
using Newtonsoft.Json;
using ReactiveUI;
using System.Collections.Generic;

namespace SentenceAnalysisClient.ViewModels.Semantics
{
    public class ObjectDescriptionViewModel : ViewModelBase
    {
        private string _text = string.Empty;
        [JsonProperty]
        public string Text
        {
            get => _text;
            set => this.RaiseAndSetIfChanged(ref _text, value);
        }

        private int _emphasis;
        [JsonProperty]
        public int Emphasis
        {
            get => _emphasis;
            set => this.RaiseAndSetIfChanged(ref _emphasis, value);
        }

        private string _description = string.Empty;
        [JsonProperty]
        public string Description
        {
            get => _description;
            set => this.RaiseAndSetIfChanged(ref _description, value);
        }

        private List<string>? _imagesUrls = null;
        [JsonProperty]
        public List<string>? ImagesUrls
        {
            get => _imagesUrls;
            set => this.RaiseAndSetIfChanged(ref _imagesUrls, value);
        }
    }
}
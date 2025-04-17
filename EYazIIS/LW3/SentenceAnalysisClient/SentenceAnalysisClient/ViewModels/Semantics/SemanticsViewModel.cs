using Newtonsoft.Json;
using ReactiveUI;

namespace SentenceAnalysisClient.ViewModels.Semantics
{
    public class SemanticsViewModel : ViewModelBase
    {
        private NamedEntityViewModel? _namedEntity;
        [JsonProperty]
        public NamedEntityViewModel? NamedEntity
        {
            get => _namedEntity;
            set => this.RaiseAndSetIfChanged(ref _namedEntity, value);
        }

        private ObjectDescriptionViewModel? _objectDescription;
        [JsonProperty]
        public ObjectDescriptionViewModel? ObjectDescription
        {
            get => _objectDescription;
            set => this.RaiseAndSetIfChanged(ref _objectDescription, value);
        }
    }
}
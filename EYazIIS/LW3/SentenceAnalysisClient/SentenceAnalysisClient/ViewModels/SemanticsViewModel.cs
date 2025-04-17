using Newtonsoft.Json;
using ReactiveUI;

namespace SentenceAnalysisClient.ViewModels
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

        //    private ObjectDescriptionDto? _objectDescription;
        //    [JsonProperty]
        //    public ObjectDescriptionDto? ObjectDescription
        //    {
        //        get => _objectDescription;
        //        set => this.RaiseAndSetIfChanged(ref _objectDescription, value);
        //    }
        //}
    }
}
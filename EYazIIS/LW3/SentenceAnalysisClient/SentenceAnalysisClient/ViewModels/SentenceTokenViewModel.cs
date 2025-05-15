using Newtonsoft.Json;
using ReactiveUI;
using SentenceAnalysisClient.Model;
using SentenceAnalysisClient.ViewModels.Semantics;
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http.Json;
using System;
using System.Reactive;
using System.Threading.Tasks;
using System.Reactive.Linq;

namespace SentenceAnalysisClient.ViewModels
{
    public class SentenceTokenViewModel : ViewModelBase
    {
        [JsonProperty]
        public required string Text { get; set; }

        private MorphologyViewModel? _morphology;
        [JsonProperty]
        public MorphologyViewModel? Morphology
        {
            get => _morphology;
            set => this.RaiseAndSetIfChanged(ref _morphology, value);
        }

        private SyntaxViewModel? _syntax;
        [JsonProperty]
        public SyntaxViewModel? Syntax
        {
            get => _syntax;
            set => this.RaiseAndSetIfChanged(ref _syntax, value);
        }

        private SemanticsViewModel? _semantics;
        [JsonProperty]
        public SemanticsViewModel? Semantics
        {
            get => _semantics;
            set => this.RaiseAndSetIfChanged(ref _semantics, value);
        }

        public ReactiveCommand<Unit, Unit> ParseSemanticsObjectInfoCommand;

        public SentenceTokenViewModel()
        {
            var canParseSemantics = this.WhenAnyValue(
                x => x.Semantics,
                semantics => semantics is not null && semantics.ObjectDescription is not null
                );

            ParseSemanticsObjectInfoCommand = ReactiveCommand.CreateFromTask(ParseSemanticsObjectInfo, canParseSemantics);
        }

        private async Task ParseSemanticsObjectInfo()
        {
            if (Semantics is not null && Semantics.ObjectDescription is not null)
                return;

            try
            {
                var response = await _httpClient.PostAsJsonAsync("get-word-semantics", new TextRequest(Text));
                response.EnsureSuccessStatusCode();

                var result = await response.Content.ReadFromJsonAsync<ObjectDescriptionDto>();

                Semantics!.ObjectDescription = new()
                {
                    Text = result.text,
                    Description = result.description,
                    ImagesUrls = result.images_urls,
                    Emphasis = result.emphasis,
                };

                this.RaisePropertyChanged(nameof(Semantics));
            }
            catch (Exception ex)
            {
                Debug.WriteLine($"Error: {ex.Message}", "Error");
            }
        }
    }
}
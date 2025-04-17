using DynamicData.Binding;
using Newtonsoft.Json;
using ReactiveUI;
using SentenceAnalysisClient.Model;
using SentenceAnalysisClient.ViewModels.Semantics;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Net.Http.Json;
using System.Reactive;
using System.Reactive.Linq;
using System.Threading.Tasks;

namespace SentenceAnalysisClient.ViewModels
{
    public class SentenceViewModel : ViewModelBase
    {
        private string _text = string.Empty;
        [JsonProperty]
        public string Text
        {
            get => _text;
            set => this.RaiseAndSetIfChanged(ref _text, value);
        }

        private List<SentenceTokenViewModel> _tokens = [];
        [JsonProperty]
        public List<SentenceTokenViewModel> Tokens
        {
            get => _tokens;
            set => this.RaiseAndSetIfChanged(ref _tokens, value);
        }

        private bool _isMorphologyVisible;
        [JsonProperty]
        public bool IsMorphologyVisible
        {
            get => _isMorphologyVisible;
            set => this.RaiseAndSetIfChanged(ref _isMorphologyVisible, value);
        }

        private bool _isSyntaxVisible;
        [JsonProperty]
        public bool IsSyntaxVisible
        {
            get => _isSyntaxVisible;
            set => this.RaiseAndSetIfChanged(ref _isSyntaxVisible, value);
        }

        private bool _isSemanticsVisible;
        [JsonProperty]
        public bool IsSemanticsVisible
        {
            get => _isSemanticsVisible;
            set => this.RaiseAndSetIfChanged(ref _isSemanticsVisible, value);
        }

        public ReactiveCommand<Unit, Unit> ParseSyntaxCommand { get; }
        public ReactiveCommand<Unit, Unit> ParseMorphologyCommand { get; }
        public ReactiveCommand<Unit, Unit> ParseSemanticsCommand { get; }

        public SentenceViewModel()
        {
            var canParseSyntax = this.WhenChanged(x => x.Tokens, (vm, tokens) => tokens?.Any(t => t.Syntax == null) ?? false);
            ParseSyntaxCommand = ReactiveCommand.CreateFromTask(ParseSyntax, canParseSyntax);
            ParseSyntaxCommand.CanExecute.Subscribe(canExecute => IsSyntaxVisible = !canExecute && Tokens != null);

            var canParseMorpology = this.WhenChanged(x => x.Tokens, (vm, tokens) => tokens?.Any(t => t.Morphology == null) ?? false);
            ParseMorphologyCommand = ReactiveCommand.CreateFromTask(ParseMorphology, canParseMorpology);
            ParseMorphologyCommand.CanExecute.Subscribe(canExecute => IsMorphologyVisible = !canExecute && Tokens != null);

            var canParseSemantics = this.WhenChanged(x => x.Tokens, (vm, tokens) => tokens?.Any(t => t.Semantics == null) ?? false);
            ParseSemanticsCommand = ReactiveCommand.CreateFromTask(ParseSemantics, canParseSemantics);
            ParseSemanticsCommand.CanExecute.Subscribe(canExecute => IsSemanticsVisible = !canExecute && Tokens != null);
        }

        private async Task ParseSemantics()
        {
            try
            {
                var request = new SentenceRequest(Text);

                var response = await _httpClient.PostAsJsonAsync("parse-semantics", request);
                response.EnsureSuccessStatusCode();

                var result = await response.Content.ReadFromJsonAsync<SemanticsResponse>();

                foreach (var (First, Second) in Tokens.Zip(result!.tokens))
                {
                    var namedEntity = Second.named_entity_info == null ? null : new NamedEntityViewModel()
                    {
                        NerClass = Second.named_entity_info.ner_class,
                        Text = Second.named_entity_info.text,
                        NormalForm = Second.named_entity_info.normal_form,
                    };

                    var objectDescription = Second.object_description == null ? null : new ObjectDescriptionViewModel()
                    {
                        Text = Second.object_description.text,
                        Emphasis = Second.object_description.emphasis,
                        Description = Second.object_description.description,
                        ImagesUrls = Second.object_description.images_urls,
                    };

                    First.Semantics = new()
                    {
                        NamedEntity = namedEntity,
                        ObjectDescription = objectDescription,
                    };
                }

                this.RaisePropertyChanged(nameof(Tokens));
            }
            catch (Exception ex)
            {
                Debug.WriteLine($"Error: {ex.Message}", "Error");
            }
        }

        private async Task ParseSyntax()
        {
            try
            {
                var request = new SentenceRequest(Text);

                var response = await _httpClient.PostAsJsonAsync("parse-syntax", request);
                response.EnsureSuccessStatusCode();

                var result = await response.Content.ReadFromJsonAsync<SyntaxResponse>();

                Dictionary<string, SentenceTokenViewModel> idToTokens = result!.tokens.Zip(Tokens).ToDictionary(pair => pair.First.id, pair => pair.Second); ;

                foreach (var (syntaxToken, sentenceToken) in result.tokens.Zip(Tokens))
                {
                    idToTokens.TryGetValue(syntaxToken.head_id, out var headToken);

                    sentenceToken.Syntax = new()
                    {
                        HeadToken = headToken,
                        Token = sentenceToken,
                        Relation = syntaxToken.relation,
                    };
                }

                this.RaisePropertyChanged(nameof(Tokens));
            }
            catch (Exception ex)
            {
                Debug.WriteLine($"Error: {ex.Message}", "Error");
            }
        }

        private async Task ParseMorphology()
        {
            try
            {
                var request = new SentenceRequest(Text);

                var response = await _httpClient.PostAsJsonAsync("parse-morphology", request);
                response.EnsureSuccessStatusCode();

                var result = await response.Content.ReadFromJsonAsync<MorphologyResponse>();

                foreach (var (First, Second) in Tokens.Zip(result!.tokens))
                {
                    First.Morphology = new()
                    {
                        Pos = Second.pos,
                        Lemma = Second.lemma,
                        MorphInfo = Second.morph_info,
                    };
                }

                this.RaisePropertyChanged(nameof(Tokens));
            }
            catch (Exception ex)
            {
                Debug.WriteLine($"Error: {ex.Message}", "Error");
            }
        }
    }
}
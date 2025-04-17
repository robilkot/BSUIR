using Newtonsoft.Json;
using ReactiveUI;
using SentenceAnalysisClient.Model;
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
    public class TextViewModel : ViewModelBase
    {
        private string _text = string.Empty;
        [JsonProperty]
        public string Text
        {
            get => _text;
            set => this.RaiseAndSetIfChanged(ref _text, value);
        }

        private List<SentenceViewModel>? _sentences = null;
        [JsonProperty]
        public List<SentenceViewModel>? Sentences
        {
            get => _sentences;
            set => this.RaiseAndSetIfChanged(ref _sentences, value);
        }

        public ReactiveCommand<Unit, Unit> SplitIntoSentencesCommand { get; }

        public TextViewModel()
        {
            this.ObservableForProperty(vm => vm.Text).Subscribe(text => Sentences = null);

            var canSplit = this.WhenAnyValue(
                x => x.Sentences,
                sents => sents == null || sents.Count == 0);

            SplitIntoSentencesCommand = ReactiveCommand.CreateFromTask(SplitIntoSentences, canSplit);
        }

        private async Task SplitIntoSentences()
        {
            try
            {
                var response = await _httpClient.PostAsJsonAsync("text-to-sentences", new TextRequest(Text));
                response.EnsureSuccessStatusCode();

                var result = await response.Content.ReadFromJsonAsync<SentencesResponse>();

                List<SentenceViewModel> newSentences = result!.sentences.Select(sentence =>
                    new SentenceViewModel
                    {
                        Text = sentence.text,
                        Tokens = sentence.tokens.Select(t => new SentenceTokenViewModel()
                        {
                            Text = Text[t.start_idx..t.end_idx],
                        })
                        .ToList()
                    }).ToList();

                Sentences = newSentences;
            }
            catch (Exception ex)
            {
                Debug.WriteLine($"Error: {ex.Message}", "Error");
            }
        }
    }
}
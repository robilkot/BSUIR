using DynamicData;
using ReactiveUI;
using SentenceAnalysisClient.Model;
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Diagnostics;
using System.Linq;
using System.Net.Http.Json;
using System.Reactive;
using System.Threading.Tasks;

namespace SentenceAnalysisClient.ViewModels
{
    public class TextViewModel : ViewModelBase
    {
        private string _text = string.Empty;
        public string Text
        {
            get => _text;
            set
            {
                this.RaiseAndSetIfChanged(ref _text, value);
                Sentences = null;
            }
        }

        private List<SentenceViewModel>? _sentences;
        public List<SentenceViewModel>? Sentences
        {
            get => _sentences;
            set => this.RaiseAndSetIfChanged(ref _sentences, value);
        }

        public ReactiveCommand<Unit, Unit> SplitIntoSentencesCommand { get; }

        public TextViewModel()
        {
            var canSplit = this.WhenAnyValue(
                x => x.Sentences,
                sents => sents == null || sents.Count == 0);

            SplitIntoSentencesCommand = ReactiveCommand.CreateFromTask(SplitIntoSentences, canSplit);
        }

        private async Task SplitIntoSentences()
        {
            try
            {
                var response = await _httpClient.PostAsJsonAsync("text-to-sentences", new { text = Text });
                response.EnsureSuccessStatusCode();

                var result = await response.Content.ReadFromJsonAsync<SentencesResponse>();

                List<SentenceViewModel> newSentences = result.Sentences.Select(sentence =>
                    new SentenceViewModel
                    {
                        Text = sentence.Text,
                        Tokens = sentence.Tokens.Select(t => new SentenceTokenViewModel
                        {
                            Text = Text[t.start_idx..t.end_idx],
                            StartIdx = t.start_idx,
                            EndIdx = t.end_idx,
                            Pos = t.pos,
                            Lemma = t.lemma,
                            MorphInfo = t.morph_info
                        })
                        .ToList()
                    }).ToList();

                Sentences = newSentences;
            }
            catch (Exception ex)
            {
                Debug.WriteLine($"Error: {ex.Message}", "Error");
                //await MessageBox.Show(GetParentWindow(), $"Error: {ex.Message}", "Error");
            }
        }
    }
}
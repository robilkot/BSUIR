using ReactiveUI;
using SentenceAnalysisClient.Model;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Net.Http.Json;
using System.Reactive;
using System.Threading.Tasks;

namespace SentenceAnalysisClient.ViewModels
{
    public class SentenceViewModel : ViewModelBase
    {
        private string _text;
        public string Text
        {
            get => _text;
            set => this.RaiseAndSetIfChanged(ref _text, value);
        }

        private List<SentenceTokenViewModel> _tokens;
        public List<SentenceTokenViewModel> Tokens
        {
            get => _tokens;
            set => this.RaiseAndSetIfChanged(ref _tokens, value);
        }

        private List<SyntaxTokenResponse>? _syntaxTokens = null;
        public List<SyntaxTokenResponse>? SyntaxTokens
        {
            get => _syntaxTokens;
            set => this.RaiseAndSetIfChanged(ref _syntaxTokens, value);
        }

        public ReactiveCommand<Unit, Unit> ParseSyntaxCommand { get; }

        public SentenceViewModel()
        {
            var canParse = this.WhenAnyValue(
                x => x.SyntaxTokens,
                tokens => tokens == null || tokens.Count == 0);

            ParseSyntaxCommand = ReactiveCommand.CreateFromTask(ParseSyntax, canParse);
        }

        private async Task ParseSyntax()
        {
            try
            {
                var request = new SentenceRequest(Text, Tokens.Select(token => new TokenDto(token.StartIdx, token.EndIdx, token.Pos, token.Lemma, token.MorphInfo)).ToList());

                var response = await _httpClient.PostAsJsonAsync("parse-syntax", request);
                response.EnsureSuccessStatusCode();
                var js = await response.Content.ReadAsStringAsync();

                var result = await response.Content.ReadFromJsonAsync<SentenceResponse>();
                SyntaxTokens = result.Syntax.Tokens;
            }
            catch (Exception ex)
            {
                Debug.WriteLine($"Error: {ex.Message}", "Error");
                //await MessageBox.Show(GetParentWindow(), $"Error: {ex.Message}", "Error");
            }
        }
    }
}
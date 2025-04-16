using ReactiveUI;
using System.Collections.ObjectModel;
using System.Reactive;

namespace SentenceAnalysisClient.ViewModels
{
    public class MainWindowViewModel : ViewModelBase
    {
        private string _newText = string.Empty;
        public string NewText
        {
            get => _newText;
            set => this.RaiseAndSetIfChanged(ref _newText, value);
        }

        private TextViewModel? _selectedText = null;
        public TextViewModel? SelectedText
        {
            get => _selectedText;
            set => this.RaiseAndSetIfChanged(ref _selectedText, value);
        }

        public ObservableCollection<TextViewModel> Texts { get; } = [];


        public ReactiveCommand<Unit, Unit> AddTextCommand { get; }
        public ReactiveCommand<TextViewModel, Unit> DeleteTextCommand { get; }

        public MainWindowViewModel()
        {
            var canAddText = this.WhenAnyValue(
                x => x.NewText,
                newText => !string.IsNullOrWhiteSpace(newText)
                );

            AddTextCommand = ReactiveCommand.Create(AddText, canAddText);

            DeleteTextCommand = ReactiveCommand.Create<TextViewModel>(DeleteText);

            Texts = [
                new() {
                    Text = "Мы написали новый текст! Давайте его протестируем."
                },
                new() {
                    Text = "Друзья, поступайте на ФИТУ! Тут классно и очень весело, правда, очень весело. Не обманываю вас, потому что я сам студент этого замечательного факультета."
                }
                ];
        }

        private void DeleteText(TextViewModel model)
        {
            Texts.Remove(model);
        }
        private void AddText()
        {
            Texts.Add(new() { Text = NewText });
            NewText = string.Empty;
        }
    }
}
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

        private TextViewModel? _selectedText;
        public TextViewModel? SelectedText
        {
            get => _selectedText;
            set => this.RaiseAndSetIfChanged(ref _selectedText, value);
        }

        public ObservableCollection<TextViewModel> Texts { get; } = [];


        public ReactiveCommand<Unit, Unit> AddTextCommand { get; }

        public MainWindowViewModel()
        {
            var canAddText = this.WhenAnyValue(
                x => x.NewText,
                newText => !string.IsNullOrWhiteSpace(newText)
                );

            AddTextCommand = ReactiveCommand.Create(AddText, canAddText);

            Texts = [
                new() {
                    Text = "Я не хочу учиться. Я хочу жениться!"
                },
                new() {
                    Text = "Поступайте на ФИТУ! Тут классно. Тут очень весело. Не обманываю"
                }
                ];
        }

        private void AddText()
        {
            Texts.Add(new() { Text = NewText });
            NewText = string.Empty;
        }
    }
}
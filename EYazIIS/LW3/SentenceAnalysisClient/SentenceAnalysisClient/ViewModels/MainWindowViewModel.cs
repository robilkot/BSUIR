using Avalonia;
using Avalonia.Controls.ApplicationLifetimes;
using Avalonia.Platform.Storage;
using Avalonia.Threading;
using Newtonsoft.Json;
using ReactiveUI;
using System;
using System.Collections.ObjectModel;
using System.Diagnostics;
using System.IO;
using System.Net.Http.Json;
using System.Reactive;
using System.Runtime.Serialization.Formatters.Binary;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Threading.Tasks;
using System.Xml;

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
        public ReactiveCommand<Unit, Unit> SaveCommand { get; }
        public ReactiveCommand<Unit, Unit> OpenCommand { get; }
        public ReactiveCommand<TextViewModel, Unit> DeleteTextCommand { get; }

        public MainWindowViewModel()
        {
            var canAddText = this.WhenAnyValue(
                x => x.NewText,
                newText => !string.IsNullOrWhiteSpace(newText)
                );

            AddTextCommand = ReactiveCommand.Create(AddText, canAddText);
            DeleteTextCommand = ReactiveCommand.Create<TextViewModel>(DeleteText);

            var canSaveText = this.WhenAnyValue(
                x => x.SelectedText,
                vm => (vm as TextViewModel) != null
                );

            SaveCommand = ReactiveCommand.CreateFromTask(Save, canSaveText);
            OpenCommand = ReactiveCommand.CreateFromTask(Open);

            Texts = [
                new() {
                    Text = "В БГУИР прибыл важный гость, Тимур Маркович."
                },
                new() {
                    Text = "Друзья, поступайте на ФИТУ! Тут классно и очень весело, правда, очень весело. Не обманываю вас, потому что я сам студент этого замечательного факультета."
                },
                new() {
                    Text = "Задача организации, в особенности же сложившаяся структура организации способствует подготовки и реализации систем массового участия. Разнообразный и богатый опыт новая модель организационной деятельности требуют от нас анализа соответствующий условий активизации. Значимость этих проблем настолько очевидна, что начало повседневной работы по формированию позиции требуют от нас анализа соответствующий условий активизации. Не следует, однако забывать, что новая модель организационной деятельности влечет за собой процесс внедрения и модернизации существенных финансовых и административных условий."
                }
                ];


            //Task.Run(() =>
            //{
            //    var text = Open<TextViewModel>("C:/Users/robilkot/Desktop/a.json");
            //    Dispatcher.UIThread.Post(() =>
            //    {
            //        Texts.Add(text);
            //        SelectedText = text;
            //    });
            //});
        }

        private T Open<T>(string filename)
        {
            var fileContent = File.ReadAllText(filename);

            var settings = new JsonSerializerSettings
            {
                Formatting = Newtonsoft.Json.Formatting.Indented,
                PreserveReferencesHandling = PreserveReferencesHandling.Objects
            };
            var result = JsonConvert.DeserializeObject<T>(fileContent, settings);

            return result;
        }

        private async Task Open()
        {
            try
            {
                var window = ((ClassicDesktopStyleApplicationLifetime)App.Current!.ApplicationLifetime!).MainWindow;

                var files = await window!.StorageProvider.OpenFilePickerAsync(new FilePickerOpenOptions
                {
                    Title = "Открыть текст",
                    AllowMultiple = false
                });

                if (files.Count >= 1)
                {
                    var path = files[0].Path.AbsolutePath;

                    var newText = Open<TextViewModel>(path);

                    Texts.Add(newText!);
                    SelectedText = newText;
                }
            }
            catch (Exception ex)
            {
                Debug.WriteLine(ex);
            }
        }

        private async Task Save()
        {
            try
            {
                var window = ((ClassicDesktopStyleApplicationLifetime)App.Current!.ApplicationLifetime!).MainWindow;

                var file = await window!.StorageProvider.SaveFilePickerAsync(new FilePickerSaveOptions
                {
                    Title = "Сохранить текст"
                });

                if (file is not null)
                {
                    var settings = new JsonSerializerSettings
                    {
                        Formatting = Newtonsoft.Json.Formatting.Indented,
                        PreserveReferencesHandling = PreserveReferencesHandling.Objects
                    };

                    var json = JsonConvert.SerializeObject(SelectedText, settings);
                    await File.WriteAllTextAsync(file.Path.AbsolutePath, json);
                }
            }
            catch (Exception ex)
            {
                Debug.WriteLine(ex);
            }
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
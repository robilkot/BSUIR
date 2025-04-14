using Avalonia;
using Avalonia.Controls;
using Avalonia.Markup.Xaml;
using SentenceAnalysisClient.ViewModels;
using System;
using System.Collections.ObjectModel;
using System.Linq;

namespace SentenceAnalysisClient.Views
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
#if DEBUG
            this.AttachDevTools();
#endif

            // Handle when a sentence's syntax parsing is complete
            this.FindControl<ItemsControl>("SentencesList")?.GetObservable(ItemsControl.ItemsSourceProperty)
                .Subscribe(items =>
                {
                    if (items is ObservableCollection<SentenceViewModel> sentences)
                    {
                        foreach (var sentence in sentences.Where(s => s.SyntaxTokens is not null))
                        {
                            RenderSyntaxVisualization(sentence);
                        }
                    }
                });
        }
        private void InitializeComponent()
        {
            AvaloniaXamlLoader.Load(this);
        }

        private void RenderSyntaxVisualization(SentenceViewModel sentence)
        {

        }
    }
}
using Avalonia.Controls;
using Avalonia.Metadata;
using Avalonia.Threading;
using SentenceAnalysisClient.ViewModels;
using System.Threading;
using System.Threading.Tasks;

namespace SentenceAnalysisClient.Views.Sentence;

public partial class TokenSemanticsView : UserControl
{
    private bool _carouselRotationDirection = true;
    private CancellationTokenSource _cts = new();

    public TokenSemanticsView()
    {
        InitializeComponent();

        slides.AttachedToVisualTree += Slides_AttachedToVisualTree;
        slides.DetachedFromVisualTree += Slides_DetachedFromVisualTree;

        tooltip.Loaded += TooltipShown;
    }

    private void TooltipShown(object? sender, Avalonia.Interactivity.RoutedEventArgs e)
    {
        if (DataContext is not SentenceTokenViewModel vm)
            return;

        vm.ParseSemanticsObjectInfoCommand.Execute();
    }

    private void Slides_DetachedFromVisualTree(object? sender, Avalonia.VisualTreeAttachmentEventArgs e)
    {
        _cts.Cancel();
    }

    private async void Slides_AttachedToVisualTree(object? sender, Avalonia.VisualTreeAttachmentEventArgs e)
    {
        _cts = new();

        try
        {
            await Task.Run(async () =>
            {
                while (true)
                {
                    await Task.Delay(2000, _cts.Token);

                    if (slides.SelectedIndex == slides.ItemCount - 1 || slides.SelectedIndex == 0)
                    {
                        _carouselRotationDirection = !_carouselRotationDirection;
                    }

                    if (_carouselRotationDirection)
                    {
                        Dispatcher.UIThread.Post(slides.Next);
                    }
                    else
                    {
                        Dispatcher.UIThread.Post(slides.Previous);
                    }
                }
            }, _cts.Token);
        }
        catch (TaskCanceledException) { }
    }
}
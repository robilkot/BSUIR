using Avalonia.Controls;
using Avalonia.Threading;
using System.Threading.Tasks;
using System.Threading;

namespace LW5.Views;

public partial class UserMessageView : UserControl
{
    private bool _carouselRotationDirection = true;
    private CancellationTokenSource _cts = new();

    public UserMessageView()
    {
        InitializeComponent();

        slides.AttachedToVisualTree += Slides_AttachedToVisualTree;
        slides.DetachedFromVisualTree += Slides_DetachedFromVisualTree;
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
                        Dispatcher.UIThread.Post(() => slides.Next());
                    }
                    else
                    {
                        Dispatcher.UIThread.Post(() => slides.Previous());
                    }
                }
            }, _cts.Token);
        }
        catch (TaskCanceledException) { }
    }
}
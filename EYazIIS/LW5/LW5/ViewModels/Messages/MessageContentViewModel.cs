using Avalonia.Media.Imaging;
using ReactiveUI;
using System;
using System.Collections.ObjectModel;

namespace LW5.ViewModels.Messages;

public class MessageContentViewModel : ViewModelBase
{
    private ObservableCollection<Bitmap>? _images;
    public ObservableCollection<Bitmap>? Images
    {
        get => _images;
        set => this.RaiseAndSetIfChanged(ref _images, value);
    }

    private string? _text;
    public string? Text
    {
        get => _text;
        set => this.RaiseAndSetIfChanged(ref _text, value);
    }

    private ObservableCollection<Uri>? _links;
    public ObservableCollection<Uri>? Links
    {
        get => _links;
        set => this.RaiseAndSetIfChanged(ref _links, value);
    }
}

using ReactiveUI;
using System;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;

namespace LW5.ViewModels.Messages;

[DataContract]
public class MessageContentViewModel : ViewModelBase
{
    private ObservableCollection<string> _images = [];
    [DataMember]
    public ObservableCollection<string> Images
    {
        get => _images;
        set => this.RaiseAndSetIfChanged(ref _images, value);
    }

    private string? _text;
    [DataMember]
    public string? Text
    {
        get => _text;
        set => this.RaiseAndSetIfChanged(ref _text, value);
    }

    private ObservableCollection<Uri> _links = [];
    [DataMember]
    public ObservableCollection<Uri> Links
    {
        get => _links;
        set => this.RaiseAndSetIfChanged(ref _links, value);
    }
}

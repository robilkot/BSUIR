using ReactiveUI;
using System;
using System.Runtime.Serialization;

namespace LW5.ViewModels.Messages;

[DataContract]
public class MessageMetadataViewModel : MessageViewModel
{
    private DateTimeOffset _sent;
    [DataMember]
    public DateTimeOffset Sent
    {
        get => _sent;
        set => this.RaiseAndSetIfChanged(ref _sent, value);
    }

    private UserViewModel _sender;
    [DataMember]
    public UserViewModel Sender
    {
        get => _sender;
        set => this.RaiseAndSetIfChanged(ref _sender, value);
    }
}

using ReactiveUI;
using System;

namespace LW5.ViewModels.Messages;

public class MessageMetadataViewModel : MessageViewModel
{
    private DateTimeOffset _sent;
    public DateTimeOffset Sent
    {
        get => _sent;
        set => this.RaiseAndSetIfChanged(ref _sent, value);
    }

    private MessageSenderViewModel _sender;
    public MessageSenderViewModel Sender
    {
        get => _sender;
        set => this.RaiseAndSetIfChanged(ref _sender, value);
    }
}

using Avalonia.Media.Imaging;
using ReactiveUI;
using System;

namespace LW5.ViewModels.Messages;

public class UserMessageViewModel : MessageViewModel
{
    private MessageContentViewModel _content;
    public MessageContentViewModel Content
    {
        get => _content;
        set => this.RaiseAndSetIfChanged(ref _content, value);
    }

    private MessageMetadataViewModel _metadata;
    public MessageMetadataViewModel Metadata
    {
        get => _metadata;
        set => this.RaiseAndSetIfChanged(ref _metadata, value);
    }

    private MessageReactionsViewModel? _reactions;
    public MessageReactionsViewModel? Reactions
    {
        get => _reactions;
        set => this.RaiseAndSetIfChanged(ref _reactions, value);
    }

    public UserMessageViewModel()
    {
        Content = new()
        {
            Text = "Text content",
            Links = [
                new("https://yandex.ru/"),
                new("https://google.com/"),
                ],
            Images = [
                new("E:\\archive\\архив\\15653847220781.png"),
                new("E:\\archive\\архив\\burger.png")
                ],
        };
        Metadata = new()
        {
            Sender = new()
            {
                Name = "Sender name",
            },
            Sent = DateTimeOffset.Now
        };
        Reactions = new()
        {
        };
    }
}

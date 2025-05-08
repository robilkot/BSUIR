using AsyncImageLoader;
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
                "https://i.pinimg.com/236x/c6/2e/47/c62e47ccce4e8e568c9c7e381032bde9.jpg",
                "https://images.pexels.com/photos/1170986/pexels-photo-1170986.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"
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

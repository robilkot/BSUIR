using Avalonia.Controls;
using LW5.Models;
using ReactiveUI;
using System;
using System.Linq;
using System.Reactive;
using System.Reactive.Linq;

namespace LW5.ViewModels.Messages;

public class UserMessageViewModel : MessageViewModel
{
    private MessageStatus _status;
    public MessageStatus Status
    {
        get => _status;
        set => this.RaiseAndSetIfChanged(ref _status, value);
    }
    private string? _errorMsg;
    public string? ErrorMsg
    {
        get => _errorMsg;
        set => this.RaiseAndSetIfChanged(ref _errorMsg, value);
    }

    private MessageContentViewModel _content;
    public MessageContentViewModel Content
    {
        get => _content;
        set => this.RaiseAndSetIfChanged(ref _content, value);
    }

    private MessageMetadataViewModel _metadata = new();
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

    private ReactiveCommand<UserMessageViewModel, Unit>? _resendCommand;
    public ReactiveCommand<UserMessageViewModel, Unit>? ResendCommandInternal
    {
        get => _resendCommand;
        set => this.RaiseAndSetIfChanged(ref _resendCommand, value);
    }
    public ReactiveCommand<Unit, Unit> ResendCommand { get; }

    public UserMessageViewModel()
    {
        if (Design.IsDesignMode)
        {

            Content = new()
            {
                Text = "Привет, я кинопомощник. Помогу найти фильм, дам ссылку на источники информации, покажу актуальные фото по теме.",
                Links = [
                        new("https://example.com/"),
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
                    Name = "Кинопомощник"
                },
                Sent = DateTimeOffset.Now
            };
            Reactions = new() { };
        }

        ResendCommand = ReactiveCommand.Create(Resend);
    }

    public UserMessageViewModel(Message msg)
    {
        Content = new()
        {
            Text = msg.content.text,
            Links = new(msg.content.links.Select(str => new Uri(str))),
            Images = new(msg.content.images),
        };
        Metadata = new()
        {
            Sender = new()
            {
                Name = msg.metadata.sender.name,
                About = msg.metadata.sender.about,
            },
            Sent = msg.metadata.sent,
        };
        Reactions = new();
    }

    private void Resend()
    {
        ResendCommandInternal?.Execute(this);
    }

    public Message ToModel()
    {
        return new(
            new([.. Content.Images], Content.Links.Select(uri => uri.ToString()).ToList(), Content.Text),
            new(Metadata.Sent, new(Metadata.Sender.Name, Metadata.Sender.About)),
            new(Reactions?.Rating ?? MessageRating.None)
            );
    }
}

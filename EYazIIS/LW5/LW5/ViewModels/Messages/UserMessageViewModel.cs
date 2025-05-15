using Avalonia.Controls;
using Avalonia.Threading;
using LW5.Models;
using ReactiveUI;
using System;
using System.Diagnostics;
using System.Linq;
using System.Reactive;
using System.Reactive.Linq;
using System.Runtime.Serialization;

namespace LW5.ViewModels.Messages;

[DataContract]
public class UserMessageViewModel : MessageViewModel
{
    private MessageStatus _status;
    [DataMember]
    public MessageStatus Status
    {
        get => _status;
        set => this.RaiseAndSetIfChanged(ref _status, value);
    }

    private bool _saved;
    [DataMember]
    public bool Saved
    {
        get => _saved;
        set => this.RaiseAndSetIfChanged(ref _saved, value);
    }

    private string? _errorMsg;
    [DataMember]
    public string? ErrorMsg
    {
        get => _errorMsg;
        set => this.RaiseAndSetIfChanged(ref _errorMsg, value);
    }

    private MessageContentViewModel _content;
    [DataMember]
    public MessageContentViewModel Content
    {
        get => _content;
        set => this.RaiseAndSetIfChanged(ref _content, value);
    }

    private MessageMetadataViewModel _metadata = new();
    [DataMember]
    public MessageMetadataViewModel Metadata
    {
        get => _metadata;
        set => this.RaiseAndSetIfChanged(ref _metadata, value);
    }

    private MessageReactionsViewModel? _reactions;
    [DataMember]
    public MessageReactionsViewModel? Reactions
    {
        get => _reactions;
        set => this.RaiseAndSetIfChanged(ref _reactions, value);
    }


    [IgnoreDataMember]
    public ReactiveCommand<Unit, Unit> ResendCommand { get; }

    [IgnoreDataMember]
    public ReactiveCommand<bool, Unit> SaveCommand { get; }

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
        SaveCommand = ReactiveCommand.Create<bool>(Save);
    }

    public UserMessageViewModel(Message msg) : this()
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
        Dialog?.ResendMessageCommand.Execute(this);
    }

    private void Save(bool save)
    {
        if(save)
        {
            Dialog?.SaveMessageCommand.Execute(this);
        }
        else
        {
            Dialog?.UnsaveMessageCommand.Execute(this);
        }
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

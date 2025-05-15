using LW5.Services;
using LW5.ViewModels.Messages;
using ReactiveUI;
using System;
using System.Collections.ObjectModel;
using System.Linq;
using System.Reactive;
using System.Runtime.Serialization;
using System.Threading.Tasks;

namespace LW5.ViewModels;

[DataContract]
public class DialogViewModel : ViewModelBase
{
    [IgnoreDataMember]
    public DialogService DialogService { get; set; }

    [IgnoreDataMember]
    public SettingsViewModel Settings { get; set; }

    [IgnoreDataMember]
    public BookmarksViewModel Bookmarks { get; set; }


    private string _input = "";
    [DataMember]
    public string Input
    {
        get => _input;
        set => this.RaiseAndSetIfChanged(ref _input, value);
    }

    private UserViewModel _helper_sender = new()
    {
        Name = "Кинопомощник",
        About = "Помогает искать информацию о фильмах"
    };

    [IgnoreDataMember]
    public ReactiveCommand<string, Unit> SendMessageCommand { get; }

    [IgnoreDataMember]
    public ReactiveCommand<UserMessageViewModel, Unit> ResendMessageCommand { get; }

    [IgnoreDataMember]
    public ReactiveCommand<UserMessageViewModel, Unit> SaveMessageCommand { get; }

    [IgnoreDataMember]
    public ReactiveCommand<UserMessageViewModel, Unit> UnsaveMessageCommand { get; }


    private ObservableCollection<MessageViewModel> _messages = [];
    [DataMember]
    public ObservableCollection<MessageViewModel> Messages
    {
        get => _messages;
        set => this.RaiseAndSetIfChanged(ref _messages, value);
    }

    public DialogViewModel()
    {
        SaveMessageCommand = ReactiveCommand.CreateFromTask<UserMessageViewModel>(SaveMessage);
        UnsaveMessageCommand = ReactiveCommand.CreateFromTask<UserMessageViewModel>(UnsaveMessage);

        SendMessageCommand = ReactiveCommand.CreateFromTask<string>(SendMessage);
        ResendMessageCommand = ReactiveCommand.CreateFromTask<UserMessageViewModel>(ResendMessage);
    }

    public void Init()
    {
        if (Messages.Count == 0)
        {
            Messages = [
            new ServiceMessageViewModel(),
            new UserMessageViewModel()
            {
                Status = Models.MessageStatus.Delivered,
                Content = new()
                {
                    Text = "Привет, я кинопомощник. Помогу найти фильм, дам ссылку на источники информации, покажу актуальные фото по теме.",
                    Links = [
                        new("https://www.kinopoisk.ru/"),
                        new("https://google.com/"),
                        ],
                    Images = [
                        "https://upload.wikimedia.org/wikipedia/ru/9/93/Pulp_Fiction.jpg",
                        "https://upload.wikimedia.org/wikipedia/ru/d/de/Movie_poster_the_shawshank_redemption.jpg",
                        "https://upload.wikimedia.org/wikipedia/ru/e/e3/%D0%9F%D0%BE%D1%81%D1%82%D0%B5%D1%80_%D0%BA_%D1%84%D0%B8%D0%BB%D1%8C%D0%BC%D1%83_%C2%AB%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D1%8B%D0%B5_%D0%BE%D0%B3%D0%BD%D0%B8%C2%BB.jpg"
                        ],
                },
                Metadata = new()
                {
                    Sender = _helper_sender,
                    Sent = DateTimeOffset.Now
                },
                Reactions = null,
            }
        ];
        }

        Messages = [..Messages.
            Where(m => m is not UserMessageViewModel uvm || uvm.Status != Models.MessageStatus.Error)];
    }

    private void DeleteMessage(MessageViewModel msg)
    {
        Messages.Remove(msg);
    }

    private async Task SendMessage(string text)
    {
        var msg = new UserMessageViewModel()
        {
            Content = new()
            {
                Text = text,
                Links = [],
                Images = [],
            },
        };

        Input = string.Empty;

        await SendMessage(msg);
    }

    private async Task SendMessage(UserMessageViewModel msg)
    {
        msg.Dialog = this;
        msg.Status = Models.MessageStatus.Sent;
        msg.Metadata.Sent = DateTimeOffset.Now;
        msg.Metadata.Sender = Settings.User;
        msg.Reactions = null;

        Messages.Add(msg);

        var response = await DialogService.Send(msg);

        if (response != null)
        {
            var newVM = new UserMessageViewModel(response)
            {
                Dialog = this,
                Status = Models.MessageStatus.Delivered,
            };
            Messages.Add(newVM);
        }
    }

    private Task SaveMessage(UserMessageViewModel msg)
    {
        if (!Bookmarks.Saved.Contains(msg))
        {
            Bookmarks.Saved.Add(msg);
        }

        msg.Saved = true;

        return Task.CompletedTask;
    }
    private Task UnsaveMessage(UserMessageViewModel msg)
    {
        Bookmarks.Saved.Remove(msg);

        msg.Saved = false;

        return Task.CompletedTask;
    }

    private async Task ResendMessage(UserMessageViewModel msg)
    {
        DeleteMessage(msg);
        await SendMessage(msg);
    }
}

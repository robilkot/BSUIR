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


    private UserViewModel _helper_sender = new()
    {
        Name = "Кинопомощник",
        About = "Помогает искать информацию о фильмах"
    };

    [IgnoreDataMember]
    public ReactiveCommand<string, Unit> SendMessageCommand { get; }

    private ObservableCollection<MessageViewModel> _messages = [];
    [DataMember]
    public ObservableCollection<MessageViewModel> Messages
    {
        get => _messages;
        set => this.RaiseAndSetIfChanged(ref _messages, value);
    }

    public DialogViewModel()
    {
        SendMessageCommand = ReactiveCommand.CreateFromTask<string>(SendMessage);
    }

    public void Init()
    {
        if(Messages.Count == 0)
        {
            Messages = [
            new ServiceMessageViewModel(),
            new UserMessageViewModel()
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
            ResendCommandInternal = ReactiveCommand.CreateFromTask<UserMessageViewModel>(ResendMessage)
        };

        await SendMessage(msg);
    }

    private async Task SendMessage(UserMessageViewModel msg)
    {
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
                Status = Models.MessageStatus.Delivered
            };
            Messages.Add(newVM);
        }
    }

    private async Task ResendMessage(UserMessageViewModel msg)
    {
        DeleteMessage(msg);
        await SendMessage(msg);
    }
}

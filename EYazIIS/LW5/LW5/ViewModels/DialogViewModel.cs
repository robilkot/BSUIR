using LW5.Services;
using LW5.ViewModels.Messages;
using ReactiveUI;
using System;
using System.Collections.ObjectModel;
using System.Reactive;
using System.Threading.Tasks;

namespace LW5.ViewModels;

public class DialogViewModel : ViewModelBase
{
    private readonly DialogService _dialogService = new();

    private UserViewModel _user = new();
    public UserViewModel User
    {
        get => _user;
        set => this.RaiseAndSetIfChanged(ref _user, value);
    }

    private UserViewModel _helper_sender = new()
    {
        Name = "Кинопомощник",
        About = "Помогает искать информацию о фильмах"
    };
    private UserViewModel _user_sender = new()
    {
        Name = "User",
        About = "Пользователь приложения"
    };

    public ReactiveCommand<string, Unit> SendMessageCommand { get; }

    public ObservableCollection<MessageViewModel> Messages { get; set; }

    public DialogViewModel()
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

        SendMessageCommand = ReactiveCommand.CreateFromTask<string>(SendMessage);
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
        msg.Metadata.Sender = _user_sender;
        msg.Reactions = null;

        Messages.Add(msg);

        var response = await _dialogService.Send(msg);

        if (response != null)
        {
            var newVM = new UserMessageViewModel(response);
            Messages.Add(newVM);
        }
    }

    private async Task ResendMessage(UserMessageViewModel msg)
    {
        DeleteMessage(msg);
        await SendMessage(msg);
    }
}

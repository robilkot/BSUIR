using LW5.ViewModels.Messages;
using ReactiveUI;
using System;
using System.Collections.ObjectModel;

namespace LW5.ViewModels;

public class DialogViewModel : ViewModelBase
{
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

    public ObservableCollection<MessageViewModel> Messages => [
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
            Reactions = new() { },
        },
        new UserMessageViewModel() {
            Content = new()
            {
                Text = "Какой же ты классный. Надеюсь, у нас получится хороший диалог.",
                Links = [],
                Images = [],
            },
            Metadata = new()
            {
                Sender = _user_sender,
                Sent = DateTimeOffset.Now
            },
            Reactions = null,
        },
        new UserMessageViewModel() {
            Content = new()
            {
                Text = "Я тоже на это надеюсь.",
                Links = [],
                Images = [],
            },
            Metadata = new()
            {
                Sender = _helper_sender,
                Sent = DateTimeOffset.Now
            },
            Reactions = new() { },
        }
        ];
}

using LW5.ViewModels.Messages;
using System;
using System.Collections.ObjectModel;

namespace LW5.ViewModels
{
    public class BookmarksViewModel : ViewModelBase
    {
        private MessageSenderViewModel _helper_sender = new()
        {
            Name = "Кинопомощник",
        };

        public ObservableCollection<UserMessageViewModel> Saved => [
                new ()
                {
                    Content = new()
                    {
                        Text = "Очень важное сохраненное сообщение со ссылками и фотографиями.",
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
                new () {
                    Content = new()
                    {
                        Text = "Ещё одно сообщение, но уже без вложений.",
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
}

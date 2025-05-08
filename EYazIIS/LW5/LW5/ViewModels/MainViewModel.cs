using LW5.ViewModels.Messages;
using ReactiveUI;
using System.Collections.ObjectModel;

namespace LW5.ViewModels;

public class MainViewModel : ViewModelBase
{
    private UserViewModel _user = new();
    public UserViewModel User
    {
        get => _user;
        set => this.RaiseAndSetIfChanged(ref _user, value);
    }

    public ObservableCollection<MessageViewModel> Messages => [
        new ServiceMessageViewModel(),
        new UserMessageViewModel(),
        new UserMessageViewModel() {
            Metadata = new() {
                Sender = new() {
                    Name = "User"
                }
            },
            Reactions = null,
        },
        new UserMessageViewModel()
        ];
}

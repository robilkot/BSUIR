using LW5.ViewModels.Messages;
using System.Collections.ObjectModel;

namespace LW5.ViewModels;

public class MainViewModel : ViewModelBase
{
    public ObservableCollection<MessageViewModel> Messages => [
        new UserMessageViewModel(),
        new ServiceMessageViewModel(),
        new UserMessageViewModel(),
        new UserMessageViewModel()
        ];
}

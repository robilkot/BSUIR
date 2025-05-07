using ReactiveUI;

namespace LW5.ViewModels.Messages;

public class MessageSenderViewModel : MessageViewModel
{
    private string _name;
    public string Name
    {
        get => _name;
        set => this.RaiseAndSetIfChanged(ref _name, value);
    }
}

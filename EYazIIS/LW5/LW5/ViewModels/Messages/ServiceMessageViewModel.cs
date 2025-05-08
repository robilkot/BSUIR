using ReactiveUI;

namespace LW5.ViewModels.Messages;

public class ServiceMessageViewModel : MessageViewModel
{
    private MessageContentViewModel _content = new()
    {
        Text = "Начало диалога"
    };

    public MessageContentViewModel Content
    {
        get => _content;
        set => this.RaiseAndSetIfChanged(ref _content, value);
    }
}

using ReactiveUI;
using System.Runtime.Serialization;

namespace LW5.ViewModels.Messages;

[DataContract]
public class ServiceMessageViewModel : MessageViewModel
{
    private MessageContentViewModel _content = new()
    {
        Text = "Начало диалога"
    };
    [DataMember]
    public MessageContentViewModel Content
    {
        get => _content;
        set => this.RaiseAndSetIfChanged(ref _content, value);
    }
}

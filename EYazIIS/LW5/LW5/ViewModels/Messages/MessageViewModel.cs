using ReactiveUI;
using System.Runtime.Serialization;

namespace LW5.ViewModels.Messages;

[DataContract]
public abstract class MessageViewModel : ViewModelBase
{
    private DialogViewModel? _dialog;
    [DataMember]
    public DialogViewModel? Dialog
    {
        get => _dialog;
        set => this.RaiseAndSetIfChanged(ref _dialog, value);
    }
}

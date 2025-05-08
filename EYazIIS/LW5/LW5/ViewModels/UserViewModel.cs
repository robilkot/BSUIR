using ReactiveUI;

namespace LW5.ViewModels
{
    public class UserViewModel : ViewModelBase
    {
        private string _name = "User";
        public string Name
        {
            get => _name;
            set => this.RaiseAndSetIfChanged(ref _name, value);
        }
    }
}

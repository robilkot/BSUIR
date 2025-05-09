using ReactiveUI;

namespace LW5.ViewModels
{
    public class SettingsViewModel : ViewModelBase
    {
        private UserViewModel _user = new();
        public UserViewModel User
        {
            get => _user;
            set => this.RaiseAndSetIfChanged(ref _user, value);
        }

        private string _serverIp = "http://127.0.0.1:8000";
        public string ServerIp
        {
            get => _serverIp;
            set => this.RaiseAndSetIfChanged(ref _serverIp, value);
        }
    }
}

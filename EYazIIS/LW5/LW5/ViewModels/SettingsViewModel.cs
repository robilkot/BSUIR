using LW5.Services;
using ReactiveUI;
using System.Reactive;
using System.Reactive.Concurrency;
using System.Reactive.Linq;
using System.Runtime.Serialization;

namespace LW5.ViewModels
{
    [DataContract]
    public class SettingsViewModel : ViewModelBase
    {
        private DialogService? _dialogService;
        [IgnoreDataMember]
        public DialogService? DialogService
        {
            get => _dialogService;
            set
            {
                _dialogService = value;
                if (_dialogService != null)
                {
                    _dialogService.BaseUrl = ServerIp;
                }
            }
        }

        private UserViewModel _user = new();
        [DataMember]
        public UserViewModel User
        {
            get => _user;
            set => this.RaiseAndSetIfChanged(ref _user, value);
        }

        private string _serverIp = "http://127.0.0.1:8000";
        [DataMember]
        public string ServerIp
        {
            get => _serverIp;
            set => this.RaiseAndSetIfChanged(ref _serverIp, value);
        }
        private ReactiveCommand<string, Unit> UpdateIpCommand { get; }
        private ReactiveCommand<DialogService, Unit> InitServiceCommand { get; }

        public SettingsViewModel()
        {
            UpdateIpCommand = ReactiveCommand.Create<string>(ip =>
            {
                if (DialogService != null)
                {
                    DialogService.BaseUrl = ip;
                }
            });

            this.WhenAnyValue(x => x.ServerIp)
                .Skip(1)
                .ObserveOn(Scheduler.Default)
                .InvokeCommand(UpdateIpCommand);
        }

        private void InitService(DialogService service)
        {
            service.BaseUrl = ServerIp;
        }
    }
}

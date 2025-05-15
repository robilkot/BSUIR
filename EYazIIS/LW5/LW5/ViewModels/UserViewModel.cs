using Newtonsoft.Json;
using ReactiveUI;

namespace LW5.ViewModels
{
    public class UserViewModel : ViewModelBase
    {
        private string _name = "Тимур";
        [JsonProperty]
        public string Name
        {
            get => _name;
            set => this.RaiseAndSetIfChanged(ref _name, value);
        }

        private string _about = "Люблю Sci-Fi";
        [JsonProperty]
        public string About
        {
            get => _about;
            set => this.RaiseAndSetIfChanged(ref _about, value);
        }
    }
}

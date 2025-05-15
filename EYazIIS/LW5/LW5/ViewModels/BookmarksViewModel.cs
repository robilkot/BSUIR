using LW5.ViewModels.Messages;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;

namespace LW5.ViewModels
{
    [DataContract]
    public class BookmarksViewModel : ViewModelBase
    {
        [DataMember]
        public ObservableCollection<UserMessageViewModel> Saved { get; set; } = [];
    }
}

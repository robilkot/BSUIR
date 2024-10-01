using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using SkiaSharp;

namespace LW4
{
    public partial class MainPageViewmodel : ObservableObject
    {
        [ObservableProperty]
        private bool _showClusters;

        [ObservableProperty]
        private int _clusterCount = 5;

        [ObservableProperty]
        private int _iterations = 100;
    }
}

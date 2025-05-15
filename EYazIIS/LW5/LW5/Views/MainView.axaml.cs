using Avalonia.ReactiveUI;
using LW5.ViewModels;
using ReactiveUI;

namespace LW5.Views;

public partial class MainView : ReactiveUserControl<MainViewModel>
{
    public MainView()
    {
        InitializeComponent();
    }
}

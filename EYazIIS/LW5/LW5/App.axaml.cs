using Avalonia;
using Avalonia.Controls.ApplicationLifetimes;
using Avalonia.Markup.Xaml;
using Avalonia.ReactiveUI;
using LW5.Services;
using LW5.ViewModels;
using LW5.Views;
using ReactiveUI;

namespace LW5;

public partial class App : Application
{
    public override void Initialize()
    {
        AvaloniaXamlLoader.Load(this);
    }

    public override void OnFrameworkInitializationCompleted()
    {
        if (ApplicationLifetime is IClassicDesktopStyleApplicationLifetime desktop)
        {
            // Create the AutoSuspendHelper.
            var suspension = new AutoSuspendHelper(ApplicationLifetime);
            RxApp.SuspensionHost.CreateNewAppState = () => new MainViewModel();
            RxApp.SuspensionHost.SetupDefaultSuspendResume(new NewtonsoftJsonSuspensionDriver("appstate.json"));
            suspension.OnFrameworkInitializationCompleted();

            var state = RxApp.SuspensionHost.GetAppState<MainViewModel>();

            desktop.MainWindow = new MainWindow
            {
                DataContext = state
            };

            state.Init();
        }
        else if (ApplicationLifetime is ISingleViewApplicationLifetime singleViewPlatform)
        {
            var state = new MainViewModel();

            singleViewPlatform.MainView = new MainView
            {
                DataContext = state
            };

            state.Init();
        }


        base.OnFrameworkInitializationCompleted();
    }
}

using Android.App;
using Android.Views;
using Android.Content.PM;

using Avalonia;
using Avalonia.Android;
using Avalonia.ReactiveUI;
using System;

namespace LW5.Android;

[Activity(
    Label = "LW5.Android",
    Theme = "@style/MyTheme.NoActionBar",
    Icon = "@drawable/icon",
    WindowSoftInputMode = SoftInput.AdjustResize,
    MainLauncher = true,
    ScreenOrientation = ScreenOrientation.SensorPortrait,
    ConfigurationChanges = ConfigChanges.Orientation | ConfigChanges.ScreenSize | ConfigChanges.UiMode)]
public class MainActivity : AvaloniaMainActivity<App>
{
    protected override AppBuilder CustomizeAppBuilder(AppBuilder builder)
    {
        AppContext.SetSwitch("System.Reflection.NullabilityInfoContext.IsSupported", true);

        return base.CustomizeAppBuilder(builder)
            .WithInterFont()
            .UseReactiveUI();
    }
}
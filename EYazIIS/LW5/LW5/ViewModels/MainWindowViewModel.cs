using Avalonia.Controls;
using LW5.Models;
using LW5.Views;
using ReactiveUI;
using System;
using System.Collections.Generic;
using System.Reactive;

namespace LW5.ViewModels;

public class MainWindowViewModel : ViewModelBase
{
    private UserControl _currentPage;
    public UserControl CurrentPage
    {
        get => _currentPage;
        set => this.RaiseAndSetIfChanged(ref _currentPage, value);
    }

    private Dictionary<AppPage, UserControl> _pages = [];

    private Dictionary<AppPage, Type> _pageTypes = new()
    {
        { AppPage.Main, typeof(MainView) },
        { AppPage.Settings, typeof(SettingsView) },
        { AppPage.Bookmarks, typeof(BookmarksView) },
    };

    private Dictionary<Type, Type> _viewModels = new()
    {
        { typeof(MainView), typeof(MainViewModel) },
        { typeof(SettingsView), typeof(SettingsViewModel) },
        { typeof(BookmarksView), typeof(BookmarksViewModel) },
    };

    public ReactiveCommand<AppPage, Unit> NavigateCommand { get; }

    public MainWindowViewModel()
    {
        NavigateCommand = ReactiveCommand.Create<AppPage>(Navigate);

        Navigate(AppPage.Main);
    }

    private void Navigate(AppPage page)
    {
        if (!_pages.TryGetValue(page, out UserControl? control))
        {
            var inst = Activator.CreateInstance(_pageTypes[page])!;
            control = (UserControl)inst;
            _pages.Add(page, control);
        }

        var vmType = _viewModels[control.GetType()];
        var vm = Activator.CreateInstance(vmType);

        CurrentPage = control;
        CurrentPage.DataContext = vm;
    }
}

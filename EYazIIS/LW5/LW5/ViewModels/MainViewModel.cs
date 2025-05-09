using Avalonia.Controls;
using LW5.Models;
using LW5.Views;
using ReactiveUI;
using System;
using System.Collections.Generic;
using System.Reactive;

namespace LW5.ViewModels;

public class MainViewModel : ViewModelBase
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
        { AppPage.Dialog, typeof(DialogView) },
        { AppPage.Settings, typeof(SettingsView) },
        { AppPage.Bookmarks, typeof(BookmarksView) },
    };

    private Dictionary<Type, ViewModelBase> _viewModels = new()
    {
        { typeof(DialogView), new DialogViewModel() },
        { typeof(SettingsView), new SettingsViewModel() },
        { typeof(BookmarksView), new BookmarksViewModel() },
    };

    public ReactiveCommand<AppPage, Unit> NavigateCommand { get; }

    public MainViewModel()
    {
        NavigateCommand = ReactiveCommand.Create<AppPage>(Navigate);

        Navigate(AppPage.Dialog);
    }

    private void Navigate(AppPage page)
    {
        if (!_pages.TryGetValue(page, out UserControl? control))
        {
            var inst = Activator.CreateInstance(_pageTypes[page])!;
            control = (UserControl)inst;
            _pages.Add(page, control);
        }

        var vm = _viewModels[control.GetType()];

        control.DataContext = vm;
        CurrentPage = control;
    }
}

using Avalonia.Controls;
using LW5.Models;
using LW5.Services;
using LW5.Views;
using ReactiveUI;
using System;
using System.Collections.Generic;
using System.Reactive;
using System.Runtime.Serialization;

namespace LW5.ViewModels;

[DataContract]
public class MainViewModel : ViewModelBase
{
    private UserControl _currentPage;
    [IgnoreDataMember]
    public UserControl CurrentPage
    {
        get => _currentPage;
        set => this.RaiseAndSetIfChanged(ref _currentPage, value);
    }

    private SettingsViewModel _settings = new();
    [DataMember]
    public SettingsViewModel Settings
    {
        get => _settings;
        set => this.RaiseAndSetIfChanged(ref _settings, value);
    }

    private DialogViewModel _dialog = new();
    [DataMember]
    public DialogViewModel Dialog
    {
        get => _dialog;
        set => this.RaiseAndSetIfChanged(ref _dialog, value);
    }

    private BookmarksViewModel _bookmarks = new();
    [DataMember]
    public BookmarksViewModel Bookmarks
    {
        get => _bookmarks;
        set => this.RaiseAndSetIfChanged(ref _bookmarks, value);
    }

    private Dictionary<AppPage, UserControl> _pages = [];

    private Dictionary<AppPage, Type> _pageTypes = new()
    {
        { AppPage.Dialog, typeof(DialogView) },
        { AppPage.Settings, typeof(SettingsView) },
        { AppPage.Bookmarks, typeof(BookmarksView) },
    };


    [IgnoreDataMember]
    public ReactiveCommand<AppPage, Unit> NavigateCommand { get; }

    public MainViewModel()
    {
        NavigateCommand = ReactiveCommand.Create<AppPage>(Navigate);

        Navigate(AppPage.Dialog);
    }

    public void Init()
    {
        var dialogService = new DialogService();

        Settings.DialogService = dialogService;
        Dialog.DialogService = dialogService;
        Dialog.Settings = Settings;

        Dialog.Init();
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

        object? vm = control switch
        {
            DialogView => Dialog,
            BookmarksView => Bookmarks,
            SettingsView => Settings,
            _ => null
        };

        control.DataContext = vm;
        CurrentPage = control;
    }
}

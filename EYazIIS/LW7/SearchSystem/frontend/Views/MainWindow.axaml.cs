using Avalonia.Controls;
using Avalonia.Input;
using CommonLib.Models;
using frontend.ViewModels;
using ReactiveUI;
using ShadUI;
using System;
using System.Diagnostics;

namespace frontend.Views;

public partial class MainWindow : ShadUI.Window
{
    public MainWindow()
    {
        InitializeComponent();
    }

    private void OnSearchKeyDown(object sender, KeyEventArgs e)
    {
        if (e.Key == Key.Enter)
        {
            if (DataContext is ViewModels.MainViewModel viewModel)
            {
                viewModel.SearchCommand.Execute();
            }
            e.Handled = true;
        }
    }

    private void TextBlock_PointerPressed(object? sender, Avalonia.Input.PointerPressedEventArgs e)
    {
        TextBlock tb = (TextBlock)sender!;
        var result = (SearchResult)tb.DataContext!;

        var uri = result.Uri;
        string unescapedUri = uri.ToString();
        Process.Start(new ProcessStartInfo(unescapedUri) { UseShellExecute = true });
    }

    private void ScrollViewer_ScrollChanged(object? sender, Avalonia.Controls.ScrollChangedEventArgs e)
    {
        ScrollViewer scrollViewer = (ScrollViewer)sender!;

        if(Math.Abs(scrollViewer.Offset.Y - scrollViewer.ScrollBarMaximum.Y) <= 0.1)
        {
            MainViewModel vm = (MainViewModel)DataContext!;

            vm.NextPageCommand.Execute();
        }
    }
}

using Avalonia.Controls;
using Avalonia.Input;

namespace frontend.Views;

public partial class MainWindow : Window
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
                viewModel.SearchCommand.Execute(null);
            }
            e.Handled = true;
        }
    }
}

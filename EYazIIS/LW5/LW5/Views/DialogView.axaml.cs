using Avalonia.Controls;
using LW5.ViewModels;

namespace LW5.Views;

public partial class DialogView : UserControl
{
    public DialogView()
    {
        InitializeComponent();

        AttachedToVisualTree += DialogView_AttachedToVisualTree;
        DetachedFromVisualTree += DialogView_DetachedFromVisualTree; ;
    }

    private void DialogView_DetachedFromVisualTree(object? sender, Avalonia.VisualTreeAttachmentEventArgs e)
    {
        if (DataContext is DialogViewModel vm)
        {
            vm.Messages.CollectionChanged -= Messages_CollectionChanged;
        }
    }

    private void DialogView_AttachedToVisualTree(object? sender, Avalonia.VisualTreeAttachmentEventArgs e)
    {
        if (DataContext is DialogViewModel vm)
        {
            vm.Messages.CollectionChanged += Messages_CollectionChanged;
        }
    }

    private void Messages_CollectionChanged(object? sender, System.Collections.Specialized.NotifyCollectionChangedEventArgs e)
    {
        if (e.Action == System.Collections.Specialized.NotifyCollectionChangedAction.Add)
        {
            scroller.ScrollToEnd();
        }
    }
}
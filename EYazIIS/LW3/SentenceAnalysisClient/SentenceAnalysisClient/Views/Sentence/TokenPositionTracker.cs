using Avalonia;
using Avalonia.Controls;
using SentenceAnalysisClient.ViewModels;
using System;

namespace SentenceAnalysisClient.Views.Sentence
{
    public static class TokenPositionTracker
    {
        //public static readonly AttachedProperty<SyntaxViewModel> TrackPositionProperty =
        //    AvaloniaProperty.RegisterAttached<Control, SyntaxViewModel>("TrackPosition", typeof(TokenPositionTracker));

        //static TokenPositionTracker()
        //{
        //    TrackPositionProperty.Changed.Subscribe(args =>
        //    {
        //        if (args.Sender is Control control && args.NewValue is SyntaxViewModel vm)
        //        {
        //            control.AttachedToVisualTree += (_, _) =>
        //            {
        //                control.Dispatcher.UIThread.Post(() =>
        //                {
        //                    var point = control.TranslatePoint(new Point(0, 0), null);
        //                    if (point.HasValue)
        //                        vm.TokenVisualPosition = point.Value;
        //                }, Avalonia.Threading.DispatcherPriority.Render);
        //            };
        //        }
        //    });
        //}

        //public static void SetTrackPosition(Control control, SyntaxViewModel value) =>
        //    control.SetValue(TrackPositionProperty, value);

        //public static SyntaxViewModel GetTrackPosition(Control control) =>
        //    control.GetValue(TrackPositionProperty);
    }

}

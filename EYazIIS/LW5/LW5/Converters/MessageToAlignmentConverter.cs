using Avalonia.Data.Converters;
using Avalonia.Layout;
using LW5.ViewModels.Messages;
using System;
using System.Collections.Generic;
using System.Globalization;

namespace LW5.Converters
{
    public class MessageToAlignmentConverter : IMultiValueConverter
    {
        public object? Convert(IList<object?> values, Type targetType, object? parameter, CultureInfo culture)
        {
            HorizontalAlignment alignment = values[0] switch
            {
                UserMessageViewModel uvm when values[1] is string username && uvm.Metadata.Sender.Name == username => HorizontalAlignment.Right,
                UserMessageViewModel => HorizontalAlignment.Left,
                ServiceMessageViewModel => HorizontalAlignment.Center,
                _ => HorizontalAlignment.Stretch,
            };

            return alignment;
        }

        public object? ConvertBack(object? value, Type targetType, object? parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}

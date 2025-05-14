using Avalonia.Data.Converters;
using Avalonia.Media.Immutable;
using LW5.Models;
using System;
using System.Globalization;

namespace LW5.Converters
{
    public class MessageStatusToColorConverter : IValueConverter
    {
        public ImmutableSolidColorBrush? OkColor { get; set; }
        public ImmutableSolidColorBrush? ErrorColor { get; set; }
        public object? Convert(object? value, Type targetType, object? parameter, CultureInfo culture)
        {
            if (value is MessageStatus status)
            {
                return status switch
                {
                    MessageStatus.Error => ErrorColor,
                    _ => OkColor
                };
            }

            return null;
        }

        public object? ConvertBack(object? value, Type targetType, object? parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}

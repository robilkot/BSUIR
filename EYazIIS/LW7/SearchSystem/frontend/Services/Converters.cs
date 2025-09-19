using Avalonia.Data.Converters;
using System;
using System.Globalization;

namespace frontend.Services
{
    public class IsNotNullOrEmptyConverter : IValueConverter
    {
        public object? Convert(object? value, Type targetType, object? parameter, CultureInfo culture)
        {
            if(value is null)
            {
                return false;
            }

            if(value is string str)
            {
                return !(string.IsNullOrEmpty(str) || string.IsNullOrWhiteSpace(str));
            }

            return true;
        }

        public object? ConvertBack(object? value, Type targetType, object? parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}

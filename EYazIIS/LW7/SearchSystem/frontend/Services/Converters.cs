using Avalonia.Data.Converters;
using System;
using System.Collections;
using System.Globalization;

namespace frontend.Services
{
    public class IsNotNullAndIsEmptyConverter : IValueConverter
    {
        public object? Convert(object? value, Type targetType, object? parameter, CultureInfo culture)
        {
            if (value == null) 
                return false;

            if (value is ICollection collection)
            {
                return collection.Count == 0;
            }

            return false;
        }

        public object? ConvertBack(object? value, Type targetType, object? parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }

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

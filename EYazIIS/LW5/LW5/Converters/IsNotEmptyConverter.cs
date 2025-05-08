using Avalonia.Data.Converters;
using System;
using System.Collections;
using System.Globalization;

namespace LW5.Converters
{
    public class IsNotEmptyConverter : IValueConverter
    {
        public object? Convert(object? value, Type targetType, object? parameter, CultureInfo culture)
        {
            if (value is IList list)
            {
                return list.Count != 0;
            }

            return true;
        }

        public object? ConvertBack(object? value, Type targetType, object? parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}

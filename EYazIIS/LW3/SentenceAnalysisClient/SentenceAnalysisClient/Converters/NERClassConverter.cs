using Avalonia.Data.Converters;
using SentenceAnalysisClient.Model;
using System;
using System.Collections.Generic;
using System.Globalization;

namespace SentenceAnalysisClient.Converters
{
    public class NERClassConverter : IValueConverter
    {
        private static readonly Dictionary<NERClass, string> translations = new()
        {
            { NERClass.LOC, "Локация" },
            { NERClass.ORG, "Организация" },
            { NERClass.PER, "Личность" },
        };

        public object Convert(object? value, Type targetType, object? parameter, CultureInfo culture)
        {
            if (value is NERClass pos)
                return translations[pos];

            return "Ошибка определения класса сущности";
        }

        public object ConvertBack(object? value, Type targetType, object? parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}

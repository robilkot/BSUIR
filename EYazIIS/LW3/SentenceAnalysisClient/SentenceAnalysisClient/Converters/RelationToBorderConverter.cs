using Avalonia;
using Avalonia.Data.Converters;
using SentenceAnalysisClient.Model;
using System;
using System.Globalization;

namespace SentenceAnalysisClient.Converters
{
    public class RelationToBorderConverter : IValueConverter
    {
        public object Convert(object? value, Type targetType, object? parameter, CultureInfo culture)
        {
            if (value is GrammaticalRelation relation)
            {
                return relation switch
                {
                    GrammaticalRelation.Nsubj => new Thickness(0, 0, 0, 1), // одиночная линия
                    GrammaticalRelation.Root => new Thickness(0, 0, 0, 2), // двойная
                    GrammaticalRelation.Obj => new Thickness(0, 0, 0, 1), // другая роль
                    _ => new Thickness(0)
                };
            }

            return new Thickness(0);
        }

        public object ConvertBack(object? value, Type targetType, object? parameter, CultureInfo culture) =>
            throw new NotSupportedException();
    }

}

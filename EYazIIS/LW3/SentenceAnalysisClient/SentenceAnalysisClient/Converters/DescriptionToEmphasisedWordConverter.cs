﻿using Avalonia.Data.Converters;
using SentenceAnalysisClient.ViewModels.Semantics;
using System;
using System.Globalization;

namespace SentenceAnalysisClient.Converters
{
    public class DescriptionToEmphasisedWordConverter : IValueConverter
    {
        public object? Convert(object? value, Type targetType, object? parameter, CultureInfo culture)
        {
            if (value is ObjectDescriptionViewModel vm)
            {
                if (vm.Emphasis != -1)
                {
                    return vm.Text.Insert(vm.Emphasis + 1, "\'");
                }
                else
                {
                    return vm.Text;
                }
            }

            return null;
        }

        public object ConvertBack(object? value, Type targetType, object? parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}

using Avalonia.Data.Converters;
using SentenceAnalysisClient.Model;
using System;
using System.Collections.Generic;
using System.Globalization;

namespace SentenceAnalysisClient.Converters
{
    public class SyntaxRoleConverter : IValueConverter
    {
        private static readonly Dictionary<SyntaxRole, string> translations = new()
        {
            { SyntaxRole.Root, "Сказуемое" },
            { SyntaxRole.Nsubj, "Подлежащее" },
            { SyntaxRole.Obj, "Дополнение" },
            { SyntaxRole.Iobj, "Косвенное дополнение" },
            { SyntaxRole.Ccomp, "Сказуемое придаточного дополнительного предложения" },
            { SyntaxRole.Xcomp, "Дополнительный предикатив" },
            { SyntaxRole.Advmod, "Обстоятельство" },
            { SyntaxRole.Amod, "Определение" },
            { SyntaxRole.Det, "Определитель" },
            { SyntaxRole.Cc, "Сочинительный союз" },
            { SyntaxRole.Case, "Предлог" },
            { SyntaxRole.Obl, "Обстоятельственное дополнение" },
            { SyntaxRole.Appos, "Приложение" },
            { SyntaxRole.Conj, "Сказуемое сочиненного предложения" },
            { SyntaxRole.Nummod, "Грамматическое числительное" },
            { SyntaxRole.Punct, "Знак препинания" },
            { SyntaxRole.Parataxis, "Парцелляция" },
            { SyntaxRole.Acl, "Сказуемое определительного придаточного предложения" },
            { SyntaxRole.Nmod, "Именное дополнение" }
        };

        public object Convert(object? value, Type targetType, object? parameter, CultureInfo culture)
        {
            if (value is SyntaxRole role)
                return translations[role];

            return "Ошибка определения синтаксической роли";
        }

        public object ConvertBack(object? value, Type targetType, object? parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}

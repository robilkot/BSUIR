using Avalonia.Data.Converters;
using SentenceAnalysisClient.Model;
using System;
using System.Collections.Generic;
using System.Globalization;

namespace SentenceAnalysisClient.Converters
{
    public class GrammaticalRelationConverter : IValueConverter
    {
        private static readonly Dictionary<GrammaticalRelation, string> translations = new()
        {
            { GrammaticalRelation.Root, "Корень" },
            { GrammaticalRelation.Nsubj, "Подлежащее" },
            { GrammaticalRelation.Obj, "Дополнение" },
            { GrammaticalRelation.Iobj, "Косвенное дополнение" },
            { GrammaticalRelation.Ccomp, "Придаточное дополнительное" },
            { GrammaticalRelation.Xcomp, "Дополнительный предикатив" },
            { GrammaticalRelation.Advmod, "Обстоятельство" },
            { GrammaticalRelation.Amod, "Определение" },
            { GrammaticalRelation.Det, "Определитель" },
            { GrammaticalRelation.Cc, "Сочинительный союз" },
            { GrammaticalRelation.Case, "Предлог" },
            { GrammaticalRelation.Obl, "Обстоятельственное дополнение" },
            { GrammaticalRelation.Appos, "Приложение" },
            { GrammaticalRelation.Conj, "Сочиненное предложение" },
            { GrammaticalRelation.Nummod, "Грамматическое числительное" },
            { GrammaticalRelation.Punct, "Знак препинания" },
            { GrammaticalRelation.Parataxis, "Парцелляция" },
            { GrammaticalRelation.Acl, "Определительное придаточное" },
            { GrammaticalRelation.Nmod, "Именное дополнение" }
        };

        public object Convert(object? value, Type targetType, object? parameter, CultureInfo culture)
        {
            if (value is GrammaticalRelation pos)
                return translations[pos];

            return "Ошибка определения синтаксической роли";
        }

        public object ConvertBack(object? value, Type targetType, object? parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}

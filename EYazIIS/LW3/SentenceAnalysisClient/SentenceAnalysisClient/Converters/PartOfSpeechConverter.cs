using Avalonia.Data.Converters;
using SentenceAnalysisClient.Model;
using System;
using System.Collections.Generic;
using System.Globalization;

namespace SentenceAnalysisClient.Converters
{
    public class PartOfSpeechConverter : IValueConverter
    {
        private static readonly Dictionary<PartOfSpeech, string> translations = new()
        {
            { PartOfSpeech.noun, "Существительное" },
            { PartOfSpeech.verb, "Глагол" },
            { PartOfSpeech.adj, "Прилагательное" },
            { PartOfSpeech.adv, "Наречие" },
            { PartOfSpeech.pron, "Местоимение" },
            { PartOfSpeech.num, "Числительное" },
            { PartOfSpeech.adp, "Предлог" },
            { PartOfSpeech.conj, "Союз" },
            { PartOfSpeech.part, "Частица" },
            { PartOfSpeech.intj, "Междометие" },
            { PartOfSpeech.det, "Артикль или указательное слово" },
            { PartOfSpeech.punct, "Знак препинания" },
            { PartOfSpeech.sym, "Символ" },
            { PartOfSpeech.propn, "Имя собственное" },
            { PartOfSpeech.x, "Неопределенная часть речи" },
            { PartOfSpeech.aux, "Вспомогательный глагол" }
        };

        public object Convert(object? value, Type targetType, object? parameter, CultureInfo culture)
        {
            if (value is PartOfSpeech pos)
                return translations[pos];

            return "Ошибка определения части речи";
        }

        public object ConvertBack(object? value, Type targetType, object? parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}

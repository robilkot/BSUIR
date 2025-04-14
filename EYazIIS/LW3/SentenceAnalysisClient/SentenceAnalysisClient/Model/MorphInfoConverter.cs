using Avalonia.Data.Converters;
using System;
using System.Collections.Generic;
using System.Globalization;

namespace SentenceAnalysisClient.Model
{
    public class MorphInfoConverter : IValueConverter
    {
        private static readonly Dictionary<string, string> MORPH_KEYS_TRANSLATIONS = new()
        {
            { "pos", "Часть речи" },
            { "Aspect", "Вид" },
            { "Mood", "Наклонение" },
            { "Number", "Число" },
            { "Person", "Лицо" },
            { "Tense", "Время" },
            { "VerbForm", "Форма глагола" },
            { "Voice", "Залог" },
            { "Case", "Падеж" },
            { "Degree", "Степень" },
            { "Gender", "Род" },
            { "Animacy", "Одушевлённость" },
            { "Variant", "Форма" },
            { "Polarity", "Значение" },
            { "Foreign", "Иностранное" },
        };

        private static readonly Dictionary<string, Dictionary<string, string>> MORPH_VALUES_TRANSLATIONS = new()
        {
            {"Polarity", new()
                {
                    {"Neg", "отрицательная"}
                }
            },
            {"Variant", new()
                {
                    {"Short", "краткое"}
                }
            },
            {"Animacy", new()
                {
                    {"Inan", "неодушевлённое"},
                    {"Anim", "одушевлённое"}
                }
            },
            {"Gender", new()
                {
                    {"Fem", "женский"},
                    {"Masc", "мужской"},
                    {"Neut", "средний"}
                }
            },
            {"Aspect", new()
                {
                    {"Imp", "несовершенный"},
                    {"Perf", "совершенный"}
                }
            },
            {"Mood", new()
                {
                    {"Ind", "изъявительное"},
                    {"Sub", "сослагательное"},
                    {"Imp", "повелительное"}
                }
            },
            {"Number", new()
                {
                    {"Sing", "единственное"},
                    {"Plur", "множественное"}
                }
            },
            {"Foreign", new()
                {
                    {"Yes", "да"}
                }
            },
            {"Person", new()
                {
                    {"1", "Первое"},
                    {"2", "Второе"},
                    {"3", "Третье"}
                }
            },
            {"Tense", new()
                {
                    {"Pres", "настоящее"},
                    {"Past", "прошедшее"},
                    {"Fut", "будущее"}
                }
            },
            {"VerbForm", new()
                {
                    {"Fin", "личная форма"},
                    {"Inf", "инфинитив"},
                    {"Part", "причастие"},
                    {"Conv", "деепричастие"}
                }
            },
            {"Voice", new()
                {
                    {"Act", "Активный"},
                    {"Mid", "Средний"},
                    {"Pass", "Пассивный"}
                }
            },
            {"Case", new()
                {
                    {"Nom", "именительный"},
                    {"Gen", "родительный"},
                    {"Dat", "дательный"},
                    {"Acc", "винительный"},
                    {"Ins", "творительный"},
                    {"Loc", "предложный"}
                }
            },
            {"Degree", new()
                {
                    {"Pos", "положительная"},
                    {"Cmp", "сравнительная"},
                    {"Sup", "превосходная"}
                }
            }
        };

        public object Convert(object? value, Type targetType, object? parameter, CultureInfo culture)
        {
            if (value is Dictionary<string, string> dict)
            {
                var result = new List<string>();

                foreach (var pair in dict)
                {
                    if (MORPH_KEYS_TRANSLATIONS.TryGetValue(pair.Key, out var keyTranslation) &&
                        MORPH_VALUES_TRANSLATIONS.TryGetValue(pair.Key, out var innerDict) &&
                        innerDict.TryGetValue(pair.Value, out var valueTranslation))
                    {
                        result.Add($"{keyTranslation}: {valueTranslation}");
                    }
                }

                return string.Join(", ", result);
            }

            if(value is null)
            {
                return "отсутствуют";
            }

            return "ошибка отображения";
        }

        public object ConvertBack(object? value, Type targetType, object? parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}

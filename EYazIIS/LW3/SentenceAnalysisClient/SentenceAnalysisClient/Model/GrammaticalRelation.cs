using System.Collections.Generic;

namespace SentenceAnalysisClient.Model
{
    public enum GrammaticalRelation
    {
        Root = 1,           // Корень
        Nsubj,              // Подлежащее
        Obj,                // Дополнение
        Iobj,               // Косвенное дополнение
        Ccomp,              // Придаточное дополнительное
        Xcomp,              // Дополнительный предикатив
        Advmod,             // Обстоятельство
        Amod,               // Определение
        Det,                // Определитель
        Cc,                 // Сочинительный союз
        Case,               // Предлог
        Obl,                // Обстоятельственное дополнение
        Appos,              // Приложение
        Conj,               // Сочиненное предложение
        Nummod,             // Грамматическое числительное
        Punct,              // Знак препинания
        Parataxis,          // Парцелляция
        Acl,                // Определительное придаточное
        Nmod               // Именное дополнение
    }

    public static class GrammaticalRelationExtensions
    {
        private static readonly Dictionary<GrammaticalRelation, string> RussianNames = new()
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

        public static string GetRussianName(this GrammaticalRelation relation)
        {
            return RussianNames[relation];
        }
    }
}

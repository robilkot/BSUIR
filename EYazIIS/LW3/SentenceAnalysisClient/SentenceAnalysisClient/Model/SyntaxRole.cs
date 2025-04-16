using System.Collections.Generic;

namespace SentenceAnalysisClient.Model
{
    public enum SyntaxRole
    {
        Root = 1,           // Сказуемое
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
}

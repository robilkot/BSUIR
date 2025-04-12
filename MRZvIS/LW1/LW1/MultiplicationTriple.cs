// Лабораторная работа №1 по дисциплине МРЗвИС
// Вариант 1: алгоритм вычисления произведения пары 4-разрядных чисел умножением с младших разрядов со сдвигом множимого (частичного произведения) влево
// Выполнил студент группы 221701 БГУИР Робилко Тимур Маркович
//
// Файл, содержащий класс тройки для умножения чисел
//
// Источники:
// - Формальные модели обработки информации и параллельные модели решения задач : учеб.-метод. пособие / В. П. Ивашенко. – Минск : БГУИР, 2020


namespace LW1
{
    public class MultiplicationTriple
    {
        public int Index { get; init; }
        
        public required Number Multiplicand;
        public required Number Factor;
        public required Number PartialSum;

        public override string ToString() =>
                $"Множимое:        {Multiplicand}\n" +
                $"Множитель:       {Factor}\n" +
                $"Частичная сумма: {PartialSum}\n";
    };
}

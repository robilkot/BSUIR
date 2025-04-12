// Лабораторная работа №1 по дисциплине МРЗвИС
// Вариант 1: алгоритм вычисления произведения пары 4-разрядных чисел умножением с младших разрядов со сдвигом множимого (частичного произведения) влево
// Выполнил студент группы 221701 БГУИР Робилко Тимур Маркович
//
// Файл, содержащий класс, отвечающий за логгирование
//
// Источники:
// - Формальные модели обработки информации и параллельные модели решения задач : учеб.-метод. пособие / В. П. Ивашенко. – Минск : БГУИР, 2020


namespace LW1
{
    public static class Debug
    {
        public static bool Enabled = false;

        public static void Log(object? obj = null)
        {
            if(Enabled)
            {
                Console.WriteLine(obj?.ToString());
            }
        }
        public static void Log(params object[] args)
        {
            foreach(object arg in args)
            {
                Log(arg);
            }
        }
        public static void Clear()
        {
            if(Enabled)
            {
                Console.Clear();
            }
        }
    }
}

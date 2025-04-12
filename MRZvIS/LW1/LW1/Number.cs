// Лабораторная работа №1 по дисциплине МРЗвИС
// Вариант 1: алгоритм вычисления произведения пары 4-разрядных чисел умножением с младших разрядов со сдвигом множимого (частичного произведения) влево
// Выполнил студент группы 221701 БГУИР Робилко Тимур Маркович
//
// Файл, содержащий класс, представляющий число заданной разрядности (не более 32 бит)
//
// Источники:
// - Формальные модели обработки информации и параллельные модели решения задач : учеб.-метод. пособие / В. П. Ивашенко. – Минск : БГУИР, 2020


namespace LW1
{
    public record Number(uint Data, int BitDepth)
    {
        public static readonly int DefaultBitDepth = 4;

        public static implicit operator Number(uint data) => new(data, DefaultBitDepth);
        public static implicit operator uint(Number data) => data.Data;

        public override string ToString()
        {
            string result = "";

            for (int i = BitDepth - 1; i >= 0; i--)
            {
                result += $"{Data >> i & 1}";

                if (i > 0 && (i % 4 == 0))
                {
                    result += ' ';
                }
            }

            return result;
        }

        public static Number operator +(Number num, Number other)
            => num with { Data = num.Data + other.Data };
        public static Number operator <<(Number num, int count)
            => num with { Data = num.Data << count };
        public static Number operator >>(Number num, int count)
            => num with { Data = num.Data >> count };
    }
}

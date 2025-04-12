// Лабораторная работа №1 по дисциплине МРЗвИС
// Вариант 1: алгоритм вычисления произведения пары 4-разрядных чисел умножением с младших разрядов со сдвигом множимого (частичного произведения) влево
// Выполнил студент группы 221701 БГУИР Робилко Тимур Маркович
//
// Файл, содержащий классы для чтения пар чисел из файла или их генерации
//
// Источники:
// - Формальные модели обработки информации и параллельные модели решения задач : учеб.-метод. пособие / В. П. Ивашенко. – Минск : БГУИР, 2020


namespace LW1
{
    public interface IPairReader
    {
        public IEnumerable<(Number A, Number B)> ReadPairs(int bitDepth);
    }

    public class MockPairReader(int pairsCount) : IPairReader
    {
        public IEnumerable<(Number A, Number B)> ReadPairs(int bitDepth)
            => pairsCount <= 0
            ? []
            : Enumerable
            .Range(0, pairsCount)
            .Select(i
                => (new Number((uint)i, bitDepth), new Number((uint)i * 2, bitDepth)));
    }

    public class PairReader(string filename) : IPairReader
    {
        private static readonly char[] separator = [' '];

        public IEnumerable<(Number A, Number B)> ReadPairs(int bitDepth)
        {
            if (!File.Exists(filename))
            {
                Debug.Log($"Файл не найден: {filename}");
                return [];
            }

            string[] lines = File.ReadAllLines(filename);

            return lines.Select(line =>
            {
                string[] parts = line.Split(separator, StringSplitOptions.RemoveEmptyEntries);

                if (parts.Length != 2)
                    throw new FormatException($"Неверный формат пары в строке: {line}");

                if (!uint.TryParse(parts[0], out uint a) || !uint.TryParse(parts[1], out uint b))
                    throw new FormatException($"Неверный формат числа в строке: {line}");

                return (new Number(a, bitDepth), new Number(b, bitDepth));
            });
        }
    }
}

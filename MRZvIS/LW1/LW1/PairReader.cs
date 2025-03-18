using System.Linq;

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

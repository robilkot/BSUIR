using System.Collections;
using System.Text;

namespace LW1
{
    public static class Helper
    {
        public static void ShowDetails(BinaryInteger a)
        {

            Console.WriteLine(
                $"Dec:\t{a.ToDecimal()}\n" +
                $"Dir:\t{a.DirectCode().ToConsoleString()}\n" +
                $"Inv:\t{a.InvertCode().ToConsoleString()}\n" +
                $"Add:\t{a.AdditionalCode().ToConsoleString()}\n"
                );
        }

        public static int ReadInt()
        {
            while (true)
            {
                Console.Write("Inp:\t");
                var input = Console.ReadLine();

                if (int.TryParse(input, out var result))
                {
                    return result;
                }
            }
        }


        public static string ToConsoleString(this BitArray array)
        {
            StringBuilder result = new(array.Length);

            foreach (bool bit in array)
            {
                result.Append(bit ? '1' : '0');
            }

            return result.ToString();
        }
    }
}
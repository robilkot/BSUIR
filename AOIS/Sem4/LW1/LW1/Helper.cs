using System.Collections;
using System.Diagnostics.CodeAnalysis;
using System.Text;

namespace LW1
{
    [ExcludeFromCodeCoverage]
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
        public static void ShowDetails(BinaryFloat a)
        {
            Console.WriteLine(
                $"Flt:\t{a.ToFloat()}\n" +
                $"Dir:\t{a.ToBitArray().ToConsoleString()}\n"
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

        public static float ReadFloat()
        {
            while (true)
            {
                Console.Write("Inp:\t");
                var input = Console.ReadLine();

                if (float.TryParse(input, out var result))
                {
                    return result;
                }
            }
        }


        public static string ToConsoleString(this BitArray array)
        {
            StringBuilder result = new(array.Length);

            for(int k = 0; k < array.Length / 8; k++)
            {
            for (int i = 0; i <= 7; i++)
            {
                result.Append(array[i + k * 8] ? '1' : '0');
            }
            }

            return result.ToString();
        }
    }
}
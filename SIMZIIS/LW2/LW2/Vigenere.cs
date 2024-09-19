using System.Text;

namespace LW2
{
    public class Vigenere(char alphabetStart, char alphabetEnd)
    {
        public readonly char alphabetStart = alphabetStart;
        public readonly char alphabetEnd = alphabetEnd;
        private int AlphabetLength => alphabetEnd - alphabetStart + 1;

        public string Encrypt(string text, string key)
        {
            StringBuilder sb = new(text.Length);

            for (int i = 0; i < text.Length; i++)
            {
                int indexInKey = i % key.Length;

                var newSymbol = (char)(alphabetStart + Mod(text[i] + key[indexInKey] - 2 * alphabetStart, AlphabetLength));

                sb.Append(newSymbol);
            }

            return sb.ToString();
        }
        public string Decrypt(string text, string key)
        {
            StringBuilder sb = new(text.Length);

            for (int i = 0; i < text.Length; i++)
            {
                int indexInKey = i % key.Length;

                var newSymbol = (char)(alphabetStart + Mod(text[i] - key[indexInKey], AlphabetLength));

                sb.Append(newSymbol);
            }

            return sb.ToString();
        }
        private static int Mod(int x, int m)
        {
            int r = x % m;
            return r < 0 ? r + m : r;
        }
    }
}


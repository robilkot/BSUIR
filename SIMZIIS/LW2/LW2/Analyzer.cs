namespace LW2
{
    public class Analyzer(Vigenere vigenere)
    {
        public Vigenere Vigenere { get; set; } = vigenere;

        public string? BruteForceAttack(string originalText, string key)
        {
            string encryptedText = Vigenere.Encrypt(originalText, key);

            char[] alphabet = Enumerable.Range(Vigenere.alphabetStart, Vigenere.alphabetEnd - Vigenere.alphabetStart + 1)
                .Select(i => (char)i)
                .ToArray();

            for (int i = 1; i < encryptedText.Length; i++)
            {
                foreach (var k in GetAllKeys(i, alphabet))
                {
                    string decryptedText = Vigenere.Decrypt(encryptedText, k);

                    if (decryptedText == originalText)
                    {
                        return k;
                    }
                }
            }

            return null;
        }
        private static IEnumerable<string> GetAllKeys(int length, IEnumerable<char> alphabet, string current = "")
        {
            if (current.Length > length)
                yield break;

            if (current.Length == length)
            {
                //Console.WriteLine(current);
                yield return current;
            }

            foreach (var c in alphabet)
            {
                foreach (var str in GetAllKeys(length, alphabet, current + c))
                {
                    yield return str;
                }
            }
        }
    }
}

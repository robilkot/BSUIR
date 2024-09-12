using System.Text;

namespace LW1
{
    public class PasswordGenerator(List<char> alphabet, int length = 12)
    {
        public int Length { get; set; } = length;
        public List<char> Alphabet { get; set; } = alphabet;
        public string Generate()
        {
            if (Alphabet is [])
                return "";

            Random random = new((int)(DateTime.Now.Ticks % int.MaxValue));
            StringBuilder builder = new(Length);

            for (int i = 0; i < Length; i++)
            {
                int symbolIndex = random.Next() % Alphabet.Count;
                builder = builder.Append(Alphabet[symbolIndex]);
            }

            return builder.ToString();
        }
    }
}

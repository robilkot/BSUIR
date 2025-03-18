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
    }
}

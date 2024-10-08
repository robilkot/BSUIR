namespace LW4
{
    public static class MathHelper
    {
        public static int PowerByModule(int @base, int exponent, int module)
        {
            int result = 1;
            @base %= module;

            while (exponent > 0)
            {
                if (exponent % 2 == 1)
                    result = (result * @base) % module;

                exponent /= 2;
                @base = (@base * @base) % module;
            }
            return result;
        }

        public static List<int> GetDivisors(int n)
        {
            List<int> divisors = [1];

            for (int i = 2; i * i <= n; i++)
            {
                if (n % i == 0)
                {
                    divisors.Add(i);

                    if (i * i != n)
                        divisors.Add(n / i);
                }
            }

            return divisors;
        }
    }
}

namespace LW4
{
    public static class PrimitiveElement
    {
        public static int ToPrimitiveElement(this int prime)
        {
            var groupOrder = prime - 1;
            var divisors = MathHelper.GetDivisors(groupOrder);

            for (int g = 2; g < prime; g++)
            {
                if (g.IsPrimitiveElement(groupOrder, divisors))
                    return g;
            }

            throw new InvalidOperationException();
        }

        private static bool IsPrimitiveElement(this int element, int groupOrder, List<int> orderDivisors)
        {
            foreach (int divisor in orderDivisors)
            {
                if (divisor == groupOrder)
                    continue;

                if (MathHelper.PowerByModule(element, divisor, groupOrder) == 1)
                    return false;
            }
            return true;
        }
    }
}

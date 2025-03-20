namespace LW1
{
    public static class Configurations
    {
        public static int SingleRun(int r, int? n = null)
        {
            IPairReader reader = n.HasValue
                ? new MockPairReader(n.Value)
                : new PairReader("input.txt");

            var (tacts, _) = reader
                .ReadPairs(r)
                .ToList()
                .Multiply();

            Debug.Log($"Количество тактов: {tacts}");
            
            return tacts;
        }

        public static void MultipleRuns((int min, int max, int step) r_range, (int min, int max, int step) n_range)
        {
            var output = File.OpenWrite("result.csv");
            Debug.Enabled = false;

            int[] n_values = Enumerable.Range(n_range.min, n_range.max).Where(i => i % n_range.step == 0).ToArray();
            int[] r_values = Enumerable.Range(r_range.min, r_range.max).Where(i => i % r_range.step == 0).ToArray();

            output.Write($"n, r, tacts\n".Select(c => (byte)c).ToArray());
            foreach (int n in n_values)
            {
                foreach (int r in r_values)
                {
                    int tacts = SingleRun(r, n);

                    output.Write($"{n}, {r}, {tacts}\n".Select(c => (byte)c).ToArray());
                    Console.WriteLine($"n={n},\tr={r},\ttacts={tacts}");
                }
                Console.WriteLine();
            }
            output.Close();
        }
    }
}

namespace LW2
{
    public static class InputGenerator
    {
        public static double Min = -1d;
        public static double Max = 1d;

        public static (double[,] A, double[,] B, double[,] E, double[,] G) GenerateInput(int p, int m, int q, int seed)
        {
            var A = new double[p, m];
            var B = new double[m, q];
            var E = new double[1, m];
            var G = new double[p, q];

            var random = new Random(seed);
            foreach (var arr in new List<double[,]>() { A, B, E, G })
            {
                for (int i = 0; i < arr.GetLength(0); i++)
                {
                    for (int k = 0; k < arr.GetLength(1); k++)
                    {
                        arr[i, k] = Min + (Max - Min) * random.NextDouble();
                    }
                }
            }

            return (A, B, E, G);
        }
    }
}

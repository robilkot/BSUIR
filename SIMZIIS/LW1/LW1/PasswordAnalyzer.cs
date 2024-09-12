using System.Diagnostics;

namespace LW1
{
    public class PasswordAnalyzer(PasswordGenerator generator, long distributionSamples = 50000, long bruteforceSamples = 100)
    {
        private readonly long DistributionSamples = distributionSamples;
        private readonly long BruteforceSamples = bruteforceSamples;
        public PasswordGenerator Generator { get; set; } = generator;
        public Dictionary<char, double> GetSymbolsDistribution()
        {
            Dictionary<char, int> symbolsCount = Generator.Alphabet.Select(c => (c, 0)).ToDictionary();
            long totalSymbols = 0;

            for (int i = 0; i < DistributionSamples; i++)
            {
                var password = Generator.Generate();

                foreach (char c in password)
                {
                    symbolsCount[c]++;
                }
                totalSymbols += password.Length;
            }

            return symbolsCount
                .Select(kvp => (kvp.Key, (double)kvp.Value / totalSymbols))
                .ToDictionary();
        }
        public TimeSpan GetMediumBruteforceTime()
        {
            string currentAttemptTarget = Generator.Generate();

            TimeSpan totalTime = TimeSpan.Zero;

            for (int i = 0; i < BruteforceSamples; i++)
            {
                var stopwatch = Stopwatch.StartNew();

                _ = TryCrack(currentAttemptTarget, string.Empty);
                
                totalTime = totalTime.Add(stopwatch.Elapsed);
            }

            return totalTime / BruteforceSamples;
        }
        private bool TryCrack(string target, string current)
        {
            if (current == target)
                return true;

            if (current.Length > target.Length)
                return false;

            foreach (var c in Generator.Alphabet)
            {
                if (TryCrack(target, current + c)) return true;
            }

            return false;
        }
    }
}

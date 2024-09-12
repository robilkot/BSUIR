using System.Collections.Immutable;
using System.Numerics;

namespace LW1
{
    public static class Fourier
    {
        public static ImmutableList<Complex> FFT(ImmutableList<Complex> input)
        {
            int samples = input.Count;
            if (samples == 1)
                return input;

            // Even array
            List<Complex> evenList = [];
            for (int i = 0; i < (samples / 2); i++)
            {
                evenList.Add(input[2 * i]);
            }
            evenList = [.. FFT([.. evenList])];

            // Odd array
            List<Complex> oddList = [];
            for (int i = 0; i < (samples / 2); i++)
            {
                oddList.Add(input[(2 * i) + 1]);
            }
            oddList = [.. FFT([.. oddList])];

            // Result
            var result = new Complex[samples];

            for (int i = 0; i < (samples / 2); i++)
            {
                double angle = -2.0 * i * Math.PI / samples;
                Complex w = new(Math.Cos(angle), Math.Sin(angle));
                Complex even = evenList[i];
                Complex odd = oddList[i];

                result[i] = even + (w * odd);
                result[i + (samples / 2)] = even - (w * odd);
            }
            return [.. result];
        }

        public static ImmutableList<Complex> GetDiscreteValues(
            Func<double, double> func,
            double frequency, 
            double min = 0,
            double max = Math.Tau)
        {
            double step = (max - min) / frequency;

            List<Complex> data = [];

            for (double x = min; x < max; x += step)
                data.Add(func(x));

            return ImmutableList.CreateRange(data);
        }
    }
}

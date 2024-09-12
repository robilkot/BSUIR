using System.Drawing;

namespace LW2
{
    public static class ImageProcessor
    {
#pragma warning disable CA1416
        public static Bitmap MedianFilter(this Bitmap source, int diameter = 1)
        {
            Bitmap result = new(source.Width, source.Height);

            int windowSize = diameter * diameter;
            Color[] window = new Color[windowSize];

            for (int i = 0; i < source.Width; i++)
            {
                for (int j = 0; j < source.Height; j++)
                {
                    // Fill window array
                    for (int w = 0; w < windowSize; w++)
                    {
                        int x = i - diameter / 2 + (w % diameter);
                        int y = j - diameter / 2 + (w / diameter);

                        // Ignore values out of bounds
                        if (y < 0 || y >= source.Height || x < 0 || x >= source.Width)
                        {
                            window[w] = Color.Black;
                            continue;
                        }

                        window[w] = source.GetPixel(x, y);
                    }

                    Array.Sort(window, (c1, c2) => c1.ToLuminance().CompareTo(c2.ToLuminance()));

                    // Set result value to median from window
                    result.SetPixel(i, j, window[windowSize / 2]);
                }
            }

            return result;
        }
#pragma warning restore CA1416

        private static double ToLuminance(this Color color) => (color.R * 0.3) + (color.G * 0.59) + (color.G * 0.11);
    }
}

using System.Drawing;

namespace LW3
{
    public static class ImageProcessor
    {
#pragma warning disable CA1416
        public static Bitmap EqualizeBrightness(this Bitmap source, Bitmap target)
        {
            var brightness1 = GetBrightness(source);
            var brightness2 = GetBrightness(target);

            var medium = (brightness1 + brightness2) / 2;
            var brightDifference = medium - brightness2;

            return BrightnessCorrect(source, -brightDifference);
        }

        private static Bitmap BrightnessCorrect(Bitmap source, double brightDifference)
        {
            Bitmap result = new(source.Width, source.Height);

            for (int x = 0; x < source.Width; x++)
            {
                for (int y = 0; y < source.Height; y++)
                {
                    var color = source.GetPixel(x, y);

                    var red = (int)Math.Clamp(color.R + brightDifference, 0, 255);
                    var green = (int)Math.Clamp(color.G + brightDifference, 0, 255);
                    var blue = (int)Math.Clamp(color.B + brightDifference, 0, 255);

                    var newColor = Color.FromArgb(255, red, green, blue);
                    result.SetPixel(x, y, newColor);
                }
            }

            return result;
        }

        public static double GetBrightness(Bitmap image)
        {
            double brightLevel = 0;

            for (int i = 0; i < image.Width; i++)
            {
                for (int j = 0; j < image.Height; j++)
                {
                    brightLevel += image.GetPixel(i, j).ToLuminance();
                }
            }

            return brightLevel / (image.Width * image.Height);
        }

        private static double ToLuminance(this Color color) 
            => (color.R * 0.3) + (color.G * 0.59) + (color.G * 0.11);
#pragma warning restore CA1416
    }
}

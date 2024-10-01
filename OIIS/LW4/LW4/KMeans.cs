using SkiaSharp;

namespace LW4
{
    class KMeans
    {
        private readonly int _maxIterations;
        private readonly int _clustersCount;
        private readonly List<SKColor> _pixels = [];
        private readonly List<SKColor> _centers = []; 
        private int PixelCount => _pixels.Count;

        public KMeans(SKBitmap bitmap, int clustersCount, int maxIterations)
        {
            _maxIterations = maxIterations;
            _pixels = [.. bitmap.Pixels];
            _clustersCount = clustersCount;

            ChooseRandomCenters();
        }

        private void ChooseRandomCenters()
        {
            Random random = new();
            
            SKColor temp = new();
            SKColor[] mas = new SKColor[_clustersCount];

            for (int i = 0; i < _clustersCount; i++)
            {
                mas[i] = new SKColor();
            }

            for (int i = 0; i < _clustersCount; i++)
            {
                temp = _pixels[random.Next(0, PixelCount)];
                for (int j = i; j < _clustersCount; j++)
                {
                    if (temp.Red != mas[j].Red && temp.Green != mas[j].Green && temp.Blue != mas[j].Blue)
                    {
                        mas[j] = temp;
                    }
                    else
                    {
                        i--;
                        break;
                    }
                }
            }

            for (int i = 0; i < _clustersCount; i++)
            {
                _centers.Add(mas[i]);
            }
        }

        private static double Distance(SKColor k1, SKColor k2)
            => Math.Sqrt(Math.Pow(k1.Red - k2.Red, 2) + Math.Pow(k1.Green - k2.Green, 2) + Math.Pow(k1.Blue - k2.Blue, 2));

        private static double Medium(double a, double b)
            => (a + b) / 2;

        // shit
        public List<SKColor> GetClusterCenters()
        {
            List<int> check_1 = new(PixelCount);
            List<int> check_2 = new(PixelCount);

            for (int i = 0; i < PixelCount; i++)
            {
                check_1.Add(-1);
                check_2.Add(-2);
            }

            int iter = 0;

            while (true)
            {
                {
                    for (int j = 0; j < PixelCount; j++)
                    {
                        double[] mas = new double[_clustersCount];

                        for (int i = 0; i < _clustersCount; i++)
                        {
                            mas[i] = Distance(_pixels[j], _centers[i]);
                        }

                        double min_dist = mas[0];
                        int m_k = 0;
                        for (int i = 0; i < _clustersCount; i++)
                        {
                            if (min_dist > mas[i])
                            {
                                min_dist = mas[i];
                                m_k = i;
                            }
                        }

                        _centers[m_k] = _centers[m_k]
                            .WithRed((byte)Medium(_pixels[j].Red, _centers[m_k].Red))
                            .WithGreen((byte)Medium(_pixels[j].Green, _centers[m_k].Green))
                            .WithBlue((byte)Medium(_pixels[j].Blue, _centers[m_k].Blue));
                    }

                    int[] mass = new int[PixelCount];
                    for (int k = 0; k < PixelCount; k++)
                    {
                        double[] mas = new double[_clustersCount];

                        for (int i = 0; i < _clustersCount; i++)
                        {
                            mas[i] = Distance(_pixels[k], _centers[i]);
                        }

                        double min_dist = mas[0];
                        int m_k = 0;
                        for (int i = 0; i < _clustersCount; i++)
                        {
                            if (min_dist > mas[i])
                            {
                                min_dist = mas[i];
                                m_k = i;
                            }
                        }
                        mass[k] = m_k;
                    }

                    for (int i = 0; i < PixelCount; i++)
                    {
                        check_1[i] = mass[i];
                    }

                    int itr = _clustersCount + 1;
                    for (int i = 0; i < _clustersCount; i++)
                    {
                        for (int j = 0; j < PixelCount; j++)
                        {
                            if (mass[j] == i)
                            {
                                mass[j] = ++itr;
                            }
                        }
                    }
                }

                iter++;
                if (check_1 == check_2 || iter >= _maxIterations)
                {
                    break;
                }
                check_2 = check_1;
            }

            return [.. _centers];
        }
    }
}
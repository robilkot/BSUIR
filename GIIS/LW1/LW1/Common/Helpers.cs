namespace LW1.Common
{
    public static class Helpers
    {
        public static double CrossProduct(Point a, Point b, Point c)
        {
            return (b.X - a.X) * (c.Y - a.Y) - (b.Y - a.Y) * (c.X - a.X);
        }

        public static double Distance(Point a, Point b)
        {
            double dx = a.X - b.X;
            double dy = a.Y - b.Y;
            return Math.Sqrt(dx * dx + dy * dy);
        }

        public static double Distance(PointF a, PointF b)
        {
            double dx = a.X - b.X;
            double dy = a.Y - b.Y;
            return Math.Sqrt(dx * dx + dy * dy);
        }

        public static PointF ComputeCircumcenter(Point a, Point b, Point c)
        {
            double d = 2 * (a.X * (b.Y - c.Y) + b.X * (c.Y - a.Y) + c.X * (a.Y - b.Y));
            double ax2 = a.X * a.X + a.Y * a.Y;
            double bx2 = b.X * b.X + b.Y * b.Y;
            double cx2 = c.X * c.X + c.Y * c.Y;
            double centerX = (ax2 * (b.Y - c.Y) + bx2 * (c.Y - a.Y) + cx2 * (a.Y - b.Y)) / d;
            double centerY = (ax2 * (c.X - b.X) + bx2 * (a.X - c.X) + cx2 * (b.X - a.X)) / d;
            return new PointF((float)centerX, (float)centerY);
        }
        // Вычисляет точку пересечения луча с bbox. Возвращает ближайшую точку пересечения (t >= 0).
        public static PointF? ComputeRayBoxIntersection(PointF origin, PointF dir, Rectangle box)
        {
            List<double> tValues = [];
            if (Math.Abs(dir.X) > 1e-6)
            {
                double t = (box.Left - origin.X) / dir.X;
                if (t >= 0)
                {
                    double y = origin.Y + t * dir.Y;
                    if (y >= box.Top && y <= box.Bottom)
                        tValues.Add(t);
                }
                t = (box.Right - origin.X) / dir.X;
                if (t >= 0)
                {
                    double y = origin.Y + t * dir.Y;
                    if (y >= box.Top && y <= box.Bottom)
                        tValues.Add(t);
                }
            }
            if (Math.Abs(dir.Y) > 1e-6)
            {
                double t = (box.Top - origin.Y) / dir.Y;
                if (t >= 0)
                {
                    double x = origin.X + t * dir.X;
                    if (x >= box.Left && x <= box.Right)
                        tValues.Add(t);
                }
                t = (box.Bottom - origin.Y) / dir.Y;
                if (t >= 0)
                {
                    double x = origin.X + t * dir.X;
                    if (x >= box.Left && x <= box.Right)
                        tValues.Add(t);
                }
            }
            if (tValues.Count == 0)
                return null;
            double tMin = tValues.Min();
            return new PointF((float)(origin.X + tMin * dir.X), (float)(origin.Y + tMin * dir.Y));
        }
    }
}
namespace LW1.Other.Helpers
{
    public static class OtherHelpers
    {

        // Метод проверки, удовлетворяет ли тройка точек условию Делоне:
        // описанная окружность треугольника не должна содержать никаких других точек.
        public static bool IsDelaunayTriangle(Point a, Point b, Point c, List<Point> points)
        {
            // Вычисляем определитель, чтобы проверить, не коллинеарны ли точки
            double d = 2 * (a.X * (b.Y - c.Y) + b.X * (c.Y - a.Y) + c.X * (a.Y - b.Y));
            if (Math.Abs(d) < 1e-6) return false; // вырожденный треугольник

            double ax2 = a.X * a.X + a.Y * a.Y;
            double bx2 = b.X * b.X + b.Y * b.Y;
            double cx2 = c.X * c.X + c.Y * c.Y;

            double centerX = (ax2 * (b.Y - c.Y) + bx2 * (c.Y - a.Y) + cx2 * (a.Y - b.Y)) / d;
            double centerY = (ax2 * (c.X - b.X) + bx2 * (a.X - c.X) + cx2 * (b.X - a.X)) / d;

            // Вычисляем квадрат радиуса описанной окружности
            double r2 = (a.X - centerX) * (a.X - centerX) + (a.Y - centerY) * (a.Y - centerY);

            // Если любая другая точка лежит строго внутри окружности, то треугольник не удовлетворяет условию Делоне.
            foreach (var p in points)
            {
                if (p.Equals(a) || p.Equals(b) || p.Equals(c))
                    continue;
                double dist2 = (p.X - centerX) * (p.X - centerX) + (p.Y - centerY) * (p.Y - centerY);
                if (dist2 < r2 - 1e-6)
                    return false;
            }
            return true;
        }

        public static bool AreCollinear(Point a, Point b, Point c)
        {
            return Math.Abs(a.X * (b.Y - c.Y) + b.X * (c.Y - a.Y) + c.X * (a.Y - b.Y)) < 1e-6;
        }
    }
}
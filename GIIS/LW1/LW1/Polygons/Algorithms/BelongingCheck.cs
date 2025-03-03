using LW1.Common;

namespace LW1.Polygons
{
    public class BelongingCheck : IAlgorithm<(PolygonParameters polygon, PointDrawingParameters pointParams), bool>
    {
        public bool Execute((PolygonParameters polygon, PointDrawingParameters pointParams) param)
        {
            var (polygon, pointParams) = (param.polygon, param.pointParams);

            // Извлекаем точку и список вершин
            Point p = pointParams.Point.Value;
            var vertices = polygon.Vertices.Select(v => v.Value).ToList();
            int n = vertices.Count;
            if (n < 3)
                return false;

            bool inside = false;
            // Перебор вершин с использованием предыдущей вершины (j) и текущей (i)
            for (int i = 0, j = n - 1; i < n; j = i++)
            {
                Point vi = vertices[i];
                Point vj = vertices[j];

                // Если точка лежит на границе отрезка, возвращаем true
                if (IsPointOnSegment(vj, vi, p))
                    return true;

                // Проверяем пересечение горизонтальной луча, исходящего из точки p, с ребром (vj,vi)
                // Условие: p.Y находится между значениями vj.Y и vi.Y (не включая равенство, т.к. граница уже проверена)
                if ((vi.Y > p.Y) != (vj.Y > p.Y))
                {
                    // Вычисляем координату X точки пересечения ребра с горизонтальной прямой, проходящей через p.Y
                    double intersectX = vi.X + (double)(p.Y - vi.Y) * (vj.X - vi.X) / (vj.Y - vi.Y);
                    // Если пересечение совпадает с точкой p, значит p лежит на границе
                    if (intersectX == p.X)
                        return true;
                    // Если пересечение правее точки p, переключаем флаг
                    if (intersectX > p.X)
                        inside = !inside;
                }
            }
            return inside;
        }

        /// <summary>
        /// Проверяет, лежит ли точка p на отрезке, заданном точками a и b.
        /// </summary>
        private static bool IsPointOnSegment(Point a, Point b, Point p)
        {
            // Для целочисленных координат проверка на коллинеарность осуществляется через вычисление векторного произведения
            int cross = (b.X - a.X) * (p.Y - a.Y) - (b.Y - a.Y) * (p.X - a.X);
            if (cross != 0)
                return false;

            // Проверяем, что p находится между a и b
            int minX = Math.Min(a.X, b.X);
            int maxX = Math.Max(a.X, b.X);
            int minY = Math.Min(a.Y, b.Y);
            int maxY = Math.Max(a.Y, b.Y);

            return (p.X >= minX && p.X <= maxX && p.Y >= minY && p.Y <= maxY);
        }
    }
}

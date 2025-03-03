using LW1.Common;

namespace LW1.Polygons
{
    public class ConvexCheck : IAlgorithm<PolygonParameters, bool>
    {
        public bool Execute(PolygonParameters polygon)
        {
            var vertices = polygon.Vertices.Select(v => v.Value).ToList();
            int n = vertices.Count;

            // Если точек меньше трёх, полигон не может быть валидным (или трактуется как вырожденный)
            if (n < 3)
                return false;

            // Флаг, определяющий направление поворота (левый или правый)
            bool? isLeftTurn = null;

            for (int i = 0; i < n; i++)
            {
                // Берём тройки: текущая, следующая и следующая за ней (с циклическим переходом)
                var a = vertices[i];
                var b = vertices[(i + 1) % n];
                var c = vertices[(i + 2) % n];

                double cross = CrossProduct(a, b, c);

                // Если точки коллинеарны, пропускаем (не влияет на выпуклость)
                if (Math.Abs(cross) < 1e-9)
                    continue;

                // При первой ненулевой ориентации устанавливаем направление поворота
                if (isLeftTurn == null)
                {
                    isLeftTurn = cross > 0;
                }
                // Если направление меняется – полигон невыпуклый
                else if (isLeftTurn != (cross > 0))
                {
                    return false;
                }
            }

            return true;
        }
        private static double CrossProduct(Point a, Point b, Point c)
        {
            // Вектор AB = b - a и вектор BC = c - b
            double abx = b.X - a.X;
            double aby = b.Y - a.Y;
            double bcx = c.X - b.X;
            double bcy = c.Y - b.Y;
            return abx * bcy - aby * bcx;
        }
    }
}

namespace LW1.Polygons.Common
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
        public static bool IsPointInsidePolygon(Point p, PolygonParameters poly)
        {
            return new BelongingCheck().Execute((poly, p));
        }
    }
}

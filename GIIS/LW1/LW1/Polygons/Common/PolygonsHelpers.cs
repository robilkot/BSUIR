namespace LW1.Polygons.Common
{
    public static class PolygonsHelpers
    {
        public static bool IsPointInsidePolygon(Point p, PolygonParameters poly)
        {
            return new BelongingCheck().Execute((poly, p));
        }
    }
}

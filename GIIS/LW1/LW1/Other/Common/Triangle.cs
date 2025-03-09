using System.Collections;

namespace LW1.Other.Voronoi
{
    public partial class VoronoiDiagram
    {
        public record struct Triangle(Point A, Point B, Point C, PointF Circumcenter) : IEnumerable<Point>
        {
            public IEnumerator<Point> GetEnumerator()
            {
                List<Point> list = [A, B, C];
                return list.GetEnumerator();
            }

            IEnumerator IEnumerable.GetEnumerator()
            {
                return GetEnumerator();
            }
        }
    }
}
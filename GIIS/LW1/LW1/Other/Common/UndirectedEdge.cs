namespace LW1.Other.Helpers
{
    public record struct UndirectedEdge(Point A, Point B);

    public class UndirectedEdgeComparer : IEqualityComparer<UndirectedEdge>
    {
        public bool Equals(UndirectedEdge e1, UndirectedEdge e2)
        {
            return e1.A.Equals(e2.A) && e1.B.Equals(e2.B) || e1.B.Equals(e2.A) && e1.A.Equals(e2.B);
        }

        public int GetHashCode(UndirectedEdge edge)
        {
            return edge.A.GetHashCode() ^ edge.B.GetHashCode();
        }
    }
}
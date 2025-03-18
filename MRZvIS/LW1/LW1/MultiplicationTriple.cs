namespace LW1
{
    public class MultiplicationTriple
    {
        public int Index { get; init; }
        
        public Number Multiplicand;
        public Number Factor;
        public Number PartialSum;

        public override string ToString() =>
                $"mul: {Multiplicand}\n" +
                $"fac: {Factor}\n" +
                $"sum: {PartialSum}\n";
    };
}

namespace LW1
{
    public class MultiplicationTriple
    {
        public int Index { get; init; }
        
        public required Number Multiplicand;
        public required Number Factor;
        public required Number PartialSum;

        public override string ToString() =>
                $"Множимое:        {Multiplicand}\n" +
                $"Множитель:       {Factor}\n" +
                $"Частичная сумма: {PartialSum}\n";
    };
}

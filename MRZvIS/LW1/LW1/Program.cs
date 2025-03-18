using LW1;


int r = 4;
int n = 4;
bool mock_values = true;
Debug.Enabled = true;


IPairReader reader = mock_values 
    ? new MockPairReader(n)
    : new PairReader("input.txt");

var (tacts, _) = reader
    .ReadPairs(r)
    .ToList()
    .Multiply();

Console.WriteLine(tacts);
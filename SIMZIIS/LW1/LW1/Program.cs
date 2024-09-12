using LW1;

// Set alphabet by given task
var alphabet =
    Enumerable.Range('а', 'я' - 'а' + 1)
    .Select(i => (char)i)
    .Append('ё')
    .Concat(
        Enumerable.Range(0, 10)
        .Select(i => i.ToString()[0]))
    .ToList();

// Set up generator and analyzer
PasswordGenerator generator = new(alphabet, 8);
PasswordAnalyzer analyzer = new(generator, 50000, 2);

// Format output
Console.WriteLine($"Alphabet ({alphabet.Count} symbols): {string.Join(string.Empty, alphabet)}");
Console.WriteLine();
Console.WriteLine($"Sample generated password: '{generator.Generate()}'");
Console.WriteLine();

#region Distribution

var distribution = analyzer.GetSymbolsDistribution();
var idealPercent = 100d / alphabet.Count;

Console.WriteLine($"Ideal percent for distribution: {idealPercent:0.000}%");
Console.WriteLine();
Console.WriteLine($"Symbol\tOccur.\tDeviation");
foreach (var kvp in distribution)
{
    var percent = kvp.Value * 100;
    Console.WriteLine($"{kvp.Key}\t{percent:0.000}%\t{Math.Abs(percent - idealPercent):0.000}%");
}

#endregion

Console.WriteLine();

#region Bruteforce

List<int> passwordLengthSamples = [1, 2, 3, 4, 5, 6];

foreach (var passwordLengthSample in passwordLengthSamples)
{
    PasswordGenerator bfGenerator = new(alphabet, passwordLengthSample);
    PasswordAnalyzer bfAnalyzer = new(bfGenerator, 50000, 2);

    var bruteforceTime = bfAnalyzer.GetMediumBruteforceTime();
    Console.WriteLine($"Bruteforce time for length {passwordLengthSample}: {bruteforceTime}");
}

#endregion
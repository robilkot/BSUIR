using LW4;

var P = 8581;

var secret = SecretGenerator.Generate(P);

Console.WriteLine(secret);
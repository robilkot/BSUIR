using LW2;

var encrypter = new Vigenere('A', 'Z');

var message = "ATTACKATDAWN";
var key = "TEST";

Console.WriteLine(message);
Console.WriteLine(key);

var encrypted = encrypter.Encrypt(message, key);

Console.WriteLine(encrypted);

var decrypted = encrypter.Decrypt(encrypted, key);

Console.WriteLine(decrypted);

var analyzer = new Analyzer(encrypter);

var hackedKey = analyzer.BruteForceAttack(encrypted, key); 

if (hackedKey is not null)
{
    Console.WriteLine($"Brute force attack successful. Key: '{hackedKey}'");
}

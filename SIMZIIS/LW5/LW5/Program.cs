using System.Security.Cryptography;
using System.Text;


string[] testCases = [
    "Hello, world",
    "SIMZIIS is cool",
    "I am a student!!!",
    "LetMeIn",
    "Don't worry, be happy",
    "Lorem ipsum dolor sit amet",
    "I have nothing to hide"
    ];

string toEncrypt = "Hello, world";

UnicodeEncoding byteConverter = new();
RSACryptoServiceProvider RSA = new();

var privateKey = RSA.ExportParameters(true);
var publicKey = RSA.ExportParameters(false);

Console.WriteLine($"To encode: {toEncrypt}");

byte[] toEncryptBytes = byteConverter.GetBytes(toEncrypt);
byte[] encrypted = RSAEncrypt(toEncryptBytes, publicKey, false);

Console.WriteLine("Encrypt str: " + byteConverter.GetString(encrypted));

byte[] decBytes = RSADecrypt(encrypted, privateKey, false);

Console.WriteLine("Decrypt str: " + byteConverter.GetString(decBytes));

Console.ReadKey();


static byte[] RSAEncrypt(byte[] DataToEncrypt, RSAParameters RSAKeyInfo, bool DoOAEPPadding)
{
    RSACryptoServiceProvider RSA = new();

    RSA.ImportParameters(RSAKeyInfo);

    return RSA.Encrypt(DataToEncrypt, DoOAEPPadding);
}

static byte[] RSADecrypt(byte[] DataToDecrypt, RSAParameters RSAKeyInfo, bool DoOAEPPadding)
{
    RSACryptoServiceProvider RSA = new();

    RSA.ImportParameters(RSAKeyInfo);

    return RSA.Decrypt(DataToDecrypt, DoOAEPPadding);
}
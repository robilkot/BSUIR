using System.Security.Cryptography;
using System.Text;

namespace LW3;

public class SecureDataManager
{
    public static bool WriteToConsole;

    public List<string> NonConfidentialData = [];
    public List<SecureStringWrapper> ConfidentialData = [];

    private static readonly byte[] EncryptionKey = Encoding.UTF8.GetBytes("12345678abcdefgh");
    private static readonly byte[] IV = new byte[16];

    public void AddNonConfidentialData(string data)
    {
        if (string.IsNullOrEmpty(data))
            throw new ArgumentException("Data cannot be null or empty");

        NonConfidentialData.Add(data);
        if (WriteToConsole) Console.WriteLine($"Added non-confidential data: {data}");
    }

    public void AddConfidentialData(string sensitiveData)
    {
        if (string.IsNullOrEmpty(sensitiveData))
            throw new ArgumentException("Data cannot be null or empty");

        var encryptedData = EncryptData(sensitiveData);
        ConfidentialData.Add(new SecureStringWrapper(encryptedData));

        OverwriteMemory(sensitiveData);
        if (WriteToConsole) Console.WriteLine("Added confidential data (encrypted)");
    }

    public void UpdateConfidentialData(int index, string newData)
    {
        if (index < 0 || index >= ConfidentialData.Count)
            throw new ArgumentOutOfRangeException(nameof(index));

        var encryptedData = EncryptData(newData);
        ConfidentialData[index].UpdateData(encryptedData);

        OverwriteMemory(newData);
        if (WriteToConsole) Console.WriteLine($"Updated confidential data at index {index}");
    }

    public void UpdateNonConfidentialData(int index, string newData)
    {
        if (index < 0 || index >= NonConfidentialData.Count)
            throw new ArgumentOutOfRangeException(nameof(index));

        NonConfidentialData[index] = newData;

        if (WriteToConsole) Console.WriteLine($"Updated non-confidential data at index {index}");
    }

    public void DeleteConfidentialData(int index)
    {
        if (index < 0 || index >= ConfidentialData.Count)
            throw new ArgumentOutOfRangeException(nameof(index));

        ConfidentialData[index].Dispose();
        ConfidentialData.RemoveAt(index);
        if (WriteToConsole) Console.WriteLine($"Deleted confidential data at index {index}");
    }

    public void DeleteNonConfidentialData(int index)
    {
        if (index < 0 || index >= NonConfidentialData.Count)
            throw new ArgumentOutOfRangeException(nameof(index));

        NonConfidentialData.RemoveAt(index);
        if (WriteToConsole) Console.WriteLine($"Deleted nonconfidential data at index {index}");
    }

    public string GetConfidentialData(int index)
    {
        if (index < 0 || index >= ConfidentialData.Count)
            throw new ArgumentOutOfRangeException(nameof(index));

        var encryptedData = ConfidentialData[index].GetData();
        return DecryptData(encryptedData);
    }

    private byte[] EncryptData(string data)
    {
        using var aes = Aes.Create();
        aes.Key = EncryptionKey;
        aes.IV = IV;

        using var encryptor = aes.CreateEncryptor();
        using var ms = new MemoryStream();
        using (var cs = new CryptoStream(ms, encryptor, CryptoStreamMode.Write))
        using (var writer = new StreamWriter(cs))
        {
            writer.Write(data);
        }
        return ms.ToArray();
    }

    private string DecryptData(byte[] encryptedData)
    {
        using var aes = Aes.Create();
        aes.Key = EncryptionKey;
        aes.IV = IV;

        using var decryptor = aes.CreateDecryptor();
        using var ms = new MemoryStream(encryptedData);
        using var cs = new CryptoStream(ms, decryptor, CryptoStreamMode.Read);
        using var reader = new StreamReader(cs);
        return reader.ReadToEnd();
    }

    private void OverwriteMemory(string data)
    {
        unsafe
        {
            fixed (char* ptr = data)
            {
                for (int i = 0; i < data.Length; i++)
                {
                    ptr[i] = '\0';
                }
            }
        }
    }

    public void DisplayNonConfidentialData()
    {
        if (WriteToConsole) Console.WriteLine("\nNon-confidential data:");
        for (int i = 0; i < NonConfidentialData.Count; i++)
        {
            if (WriteToConsole) Console.WriteLine($"{i}: {NonConfidentialData[i]}");
        }
    }

    public void DisplayConfidentialDataSummary()
    {
        if (WriteToConsole) Console.WriteLine($"\nConfidential data items: {ConfidentialData.Count}");
    }
}

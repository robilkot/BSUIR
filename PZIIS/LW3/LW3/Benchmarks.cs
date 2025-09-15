using BenchmarkDotNet.Attributes;
using System.Security.Cryptography;
using System.Text;

namespace LW3;

public class MemoryUsageBenchmarks
{
    private const int LargeDataCount = 10000;
    private const string LargeData = "This is a large confidential data string that contains multiple sensitive elements and is designed to test memory usage patterns under heavy load conditions.";

    [Benchmark]
    public long RegularDataMemoryUsage()
    {
        var list = new List<string>();
        for (int i = 0; i < LargeDataCount; i++)
        {
            list.Add($"{LargeData}_{i}");
        }

        long totalLength = 0;
        foreach (var item in list)
        {
            totalLength += item.Length * sizeof(char);
        }

        return totalLength;
    }

    [Benchmark]
    public long SecureDataMemoryUsage()
    {
        var list = new List<byte[]>();
        for (int i = 0; i < LargeDataCount; i++)
        {
            list.Add(EncryptData($"{LargeData}_{i}"));
        }

        long totalLength = 0;
        foreach (var item in list)
        {
            totalLength += item.Length;
        }

        return totalLength;
    }

    private static byte[] EncryptData(string data)
    {
        using var aes = Aes.Create();
        aes.Key = Encoding.UTF8.GetBytes("12345678abcdefgh");
        aes.IV = new byte[16];

        using var encryptor = aes.CreateEncryptor();
        using var ms = new MemoryStream();
        using (var cs = new CryptoStream(ms, encryptor, CryptoStreamMode.Write))
        using (var writer = new StreamWriter(cs))
        {
            writer.Write(data);
        }
        return ms.ToArray();
    }
}

[MemoryDiagnoser]
[MinIterationCount(10)]
[MaxIterationCount(15)]
[InvocationCount(15)]
public class SecurityBenchmarks
{
    private SecureDataManager secureManager;
    private List<string> regularData;
    private const string TestData = "This is a confidential test data string that contains sensitive information like password: P@ssw0rd123! and credit card: 1234-5678-9012-3456";
    private const int DataCount = 1000;

    [IterationSetup]
    public void SetupIt()
    {
        for (int i = 0; i < DataCount; i++)
        {
            secureManager.AddNonConfidentialData($"{TestData}_{i}");
            secureManager.AddConfidentialData($"{TestData}_{i}");
        }
    }

    [GlobalSetup]
    public void Setup()
    {
        secureManager = new SecureDataManager();
        regularData = new(100);
    }

    [Benchmark]
    public void AddRegularDataBenchmark()
    {
        for (int i = 0; i < DataCount; i++)
        {
            secureManager.AddNonConfidentialData($"{TestData}_{i}");
        }
    }

    [Benchmark]
    public void AddSecureDataBenchmark()
    {
        for (int i = 0; i < DataCount; i++)
        {
            secureManager.AddConfidentialData($"{TestData}_{i}");
        }
    }

    [Benchmark]
    public void ReadRegularDataBenchmark()
    {
        for (int i = 0; i < Math.Min(DataCount, 100); i++)
        {
            var data = regularData[i % regularData.Count];
        }
    }

    [Benchmark]
    public void ReadSecureDataBenchmark()
    {
        for (int i = 0; i < Math.Min(DataCount, 100); i++)
        {
            var data = secureManager.GetConfidentialData(i % DataCount);
        }
    }

    //[Benchmark]
    //public void UpdateRegularDataBenchmark()
    //{
    //    for (int i = 0; i < Math.Min(DataCount, 100); i++)
    //    {
    //        regularData[i % regularData.Count] = $"{TestData}_updated_{i}";
    //    }
    //}

    //[Benchmark]
    //public void UpdateSecureDataBenchmark()
    //{
    //    for (int i = 0; i < Math.Min(DataCount, 100); i++)
    //    {
    //        secureManager.UpdateConfidentialData(i % DataCount, $"{TestData}_updated_{i}");
    //    }
    //}

    [Benchmark]
    public void DeleteRegularDataBenchmark()
    {
        while (regularData.Count > 0)
        {
            regularData.RemoveAt(0);
        }
    }

    [Benchmark]
    public void DeleteSecureDataBenchmark()
    {
        while (secureManager.ConfidentialData.Count > 0)
        {
            secureManager.DeleteConfidentialData(0);
        }
    }
}

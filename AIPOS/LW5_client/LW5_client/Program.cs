using CommandLine;

class Program
{
    static void Main(string[] args)
    {
        var config = new ClientConfig();

        // Парсим аргументы командной строки
        Parser.Default.ParseArguments<ClientConfig>(args).WithParsed(o => config = o);

        if (config.Help)
        {
            Console.WriteLine(Parser.Default.FormatCommandLine(typeof(ClientConfig)));
            return;
        }

        if (string.IsNullOrEmpty(config.Method) || string.IsNullOrEmpty(config.Url))
        {
            Console.WriteLine("Specify method and url");
            return;
        }

        var client = new HttpClient(config);
        client.SendRequest();
    }
}

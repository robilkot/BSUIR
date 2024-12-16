
using CommandLine;

class Program
{
    static void Main(string[] args)
    {
        var config = new ServerConfig();

        Parser.Default.ParseArguments<ServerConfig>(args).WithParsed(o => config = o);

        if (config.Help)
        {
            Console.WriteLine(Parser.Default.FormatCommandLine(typeof(ServerConfig)));
            return;
        }

        if (!Directory.Exists(config.Directory))
        {
            Console.WriteLine($"File not found: {config.Directory}");
            return;
        }

        var server = new HttpServer(config);
        server.Start();
    }
}


using CommandLine;

class ServerConfig
{
    [Option('a', "address", Required = false, HelpText = "Listening IP", Default = "127.0.0.1")]
    public string Address { get; set; }

    [Option('p', "port", Required = false, HelpText = "Listening port", Default = 8080)]
    public int Port { get; set; }

    [Option('d', "directory", Required = false, HelpText = "Folder for sharing files", Default = "/")]
    public string Directory { get; set; } = string.Empty;

    [Option('h', "help", Required = false, HelpText = "Show help", Default = false)]
    public bool Help { get; set; }

    [Option('l', "logfile", Required = false, HelpText = "Log filepath", Default = "server.log")]
    public string LogFile { get; set; } = string.Empty;

    [Option('H', "headers", Required = false, HelpText = "Default headers in format key:value", Separator = ';')]
    public IEnumerable<string> Headers { get; set; } = [];
}

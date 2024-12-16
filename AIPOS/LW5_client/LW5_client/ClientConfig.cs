using CommandLine;

class ClientConfig
{
    [Option('m', "method", Required = false, HelpText = "HTTP method (GET, POST, ...)", Default = "GET")]
    public string Method { get; set; } = string.Empty;

    [Option('u', "url", Required = false, HelpText = "Request URL", Default = "http://example.com")]
    public string Url { get; set; } = string.Empty;

    [Option('H', "headers", Required = false, HelpText = "Headers in format key:value", Separator = ';')]
    public IEnumerable<string> Headers { get; set; } = [];

    [Option('b', "body", Required = false, HelpText = "String body")]
    public string Body { get; set; } = string.Empty;

    [Option('f', "file", Required = false, HelpText = "File body path")]
    public string File { get; set; } = string.Empty;

    [Option('h', "help", Required = false, HelpText = "Show help", Default = false)]
    public bool Help { get; set; }
}

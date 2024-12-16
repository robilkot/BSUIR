using System.Net.Sockets;
using System.Text;

class HttpClient
{
    private readonly ClientConfig _config;

    public HttpClient(ClientConfig config)
    {
        _config = config;
    }

    public void SendRequest()
    {
        var uri = new Uri(_config.Url);
        using var client = new TcpClient(uri.Host, uri.Port > 0 ? uri.Port : 80);

        using var stream = client.GetStream();
        using var writer = new StreamWriter(stream, Encoding.ASCII) { AutoFlush = true };
        using var reader = new StreamReader(stream, Encoding.ASCII);

        // Создаем HTTP-запрос
        var request = BuildRequest(uri);
        Console.WriteLine("Sending request:\n" + request);

        writer.Write(request);

        // Получаем и выводим ответ
        var response = reader.ReadToEnd();
        Console.WriteLine("Response:\n" + response);
    }

    private string BuildRequest(Uri uri)
    {
        var requestLine = $"{_config.Method.ToUpper()} {uri.PathAndQuery} HTTP/1.1";
        var headers = new StringBuilder();
        var body = GetRequestBody();

        headers.AppendLine(requestLine);
        headers.AppendLine($"Host: {uri.Host}");
        headers.AppendLine("Connection: close");

        foreach (var header in _config.Headers)
        {
            var headerParts = header.Split(':', 2);
            if (headerParts.Length == 2)
            {
                headers.AppendLine($"{headerParts[0].Trim()}: {headerParts[1].Trim()}");
            }
        }

        if (!string.IsNullOrEmpty(body))
        {
            headers.AppendLine("Content-Type: " + GetContentType());
            headers.AppendLine($"Content-Length: {Encoding.UTF8.GetByteCount(body)}");
        }

        headers.AppendLine(); // Разделение заголовков и тела запроса

        if (!string.IsNullOrEmpty(body))
        {
            headers.AppendLine(body);
        }

        return headers.ToString();
    }

    private string GetRequestBody()
    {
        if (!string.IsNullOrEmpty(_config.Body))
        {
            return _config.Body;
        }

        if (!string.IsNullOrEmpty(_config.File) && File.Exists(_config.File))
        {
            return File.ReadAllText(_config.File);
        }

        return string.Empty;
    }

    private string GetContentType()
    {
        if (!string.IsNullOrEmpty(_config.File))
        {
            var extension = Path.GetExtension(_config.File).ToLower();
            return extension switch
            {
                ".html" => "text/html",
                ".css" => "text/css",
                ".js" => "application/javascript",
                ".json" => "application/json",
                ".png" => "image/png",
                ".jpg" or ".jpeg" => "image/jpeg",
                _ => "application/octet-stream",
            };
        }

        return "application/octet-stream";
    }
}

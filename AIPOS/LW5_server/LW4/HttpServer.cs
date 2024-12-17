using System.Net;
using System.Net.Sockets;
using System.Text;

class HttpServer
{
    private readonly ServerConfig _config;

    public HttpServer(ServerConfig config)
    {
        _config = config;
    }

    public void Start()
    {
        var listener = new TcpListener(IPAddress.Parse(_config.Address), _config.Port);
        listener.Start();

        Log("Server running on {0}:{1}", _config.Address, _config.Port);

        while (true)
        {
            try
            {
                var client = listener.AcceptTcpClient();
                new Thread(() => ProcessRequest(client)).Start();
            }
            catch (Exception ex)
            {
                Log("Error: {0}", ex.Message);
            }
        }
    }

    private void ProcessRequest(TcpClient client)
    {
        using var stream = client.GetStream();
        using var reader = new StreamReader(stream);
        using var writer = new StreamWriter(stream) { AutoFlush = true };

        var requestLine = reader.ReadLine();

        if (string.IsNullOrEmpty(requestLine))
        {
            WriteResponse(writer, HttpStatusCode.BadRequest, "Bad Request");
            return;
        }

        Log("Request: {0}", requestLine);

        var tokens = requestLine.Split(' ');
        if (tokens.Length < 3)
        {
            WriteResponse(writer, HttpStatusCode.BadRequest, "Bad Request");
            return;
        }

        var method = tokens[0];
        var url = tokens[1];
        var version = tokens[2];

        switch (method)
        {
            case "GET":
                HandleGetRequest(writer, url);
                break;
            case "POST":
                HandlePostRequest(reader, writer, url);
                break;
            case "OPTIONS":
                HandleOptionsRequest(writer);
                break;
            default:
                WriteResponse(writer, HttpStatusCode.MethodNotAllowed, "Not Allowed");
                break;
        }
    }

    private void HandleGetRequest(StreamWriter writer, string url)
    {
        string filePath = Path.Combine(_config.Directory, url.TrimStart('/'));

        if (!File.Exists(filePath))
        {
            WriteResponse(writer, HttpStatusCode.NotFound, "Not Found");
            return;
        }

        byte[] fileContent = File.ReadAllBytes(filePath);

        writer.WriteLine("HTTP/1.1 200 OK");
        writer.WriteLine("Content-Length: {0}", fileContent.Length);
        writer.WriteLine("Content-Type: {0}", GetContentType(filePath));

        foreach (var header in _config.Headers)
        {
            writer.WriteLine(header);
        }

        writer.WriteLine(); // Пустая строка завершает заголовки
        writer.BaseStream.Write(fileContent, 0, fileContent.Length);
    }

    private void HandlePostRequest(StreamReader reader, StreamWriter writer, string url)
    {
        string targetPath = Path.Combine(_config.Directory, url.TrimStart('/'));

        if (File.Exists(targetPath))
        {
            WriteResponse(writer, HttpStatusCode.Conflict, "Conflict: File already exists");
            return;
        }

        try
        {
            var contentLength = 0;

            // Читаем заголовки, чтобы получить Content-Length
            string line;
            while (!string.IsNullOrEmpty(line = reader.ReadLine()))
            {
                if (line.StartsWith("Content-Length:", StringComparison.OrdinalIgnoreCase))
                {
                    contentLength = int.Parse(line.Split(":")[1].Trim());
                }
            }

            if (contentLength == 0)
            {
                WriteResponse(writer, HttpStatusCode.BadRequest, "Missing Content-Length");
                return;
            }

            using var fs = new FileStream(targetPath, FileMode.Create, FileAccess.Write);
            var buffer = new char[1024];
            int totalRead = 0;

            while (totalRead < contentLength)
            {
                int bytesToRead = Math.Min(buffer.Length, contentLength - totalRead);
                int bytesRead = reader.Read(buffer, 0, bytesToRead);

                if (bytesRead == 0) break; // Конец данных
                var data = Encoding.UTF8.GetBytes(buffer, 0, bytesRead);
                fs.Write(data, 0, data.Length);
                totalRead += bytesRead;
            }

            Log("POST: File saved at {0}", targetPath);
            WriteResponse(writer, HttpStatusCode.Created, "File successfully uploaded");
        }
        catch (Exception ex)
        {
            Log("POST Error: {0}", ex.Message);
            WriteResponse(writer, HttpStatusCode.InternalServerError, "Failed to save file");
        }
    }


    private void HandleOptionsRequest(StreamWriter writer)
    {
        writer.WriteLine("HTTP/1.1 204 No Content");
        writer.WriteLine("Allow: GET, POST, OPTIONS");

        foreach (var header in _config.Headers)
        {
            writer.WriteLine(header);
        }

        writer.WriteLine();
    }

    private string GetContentType(string filePath)
    {
        return filePath.EndsWith(".html") ? "text/html"
             : filePath.EndsWith(".css") ? "text/css"
             : filePath.EndsWith(".js") ? "application/javascript"
             : filePath.EndsWith(".json") ? "application/json"
             : filePath.EndsWith(".png") ? "image/png"
             : filePath.EndsWith(".jpg") || filePath.EndsWith(".jpeg") ? "image/jpeg"
             : "application/octet-stream";
    }

    private void WriteResponse(StreamWriter writer, HttpStatusCode statusCode, string message)
    {
        writer.WriteLine($"HTTP/1.1 {(int)statusCode} {message}");
        writer.WriteLine("Content-Type: text/plain");
        writer.WriteLine();
        writer.WriteLine(message);
    }

    private void Log(string format, params object[] args)
    {
        var logMessage = string.Format(format, args);
        Console.WriteLine(logMessage);
        File.AppendAllText(_config.LogFile, logMessage + Environment.NewLine);
    }
}

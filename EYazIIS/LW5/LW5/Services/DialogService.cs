using LW5.Models;
using LW5.ViewModels.Messages;
using System.Net.Http;
using System;
using System.Threading.Tasks;
using System.Net.Http.Json;
using System.Diagnostics;
using System.Text.Json;
using System.Text;

namespace LW5.Services
{
    public class DialogService
    {
        private Guid? _sessionId;
        private HttpClient? _client;

        private string _baseUrl;
        public string BaseUrl
        {
            get => _baseUrl;
            set
            {
                _baseUrl = value;
                try
                {
                    _client = new HttpClient()
                    {
                        BaseAddress = new(value)
                    };
                }
                catch {
                    _client = null;
                }
            }
        }

        public async Task<Message?> Send(UserMessageViewModel msg)
        {
            if (_client == null)
            {
                msg.Status = MessageStatus.Error;
                msg.ErrorMsg = "HTTP Client is null. Check server URL.";

                return null;
            }

            _sessionId ??= Guid.NewGuid();

            try
            {
                var chatRequest = new ChatRequest(
                    _sessionId?.ToString(),
                    msg.ToModel()
                    );

                var json = JsonSerializer.Serialize(chatRequest);
                Debug.WriteLine($"Sending msg: {json}");
                var content = new StringContent(json, Encoding.UTF8, "application/json");

                var response = await _client.PostAsync($"/chat", content);
                var body = await response.Content.ReadAsStringAsync();

                response.EnsureSuccessStatusCode();

                msg.Status = MessageStatus.Delivered;

                var chatResponse = await response.Content.ReadFromJsonAsync<ChatResponse>();

                return chatResponse!.message;
            }
            catch (Exception ex)
            {
                Debug.WriteLine($"Error sending message to chat: {ex}");
                msg.Status = MessageStatus.Error;
                msg.ErrorMsg = ex.Message;

                return null;
            }
        }
    }
}

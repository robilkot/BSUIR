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

        public async Task<Message?> Send(UserMessageViewModel msg)
        {
            _sessionId ??= Guid.NewGuid();

            var httpClient = new HttpClient()
            {
                BaseAddress = new("http://localhost:8000/")
            };

            try
            {
                var chatRequest = new ChatRequest(
                    _sessionId?.ToString(),
                    msg.ToModel()
                    );

                var json = JsonSerializer.Serialize(chatRequest);
                Debug.WriteLine($"Sending msg: {json}");
                var content = new StringContent(json, Encoding.UTF8, "application/json");

                var response = await httpClient.PostAsync($"/chat", content);
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

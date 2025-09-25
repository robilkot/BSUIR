using System;
using System.IO;
using System.Net.Http;
using System.Threading.Tasks;
using NAudio.Wave;
using System.Collections.Generic;

namespace frontend.Services;

public class AudioRecognitionService
{
    private readonly string _apiEndpoint = "http://localhost:8000/speech-to-text";
    private readonly HttpClient _httpClient;

    private const float SilenceThreshold = 0.02f; // Порог тишины (0.02 = 2% от максимальной амплитуды)
    private const int SilenceDurationMs = 2000;   // Длительность тишины для остановки записи (2 секунды)
    private const int SampleRate = 16000;         // Частота дискретизации
    private const int Channels = 1;               // Моно аудио

    public AudioRecognitionService()
    {
        _httpClient = new HttpClient();
    }

    public async Task<string> RecordUntilSilenceAndRecognizeAsync()
    {
        byte[] audioData = await RecordAudioUntilSilenceAsync();

        if (audioData == null || audioData.Length == 0)
        {
            throw new Exception("Не удалось записать аудио");
        }

        var response = await SendAudioToServerAsync(audioData);

        return response.Replace("\"", string.Empty);
    }

    private async Task<byte[]> RecordAudioUntilSilenceAsync()
    {
        using var memoryStream = new MemoryStream();

        var waveFormat = new WaveFormat(SampleRate, Channels);

        using var waveIn = new WaveInEvent
        {
            WaveFormat = waveFormat,
            BufferMilliseconds = 100
        };

        var silenceCounter = 0;
        var isRecording = true;
        var recordedData = new List<byte>();

        waveIn.DataAvailable += (sender, e) =>
        {
            if (!isRecording) return;

            // Проверяем уровень звука на тишину
            bool isSilent = IsSilent(e.Buffer, e.BytesRecorded);

            if (isSilent)
            {
                silenceCounter += e.BytesRecorded / (waveFormat.BlockAlign * waveFormat.SampleRate / 1000);

                // Если тишина продолжается дольше заданного времени - останавливаем запись
                if (silenceCounter >= SilenceDurationMs)
                {
                    isRecording = false;
                    return;
                }
            }
            else
            {
                silenceCounter = 0; // Сбрасываем счетчик тишины при наличии звука
            }

            recordedData.AddRange(new ArraySegment<byte>(e.Buffer, 0, e.BytesRecorded));
        };

        waveIn.RecordingStopped += (sender, e) =>
        {
            isRecording = false;
        };

        waveIn.StartRecording();

        var timeout = TimeSpan.FromSeconds(5);
        var startTime = DateTime.Now;

        while (isRecording && (DateTime.Now - startTime) < timeout)
        {
            await Task.Delay(100);
        }

        waveIn.StopRecording();

        if (recordedData.Count < waveFormat.AverageBytesPerSecond) // Меньше 1 секунды
        {
            return null;
        }

        return CreateWavFile(recordedData.ToArray(), waveFormat);
    }

    private bool IsSilent(byte[] buffer, int bytesRecorded)
    {
        // Конвертируем байты в float samples для анализа амплитуды
        float maxAmplitude = 0f;
        int sampleCount = bytesRecorded / 2; // 16-bit = 2 bytes per sample

        for (int i = 0; i < sampleCount; i++)
        {
            short sample = (short)(buffer[i * 2] | (buffer[i * 2 + 1] << 8));
            float amplitude = Math.Abs(sample / 32768f); // Нормализуем к диапазону [0, 1]

            if (amplitude > maxAmplitude)
            {
                maxAmplitude = amplitude;
            }
        }

        return maxAmplitude < SilenceThreshold;
    }

    private byte[] CreateWavFile(byte[] audioData, WaveFormat waveFormat)
    {
        using var memoryStream = new MemoryStream();

        // Записываем WAV заголовок
        using var writer = new WaveFileWriter(memoryStream, waveFormat);
        writer.Write(audioData, 0, audioData.Length);
        writer.Flush();

        return memoryStream.ToArray();
    }

    private async Task<string> SendAudioToServerAsync(byte[] audioData)
    {
        using var form = new MultipartFormDataContent();
        using var audioContent = new ByteArrayContent(audioData);

        audioContent.Headers.ContentType = new System.Net.Http.Headers.MediaTypeHeaderValue("audio/wav");
        form.Add(audioContent, "file", "recording.wav");

        try
        {
            var response = await _httpClient.PostAsync(_apiEndpoint, form);
            response.EnsureSuccessStatusCode();

            return await response.Content.ReadAsStringAsync();
        }
        catch (HttpRequestException ex)
        {
            throw new Exception($"Ошибка при отправке аудио на сервер: {ex.Message}");
        }
    }
}

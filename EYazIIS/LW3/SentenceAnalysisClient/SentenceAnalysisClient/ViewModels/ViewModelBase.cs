using ReactiveUI;
using System.Net.Http;
using System;

namespace SentenceAnalysisClient.ViewModels;

public class ViewModelBase : ReactiveObject
{
    protected static readonly HttpClient _httpClient = new()
    {
        BaseAddress = new Uri("http://localhost:8000/")
    };
}

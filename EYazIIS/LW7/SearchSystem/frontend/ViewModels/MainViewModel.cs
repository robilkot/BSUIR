using CommonLib.Models;
using frontend.Services;
using ReactiveUI;
using System;
using System.Collections.ObjectModel;
using System.Diagnostics;
using System.Globalization;
using System.Linq;
using System.Speech.Recognition;
using System.Threading.Tasks;
using System.Windows.Input;

namespace frontend.ViewModels;


public class MainViewModel : ViewModelBase
{
    private readonly ApiService _apiService;
    private string _searchQuery = string.Empty;
    private DateTime? _startDate;
    private DateTime? _endDate;
    private bool _isLoading;
    private int _currentPage = 1;
    private const int PageSize = 10;
    private bool _hasNextPage = true;
    private SpeechRecognitionEngine _speechRecognizer;

    public MainViewModel()
    {
        var x = SpeechRecognitionEngine.InstalledRecognizers();
        foreach (RecognizerInfo ri in x)
        {
            System.Diagnostics.Debug.WriteLine(ri.Culture.Name);
        }

        _apiService = new ApiService();
        SearchResults = [
            new(Guid.NewGuid(), new("D:/indexingTest/1.txt"), "Test title1.txt", "Some snippet to descirbre askfsjdf sdfnjbkhkoh qgyqwph d;fx;xdl;s", DateTimeOffset.Now, 0.9d),
            new(Guid.NewGuid(), new("D:/indexingTest/1.txt"), "Test title1.txt", "Some snippet to descirbre askfsjdf sdfnjbkhkoh qgyqwph d;fx;xdl;s", DateTimeOffset.Now, 0.9d),
            new(Guid.NewGuid(), new("D:/indexingTest/1.txt"), "Test title1.txt", "Some snippet to descirbre askfsjdf sdfnjbkhkoh qgyqwph d;fx;xdl;s", DateTimeOffset.Now, 0.9d),
            new(Guid.NewGuid(), new("D:/indexingTest/1.txt"), "Test title1.txt", "Some snippet to descirbre askfsjdf sdfnjbkhkoh qgyqwph d;fx;xdl;s", DateTimeOffset.Now, 0.9d),
            new(Guid.NewGuid(), new("D:/indexingTest/1.txt"), "Test title1.txt", "Some snippet to descirbre askfsjdf sdfnjbkhkoh qgyqwph d;fx;xdl;s", DateTimeOffset.Now, 0.9d),
            new(Guid.NewGuid(), new("D:/indexingTest/1.txt"), "Test title1.txt", "Some snippet to descirbre askfsjdf sdfnjbkhkoh qgyqwph d;fx;xdl;s", DateTimeOffset.Now, 0.9d),
            new(Guid.NewGuid(), new("D:/indexingTest/1.txt"), "Test title1.txt", "Some snippet to descirbre askfsjdf sdfnjbkhkoh qgyqwph d;fx;xdl;s", DateTimeOffset.Now, 0.9d),
            new(Guid.NewGuid(), new("D:/indexingTest/1.txt"), "Test title1.txt", "Some snippet to descirbre askfsjdf sdfnjbkhkoh qgyqwph d;fx;xdl;s", DateTimeOffset.Now, 0.9d),
            ];

        SearchCommand = ReactiveCommand.CreateFromTask(PerformSearch);
        NextPageCommand = ReactiveCommand.CreateFromTask(NextPage);
        VoiceInputCommand = ReactiveCommand.CreateFromTask(VoiceInput);

        InitializeSpeechRecognition();
    }

    private void InitializeSpeechRecognition()
    {
        try
        {
            // Check if speech recognition is available
            var recognizers = SpeechRecognitionEngine.InstalledRecognizers();
            var russianRecognizer = recognizers.FirstOrDefault(r => r.Culture.TwoLetterISOLanguageName == "ru");

            if (russianRecognizer == null)
            {
                Debug.WriteLine("Russian speech recognition not available. Using default recognizer.");
                _speechRecognizer = new SpeechRecognitionEngine();
            }
            else
            {
                _speechRecognizer = new SpeechRecognitionEngine(russianRecognizer);
            }

            // Create grammar for date patterns
            //var grammarBuilder = new GrammarBuilder();
            //grammarBuilder.Culture = new CultureInfo("ru-RU");

            // Allow any speech input
            _speechRecognizer.LoadGrammar(new DictationGrammar());

            _speechRecognizer.SpeechRecognized += SpeechRecognized;
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Speech recognition initialization error: {ex.Message}");
            throw ex;
        }
    }

    private void SpeechRecognized(object sender, SpeechRecognizedEventArgs e)
    {
        if (e.Result != null && e.Result.Confidence > 0.5)
        {
            var recognizedText = e.Result.Text;
            ProcessVoiceInput(recognizedText);
        }
        else
        {
            // todo show error
        }
    }

    private void ProcessVoiceInput(string input)
    {
        try
        {
            // Pattern: "[query] от [start date] до [end date]"
            var pattern = @"(.*?)(?:\s+от\s+(\d{1,2}(?:\.\d{1,2}(?:\.\d{2,4})?)?)\s+до\s+(\d{1,2}(?:\.\d{1,2}(?:\.\d{2,4})?)?))?$";

            // Try to match the pattern
            var match = System.Text.RegularExpressions.Regex.Match(input, pattern,
                System.Text.RegularExpressions.RegexOptions.IgnoreCase);

            if (match.Success)
            {
                var searchQuery = match.Groups[1].Value.Trim();
                var startDateStr = match.Groups[2].Value;
                var endDateStr = match.Groups[3].Value;

                // Update search query
                SearchQuery = searchQuery;

                // Parse dates if they exist
                if (!string.IsNullOrEmpty(startDateStr) && !string.IsNullOrEmpty(endDateStr))
                {
                    if (TryParseRussianDate(startDateStr, out var startDate))
                    {
                        StartDate = startDate;
                    }

                    if (TryParseRussianDate(endDateStr, out var endDate))
                    {
                        EndDate = endDate;
                    }
                }
                else
                {
                    // Clear dates if no date range was specified
                    StartDate = null;
                    EndDate = null;
                }

                // Auto-trigger search after voice input
                _ = PerformSearch();
            }
            else
            {
                // No date pattern found, use entire input as search query
                SearchQuery = input;
                StartDate = null;
                EndDate = null;

                // Auto-trigger search
                _ = PerformSearch();
            }
        }
        catch (Exception ex)
        {
            Debug.WriteLine($"Voice input processing error: {ex.Message}");
            SearchQuery = input; // Fallback to using raw input
        }
    }

    public string SearchQuery
    {
        get => _searchQuery;
        set => this.RaiseAndSetIfChanged(ref _searchQuery, value);
    }

    public DateTime? StartDate
    {
        get => _startDate;
        set => this.RaiseAndSetIfChanged(ref _startDate, value);
    }

    public DateTime? EndDate
    {
        get => _endDate;
        set => this.RaiseAndSetIfChanged(ref _endDate, value);
    }

    public bool IsLoading
    {
        get => _isLoading;
        set => this.RaiseAndSetIfChanged(ref _isLoading, value);
    }

    public int CurrentPage
    {
        get => _currentPage;
        set => this.RaiseAndSetIfChanged(ref _currentPage, value);
    }

    public bool HasNextPage
    {
        get => _hasNextPage;
        set => this.RaiseAndSetIfChanged(ref _hasNextPage, value);
    }

    public bool HasResults => SearchResults.Count > 0;
    public bool HasNoResults => !IsLoading && SearchResults.Count == 0 && !string.IsNullOrEmpty(SearchQuery);

    public ObservableCollection<SearchResult> SearchResults { get; }

    public ICommand VoiceInputCommand { get; }
    public ICommand SearchCommand { get; }
    public ICommand NextPageCommand { get; }

    private bool TryParseRussianDate(string dateString, out DateTime result)
    {
        // Try common Russian date formats
        var formats = new[]
        {
            "d.M.yyyy", "d.M.yy", "dd.MM.yyyy", "dd.MM.yy",
            "d/M/yyyy", "d/M/yy", "dd/MM/yyyy", "dd/MM/yy",
            "d M yyyy", "d M yy", "dd MM yyyy", "dd MM yy"
        };

        foreach (var format in formats)
        {
            if (DateTime.TryParseExact(dateString, format,
                CultureInfo.GetCultureInfo("ru-RU"),
                DateTimeStyles.None, out result))
            {
                return true;
            }
        }

        // Try natural language parsing for common phrases
        var now = DateTime.Now;
        dateString = dateString.ToLower();

        switch (dateString)
        {
            case "сегодня":
                result = now.Date;
                return true;
            case "вчера":
                result = now.AddDays(-1).Date;
                return true;
            case "завтра":
                result = now.AddDays(1).Date;
                return true;
            case "неделю назад":
                result = now.AddDays(-7).Date;
                return true;
            case "месяц назад":
                result = now.AddMonths(-1).Date;
                return true;
            case "год назад":
                result = now.AddYears(-1).Date;
                return true;
        }

        result = DateTime.MinValue;
        return false;
    }

    private async Task VoiceInput()
    {
        try
        {
            if (_speechRecognizer != null)
            {
                // Set input to microphone
                _speechRecognizer.SetInputToDefaultAudioDevice();

                // Start asynchronous recognition
                _speechRecognizer.RecognizeAsync(RecognizeMode.Single);

                // You might want to show some UI indication that listening is in progress
                Console.WriteLine("Listening for voice input...");
            }
            else
            {
                Console.WriteLine("Speech recognition not available");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Voice input error: {ex.Message}");
        }

        await Task.CompletedTask;
    }

    private async Task PerformSearch()
    {
        CurrentPage = 1;
        await SearchAsync();
    }

    private async Task NextPage()
    {
        if (HasNextPage)
        {
            CurrentPage++;
            await SearchAsync();
        }
    }

    private async Task SearchAsync()
    {
        if (string.IsNullOrWhiteSpace(SearchQuery))
        {
            SearchResults.Clear();
            return;
        }

        IsLoading = true;

        try
        {
            var request = new SearchQuery(
                Text: SearchQuery,
                StartDate: StartDate,
                EndDate: EndDate,
                Page: CurrentPage,
                PageSize: PageSize
                );

            var results = await _apiService.SearchAsync(request);

            SearchResults.Clear();
            foreach (var result in results)
            {
                SearchResults.Add(result);
            }

            // Simple heuristic: if we got fewer results than page size, probably no more pages
            HasNextPage = SearchResults.Count >= PageSize;
        }
        catch (Exception ex)
        {
            // In a real app, you'd show this to the user
            Console.WriteLine($"Search error: {ex.Message}");
        }
        finally
        {
            IsLoading = false;
        }
    }
}
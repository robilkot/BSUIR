using CommonLib.Models;
using DynamicData;
using frontend.Services;
using ReactiveUI;
using System;
using System.Collections.ObjectModel;
using System.Reactive;
using System.Threading.Tasks;

namespace frontend.ViewModels;


public class MainViewModel : ViewModelBase
{
    private readonly ApiService _apiService;
    private const int PageSize = 10;
    private bool _hasNextPage = true;

    public MainViewModel()
    {
        _apiService = new ApiService();

        var canSearch = this.WhenAnyValue(x => x.SearchQuery, (query) => !string.IsNullOrEmpty(query));
        SearchCommand = ReactiveCommand.CreateFromTask(PerformSearch, canSearch);

        NextPageCommand = ReactiveCommand.CreateFromTask(NextPage);

        var canClearSearch = this.WhenAnyValue(x => x.SearchQuery, (query) => !string.IsNullOrEmpty(query));
        ClearSearchCommand = ReactiveCommand.Create(() =>
        {
            SearchQuery = string.Empty;
        }, canClearSearch);

        SearchResults = [
            new(Guid.NewGuid(), new("D:/indexingTest/test.txt"), "Test document.txt", DateTimeOffset.Now, ["keyword1", "keyword2", "keyword3", "keyword1", "keyword2", "keyword3", "keyword1", "keyword2", "keyword3", "keyword1", "keyword2", "keyword3", "keyword1", "keyword2", "keyword3"])
            ];
    }

    private string? _errMsg = null;
    public string? ErrorMessage
    {
        get => _errMsg;
        set => this.RaiseAndSetIfChanged(ref _errMsg, value);
    }

    private string _searchQuery = string.Empty;
    public string SearchQuery
    {
        get => _searchQuery;
        set => this.RaiseAndSetIfChanged(ref _searchQuery, value);
    }

    private DateTime? _startDate;
    public DateTime? StartDate
    {
        get => _startDate;
        set => this.RaiseAndSetIfChanged(ref _startDate, value);
    }

    private DateTime? _endDate;
    public DateTime? EndDate
    {
        get => _endDate;
        set => this.RaiseAndSetIfChanged(ref _endDate, value);
    }

    private bool _isLoading;
    public bool IsLoading
    {
        get => _isLoading;
        set => this.RaiseAndSetIfChanged(ref _isLoading, value);
    }

    private int _currentPage = 1;
    public int CurrentPage
    {
        get => _currentPage;
        set => this.RaiseAndSetIfChanged(ref _currentPage, value);
    }

    private ObservableCollection<SearchResult>? _searchResults = null;
    public ObservableCollection<SearchResult>? SearchResults
    {
        get => _searchResults;
        set => this.RaiseAndSetIfChanged(ref _searchResults, value);
    }

    public ReactiveCommand<Unit, Unit> SearchCommand { get; }
    public ReactiveCommand<Unit, Unit> ClearSearchCommand { get; }
    public ReactiveCommand<Unit, Unit> NextPageCommand { get; }

    private async Task PerformSearch()
    {
        CurrentPage = 1;
        await SearchAsync();
    }

    private async Task NextPage()
    {
        if (_hasNextPage)
        {
            CurrentPage++;
            await SearchAsync();
        }
    }

    private async Task SearchAsync()
    {
        if (string.IsNullOrEmpty(SearchQuery))
        {
            return;
        }

        IsLoading = true;
        ErrorMessage = null;

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

            // Simple heuristic: if we got fewer results than page size, probably no more pages
            _hasNextPage = results.Count == PageSize;
            
            if (CurrentPage == 1)
            {
                SearchResults = [];
            }

            SearchResults ??= [];
            SearchResults.AddRange(results);

            this.RaisePropertyChanged(nameof(SearchResults));
        }
        catch (Exception ex)
        {
            ErrorMessage = ex.Message;
        }
        finally
        {
            IsLoading = false;
        }
    }
}
using CommonLib.Models;
using frontend.Services;
using ReactiveUI;
using System;
using System.Collections.ObjectModel;
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

    public MainViewModel()
    {
        _apiService = new ApiService();
        SearchResults = [
            //new(Guid.NewGuid(), "Test title1.txt", "Some snippet to descirbre askfsjdf sdfnjbkhkoh qgyqwph d;fx;xdl;s", DateTimeOffset.Now, 0.9d),
            //new(Guid.NewGuid(), "Test title1.txt", "Some snippet to descirbre askfsjdf sdfnjbkhkoh qgyqwph d;fx;xdl;s", DateTimeOffset.Now, 0.9d),
            //new(Guid.NewGuid(), "Test title1.txt", "Some snippet to descirbre askfsjdf sdfnjbkhkoh qgyqwph d;fx;xdl;s", DateTimeOffset.Now, 0.9d),
            //new(Guid.NewGuid(), "Test title1.txt", "Some snippet to descirbre askfsjdf sdfnjbkhkoh qgyqwph d;fx;xdl;s", DateTimeOffset.Now, 0.9d),
            //new(Guid.NewGuid(), "Test title1.txt", "Some snippet to descirbre askfsjdf sdfnjbkhkoh qgyqwph d;fx;xdl;s", DateTimeOffset.Now, 0.9d),
            //new(Guid.NewGuid(), "Test title1.txt", "Some snippet to descirbre askfsjdf sdfnjbkhkoh qgyqwph d;fx;xdl;s", DateTimeOffset.Now, 0.9d),
            //new(Guid.NewGuid(), "Test title1.txt", "Some snippet to descirbre askfsjdf sdfnjbkhkoh qgyqwph d;fx;xdl;s", DateTimeOffset.Now, 0.9d),
            //new(Guid.NewGuid(), "Test title1.txt", "Some snippet to descirbre askfsjdf sdfnjbkhkoh qgyqwph d;fx;xdl;s", DateTimeOffset.Now, 0.9d),
            ];

        SearchCommand = ReactiveCommand.CreateFromTask(PerformSearch);
        NextPageCommand = ReactiveCommand.CreateFromTask(NextPage);
        PreviousPageCommand = ReactiveCommand.CreateFromTask(PreviousPage);
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

    public bool HasPreviousPage => CurrentPage > 1;
    public bool HasResults => SearchResults.Count > 0;
    public bool HasNoResults => !IsLoading && SearchResults.Count == 0 && !string.IsNullOrEmpty(SearchQuery);

    public ObservableCollection<SearchResult> SearchResults { get; }

    public ICommand SearchCommand { get; }
    public ICommand NextPageCommand { get; }
    public ICommand PreviousPageCommand { get; }

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

    private async Task PreviousPage()
    {
        if (CurrentPage > 1)
        {
            CurrentPage--;
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
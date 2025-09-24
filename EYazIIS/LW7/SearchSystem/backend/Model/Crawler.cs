using backend.DatetimeProviders;
using backend.Repository;
using backend.Services;
using CommonLib.Models;
using System.Collections.Concurrent;
using System.Collections.Immutable;

namespace backend.Model
{
    public enum FileEventType
    {
        Created,
        Changed,
        Deleted,
        Renamed,
    }
    public record FileEvent(FileEventType Type, string[] Args);

    public class Crawler : BackgroundService
    {
        private static readonly DatetimeProvider s_datetimeProvider = new();
        private readonly Uri _rootIndexingUri;
        private readonly IServiceScopeFactory _scopeFactory;
        private readonly ILogger<Crawler> _logger;

        private FileSystemWatcher? _watcher;

        private readonly ConcurrentQueue<FileEvent> _eventsQueue = new();

        private static readonly ImmutableHashSet<string> AllowedExtensions = ImmutableHashSet.Create(
            StringComparer.OrdinalIgnoreCase,
            ".txt", ".md"
        );

        public Crawler(IConfiguration configuration, IServiceScopeFactory scopeFactory, ILogger<Crawler> logger)
        {
            _logger = logger;
            _scopeFactory = scopeFactory;

            var uriString = configuration
                .GetRequiredSection(ConfigurationKeys.Search)
                .GetValue<string>(ConfigurationKeys.RootIndexingUri)
                ?? throw new Exception("No indexing URI set");

            _rootIndexingUri = new(uriString);
        }

        public async Task IndexAll(IServiceScopeFactory serviceScopeFactory, CancellationToken cancellationToken = default)
        {
            var allFiles = Directory.EnumerateFiles(_rootIndexingUri.LocalPath, "*.*", SearchOption.AllDirectories);

            var filteredFiles = allFiles
                .Where(file => AllowedExtensions.Contains(Path.GetExtension(file)))
                .Select(file => new Uri(file));

            List<Task> indexingTasks = [];

            foreach (var fileUri in filteredFiles)
            {
                await AddToIndexAsync(fileUri, serviceScopeFactory, cancellationToken);

                //await AddToIndexAsync(fileUri, serviceScopeFactory, cancellationToken);
                //indexingTasks.Add(task);
            }

            //await Task.WhenAll(indexingTasks);
        }

        private async Task AddToIndexAsync(Uri path, IServiceScopeFactory serviceScopeFactory, CancellationToken cancellationToken = default)
        {
            var scope = serviceScopeFactory.CreateAsyncScope();
            var indexRepository = scope.ServiceProvider.GetRequiredService<IndexRepository>();
            var nlpService = scope.ServiceProvider.GetRequiredService<NLPService>();

            var documentId = path.ToGuid();

            if (await indexRepository.GetByIdAsync(documentId, cancellationToken) is not null)
            {
                return;
            }

            _logger.LogInformation("Indexing {}", path);

            var document = await path.ToDocumentAsync(s_datetimeProvider, nlpService, cancellationToken) 
                ?? throw new Exception("Could not create document. Possibly, problem with NLP service");

            // Update lexeme frequencies
            foreach (KeywordMetadata keyword in document.Metadata.Keywords)
            {
                var lexeme = await indexRepository.GetByTextAsync(keyword.Text, cancellationToken);

                if(lexeme is null)
                {
                    var newLexeme = new LexemeMetadata() { Text = keyword.Text, ContainingDocuments = 1 };    
                    await indexRepository.AddAsync(newLexeme, cancellationToken);
                }
                else
                {
                    lexeme.ContainingDocuments += 1;
                    await indexRepository.UpdateAsync(lexeme, cancellationToken);
                }
            }

            await indexRepository.AddAsync(document, cancellationToken);
        }

        private async Task DeleteFromIndexAsync(Uri path, IServiceScopeFactory serviceScopeFactory, CancellationToken cancellationToken = default)
        {
            var scope = serviceScopeFactory.CreateAsyncScope();
            var indexRepository = scope.ServiceProvider.GetRequiredService<IndexRepository>();

            var documentId = path.ToGuid();
            var document = await indexRepository.GetByIdAsync(documentId, cancellationToken);

            if (document is null)
            {
                return;
            } 
            else
            {
                await indexRepository.DeleteAsync(documentId, cancellationToken);
            }

            // Update lexeme frequencies
            foreach (KeywordMetadata keyword in document.Metadata.Keywords)
            {
                var lexeme = await indexRepository.GetByTextAsync(keyword.Text, cancellationToken);

                if (lexeme is null)
                {
                    await indexRepository.AddAsync(new LexemeMetadata() { Text = keyword.Text, ContainingDocuments = 0 }, cancellationToken);
                }
                else
                {
                    lexeme.ContainingDocuments -= 1;

                    if (lexeme.ContainingDocuments <= 0)
                    {
                        await indexRepository.DeleteAsync(lexeme, cancellationToken);
                    }
                    else
                    {
                        await indexRepository.UpdateAsync(lexeme, cancellationToken);
                    }
                }
            }
        }

        private async Task UpdateInIndexAsync(Uri path, IServiceScopeFactory serviceScopeFactory, CancellationToken cancellationToken = default)
        {
            await DeleteFromIndexAsync(path, serviceScopeFactory, cancellationToken);
            await AddToIndexAsync(path, serviceScopeFactory, cancellationToken);
        }

        private async Task RenameInIndexAsync(Uri oldPath, Uri newPath, IServiceScopeFactory serviceScopeFactory, CancellationToken cancellationToken = default)
        {
            await DeleteFromIndexAsync(oldPath, serviceScopeFactory, cancellationToken);
            await AddToIndexAsync(newPath, serviceScopeFactory, cancellationToken);
        }

        private void CreateFileWatcher(string path)
        {
            _watcher = new()
            {
                Path = path,
                IncludeSubdirectories = true,
                NotifyFilter = NotifyFilters.LastAccess | NotifyFilters.LastWrite | NotifyFilters.FileName | NotifyFilters.DirectoryName,
                Filter = "*.*"
            };

            _watcher.Changed += new FileSystemEventHandler(OnChanged);
            _watcher.Created += new FileSystemEventHandler(OnChanged);
            _watcher.Deleted += new FileSystemEventHandler(OnChanged);
            _watcher.Renamed += new RenamedEventHandler(OnRenamed);

            _watcher.EnableRaisingEvents = true;
        }

        private void OnChanged(object source, FileSystemEventArgs e)
        {
            var extension = Path.GetExtension(e.FullPath);
            if (!AllowedExtensions.Contains(extension, StringComparer.OrdinalIgnoreCase))
                return;

            var type = e.ChangeType switch
            {
                WatcherChangeTypes.Changed => FileEventType.Changed,
                WatcherChangeTypes.Deleted => FileEventType.Deleted,
                WatcherChangeTypes.Created => FileEventType.Created,
                _ => FileEventType.Changed // todo not good
            };

            _eventsQueue.Enqueue(new(type, [e.FullPath]));
        }

        private void OnRenamed(object source, RenamedEventArgs e)
        {
            var oldExtension = Path.GetExtension(e.OldFullPath);
            var newExtension = Path.GetExtension(e.FullPath);

            if (!AllowedExtensions.Contains(oldExtension, StringComparer.OrdinalIgnoreCase) &&
                !AllowedExtensions.Contains(newExtension, StringComparer.OrdinalIgnoreCase))
                return;

            _eventsQueue.Enqueue(new(FileEventType.Renamed, [e.OldFullPath, e.FullPath]));
        }

        private async Task HandleEvents()
        {
            while (_eventsQueue.TryDequeue(out var e))
            {
                _logger.LogInformation("{} {}", e.Type, string.Join(", ", e.Args));

                try
                {
                    switch (e.Type)
                    {
                        case FileEventType.Created:
                            await AddToIndexAsync(new(e.Args[0]), _scopeFactory); break;
                        case FileEventType.Deleted:
                            await DeleteFromIndexAsync(new(e.Args[0]), _scopeFactory); break;
                        case FileEventType.Changed:
                            await UpdateInIndexAsync(new(e.Args[0]), _scopeFactory); break;
                        case FileEventType.Renamed:
                            await RenameInIndexAsync(new(e.Args[0]), new(e.Args[1]), _scopeFactory); break;
                    }
                }
                catch
                {
                    _logger.LogError("{} {}", e.Type, e.Args[0]);
                }
            }
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            CreateFileWatcher(_rootIndexingUri.LocalPath);

            if (!Directory.Exists(_rootIndexingUri.LocalPath))
            {
                throw new DirectoryNotFoundException($"Directory not found: {_rootIndexingUri.LocalPath}");
            }

            _logger.LogInformation("Crawler started");

            await IndexAll(_scopeFactory, stoppingToken);
            
            using var timer = new PeriodicTimer(TimeSpan.FromSeconds(1));

            while (!stoppingToken.IsCancellationRequested && await timer.WaitForNextTickAsync(stoppingToken))
            {
                await HandleEvents();
            }

            _logger.LogInformation("Crawler stopped.");
        }
    }
}

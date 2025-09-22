using backend.DatetimeProviders;
using backend.Repository;
using backend.Services;
using CommonLib.Models;
using System.Collections.Concurrent;
using System.Collections.Immutable;
using System.IO;
using System.Security.Cryptography;

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

    public class Crawler : IHostedService, IDisposable
    {
        private readonly Uri _rootIndexingUri;
        private readonly IServiceScopeFactory _scopeFactory;
        private readonly ILogger<Crawler> _logger;

        private readonly ConcurrentQueue<FileEvent> _eventsQueue = new();

        private Timer? _timer = null;

        private static readonly ImmutableHashSet<string> AllowedExtensions = ImmutableHashSet.Create(
            StringComparer.OrdinalIgnoreCase,
            ".txt", ".html", ".htm", ".json", ".md"
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

            CreateFileWatcher(_rootIndexingUri.LocalPath);
        }

        public async Task IndexAll(
            IndexRepository _indexRepository,
            NLPService _nlpService,
            IDatetimeProvider _datetimeProvider,
            CancellationToken cancellationToken = default)
        {
            var allFiles = Directory.EnumerateFiles(_rootIndexingUri.LocalPath, "*.*", SearchOption.AllDirectories);

            var filteredFiles = allFiles
                .Where(file => AllowedExtensions.Contains(Path.GetExtension(file)))
                .Select(file => new Uri(file));

            // todo task whenAll
            foreach (var fileUri in filteredFiles)
            {
                if (cancellationToken.IsCancellationRequested)
                {
                    break;
                }

                await AddToIndexAsync(fileUri, _indexRepository, _nlpService, _datetimeProvider, cancellationToken);                
            }
        }

        private async Task AddToIndexAsync(Uri path, 
            IndexRepository _indexRepository, 
            NLPService _nlpService, 
            IDatetimeProvider _datetimeProvider,
            CancellationToken cancellationToken = default)
        {
            var documentId = path.ToGuid();

            if (await _indexRepository.GetByIdAsync(documentId, cancellationToken) is not null)
            {
                return;
            }

            var document = await path.ToDocumentAsync(_datetimeProvider, _nlpService, cancellationToken);

            // Update lexeme frequencies
            foreach(KeywordMetadata keyword in document.Metadata.Keywords)
            {
                var lexeme = await _indexRepository.GetByTextAsync(keyword.Text, cancellationToken);

                if(lexeme is null)
                {
                    await _indexRepository.AddAsync(new LexemeMetadata() { Text = keyword.Text, ContainingDocuments = 1 }, cancellationToken);
                }
                else
                {
                    lexeme.ContainingDocuments += 1;
                    await _indexRepository.UpdateAsync(lexeme, cancellationToken);
                }
            }

            await _indexRepository.AddAsync(document, cancellationToken);
        }

        private async Task DeleteFromIndexAsync(Uri path, IndexRepository _indexRepository, CancellationToken cancellationToken = default)
        {
            var documentId = path.ToGuid();
            var document = await _indexRepository.GetByIdAsync(documentId, cancellationToken);

            if (document is null)
            {
                return;
            } 
            else
            {
                await _indexRepository.DeleteAsync(documentId, cancellationToken);
            }

            // Update lexeme frequencies
            foreach (KeywordMetadata keyword in document.Metadata.Keywords)
            {
                var lexeme = await _indexRepository.GetByTextAsync(keyword.Text, cancellationToken);

                if (lexeme is null)
                {
                    await _indexRepository.AddAsync(new LexemeMetadata() { Text = keyword.Text, ContainingDocuments = 0 }, cancellationToken);
                }
                else
                {
                    lexeme.ContainingDocuments -= 1;

                    if (lexeme.ContainingDocuments <= 0)
                    {
                        await _indexRepository.DeleteAsync(lexeme, cancellationToken);
                    }
                    else
                    {
                        await _indexRepository.UpdateAsync(lexeme, cancellationToken);
                    }
                }
            }
        }

        private async Task UpdateInIndexAsync(Uri path, 
            IndexRepository _indexRepository, 
            IDatetimeProvider _datetimeProvider, 
            NLPService _nlpService, 
            CancellationToken cancellationToken = default)
        {
            await DeleteFromIndexAsync(path, _indexRepository, cancellationToken);
            await AddToIndexAsync(path, _indexRepository, _nlpService, _datetimeProvider, cancellationToken);
        }

        private async Task RenameInIndexAsync(Uri oldPath, Uri newPath,
            IndexRepository _indexRepository,
            NLPService _nlpService,
            IDatetimeProvider _datetimeProvider,
            CancellationToken cancellationToken = default)
        {
            await DeleteFromIndexAsync(oldPath, _indexRepository, cancellationToken);
            await AddToIndexAsync(newPath, _indexRepository, _nlpService, _datetimeProvider, cancellationToken);
        }

        private void CreateFileWatcher(string path)
        {
            FileSystemWatcher watcher = new()
            {
                Path = path,
                IncludeSubdirectories = true,
                NotifyFilter = NotifyFilters.LastAccess | NotifyFilters.LastWrite | NotifyFilters.FileName | NotifyFilters.DirectoryName,
                Filter = "*.*"
            };

            watcher.Changed += new FileSystemEventHandler(OnChanged);
            watcher.Created += new FileSystemEventHandler(OnChanged);
            watcher.Deleted += new FileSystemEventHandler(OnChanged);
            watcher.Renamed += new RenamedEventHandler(OnRenamed);

            watcher.EnableRaisingEvents = true;
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

        private async void HandleEvents()
        {
            _timer?.Change(Timeout.Infinite, 0);

            using var scope = _scopeFactory.CreateAsyncScope();
            var nlpService = scope.ServiceProvider.GetRequiredService<NLPService>();
            var dateTimeProvider = scope.ServiceProvider.GetRequiredService<IDatetimeProvider>();
            var indexRepository = scope.ServiceProvider.GetRequiredService<IndexRepository>();

            while (_eventsQueue.TryDequeue(out var e))
            {
                _logger.LogInformation($"{e.Type} {string.Join(", ", e.Args)}");
                try
                {
                    switch (e.Type)
                    {
                        case FileEventType.Created:
                            await AddToIndexAsync(new(e.Args[0]), indexRepository, nlpService, dateTimeProvider); break;
                        case FileEventType.Deleted:
                            await DeleteFromIndexAsync(new(e.Args[0]), indexRepository); break;
                        case FileEventType.Changed:
                            await UpdateInIndexAsync(new(e.Args[0]), indexRepository, dateTimeProvider, nlpService); break;
                        case FileEventType.Renamed:
                            await RenameInIndexAsync(new(e.Args[0]), new(e.Args[1]), indexRepository, nlpService, dateTimeProvider); break;
                    }
                }
                catch (Exception ex)
                {
                    _logger.LogError(ex.Message);
                }
            }

            _timer?.Change(TimeSpan.FromSeconds(3), TimeSpan.Zero);
        }

        public async Task StartAsync(CancellationToken cancellationToken)
        {
            if (!Directory.Exists(_rootIndexingUri.LocalPath))
            {
                throw new DirectoryNotFoundException($"Directory not found: {_rootIndexingUri.LocalPath}");
            }

            _logger.LogInformation("Crawler started");

            _timer = new Timer(new TimerCallback((state) => HandleEvents()), null, TimeSpan.Zero, TimeSpan.FromSeconds(3));

            using var scope = _scopeFactory.CreateAsyncScope();
            var nlpService = scope.ServiceProvider.GetRequiredService<NLPService>();
            var dateTimeProvider = scope.ServiceProvider.GetRequiredService<IDatetimeProvider>();
            var indexRepository = scope.ServiceProvider.GetRequiredService<IndexRepository>();

            await IndexAll(indexRepository, nlpService, dateTimeProvider, cancellationToken);
        }

        public Task StopAsync(CancellationToken cancellationToken)
        {
            _timer?.Change(Timeout.Infinite, 0);

            _logger.LogInformation("Crawler stopped");

            return Task.CompletedTask;
        }

        public void Dispose()
        {
            _timer?.Dispose();
        }
    }
}

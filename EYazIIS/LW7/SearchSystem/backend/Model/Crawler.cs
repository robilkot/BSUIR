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

    public class Crawler : IHostedService, IDisposable
    {
        private readonly Uri _rootIndexingUri;
        private readonly IServiceScopeFactory _scopeFactory;
        private readonly ILogger<Crawler> _logger;

        private Timer? _timer = null;

        private ConcurrentQueue<FileEvent> _eventsQueue = new();

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
            if (!Directory.Exists(_rootIndexingUri.LocalPath))
            {
                throw new DirectoryNotFoundException($"Directory not found: {_rootIndexingUri.LocalPath}");
            }

            var allFiles = Directory.EnumerateFiles(
                _rootIndexingUri.LocalPath,
                "*.*",
                SearchOption.AllDirectories
            );

            var filteredFiles = allFiles
                .Where(file => AllowedExtensions.Contains(Path.GetExtension(file)))
                .Select(file => new Uri(file));

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

            await _indexRepository.AddAsync(document, cancellationToken);
        }

        private async Task DeleteFromIndexAsync(Uri path, IndexRepository _indexRepository, CancellationToken cancellationToken = default)
            => await _indexRepository.DeleteAsync(path.ToGuid(), cancellationToken);

        private async Task UpdateInIndexAsync(Uri path, 
            IndexRepository _indexRepository, 
            IDatetimeProvider _datetimeProvider, 
            NLPService _nlpService, 
            CancellationToken cancellationToken = default)
        {
            var id = path.ToGuid();
            var doc = await _indexRepository.GetByIdAsync(id, cancellationToken);

            if (doc is null)
            {
                await AddToIndexAsync(path, _indexRepository, _nlpService, _datetimeProvider, cancellationToken);
            }
            else
            {
                var newDocument = await path.ToDocumentAsync(_datetimeProvider, _nlpService, cancellationToken);

                doc.IndexedAt = newDocument.IndexedAt;
                doc.Metadata = newDocument.Metadata;

                await _indexRepository.UpdateAsync(doc, cancellationToken);
            }
        }

        private async Task RenameInIndexAsync(Uri oldPath, Uri newPath, 
            IndexRepository _indexRepository,
            NLPService _nlpService,
            IDatetimeProvider _datetimeProvider,
            CancellationToken cancellationToken = default)
        {
            var oldId = oldPath.ToGuid();

            var document = await _indexRepository.GetByIdAsync(oldId, cancellationToken);

            if (document is null)
            {
                await AddToIndexAsync(newPath, _indexRepository, _nlpService, _datetimeProvider, cancellationToken);
            } 
            else
            {
                document = new Document()
                {
                    Id = newPath.ToGuid(),
                    Uri = newPath,
                    Metadata = document.Metadata,
                    IndexedAt = _datetimeProvider.Now,
                };

                await _indexRepository.DeleteAsync(oldId, cancellationToken);

                await _indexRepository.AddAsync(document, cancellationToken);
            }
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
                _ => throw new ArgumentException("why")
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
                Console.WriteLine($"{e.Type} {string.Join(", ", e.Args)}");
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
            _logger.LogInformation("Crawler started indexing");

            _timer = new Timer(new TimerCallback((state) => HandleEvents()), null, TimeSpan.Zero, TimeSpan.FromSeconds(3));

            using var scope = _scopeFactory.CreateAsyncScope();
            var nlpService = scope.ServiceProvider.GetRequiredService<NLPService>();
            var dateTimeProvider = scope.ServiceProvider.GetRequiredService<IDatetimeProvider>();
            var indexRepository = scope.ServiceProvider.GetRequiredService<IndexRepository>();

            await IndexAll(indexRepository, nlpService, dateTimeProvider, cancellationToken);
        }

        public Task StopAsync(CancellationToken cancellationToken)
        {
            _logger.LogInformation("Crawler stopped indexing");

            _timer?.Change(Timeout.Infinite, 0);

            return Task.CompletedTask;
        }

        public void Dispose()
        {
            _timer?.Dispose();
        }
    }
}

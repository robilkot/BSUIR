using backend.DatetimeProviders;
using backend.Repository;
using CommonLib.Models;
using System.Collections.Immutable;

namespace backend.Model
{
    public class Crawler
    {
        private readonly Uri _rootIndexingUri;
        private readonly IIndexRepository _indexRepository;
        private readonly IDatetimeProvider _datetimeProvider;

        private static readonly ImmutableHashSet<string> AllowedExtensions = ImmutableHashSet.Create(
            StringComparer.OrdinalIgnoreCase,
            ".txt", ".html", ".htm", ".json", ".md"
        );

        public Crawler(IConfiguration configuration, IIndexRepository repository, IDatetimeProvider datetimeProvider)
        {
            _datetimeProvider = datetimeProvider;
            _indexRepository = repository;

            var uriString = configuration
                .GetRequiredSection(ConfigurationKeys.Search)
                .GetValue<string>(ConfigurationKeys.RootIndexingUri)
                ?? throw new Exception("No indexing URI set");

            _rootIndexingUri = new(uriString);

            CreateFileWatcher(_rootIndexingUri.LocalPath);
        }

        public async Task IndexAll(CancellationToken cancellationToken = default)
        {
            if (!Directory.Exists(_rootIndexingUri.LocalPath))
            {
                throw new DirectoryNotFoundException($"Directory not found: {_rootIndexingUri.LocalPath}");
            }

            var allFiles = Directory.EnumerateFiles(
                _rootIndexingUri.LocalPath,
                "*.*", // todo why
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

                await AddToIndexAsync(fileUri, cancellationToken);                
            }
        }

        private async Task AddToIndexAsync(Uri path, CancellationToken cancellationToken = default)
        {
            var documentId = path.ToGuid();

            if (await _indexRepository.GetByIdAsync(documentId, cancellationToken) is not null)
            {
                return;
            }

            var document = await path.ToDocumentAsync(_datetimeProvider, cancellationToken);

            await _indexRepository.AddAsync(document, cancellationToken);
        }

        private async Task DeleteFromIndexAsync(Uri path, CancellationToken cancellationToken = default)
            => await _indexRepository.DeleteAsync(path.ToGuid(), cancellationToken);

        private async Task UpdateInIndexAsync(Uri path, CancellationToken cancellationToken = default)
        {
            var id = path.ToGuid();
            var doc = await _indexRepository.GetByIdAsync(id) ?? throw new InvalidOperationException("why?");

            var newDocument = await path.ToDocumentAsync(_datetimeProvider, cancellationToken);
            doc.IndexedAt = newDocument.IndexedAt;
            doc.Metadata = newDocument.Metadata;

            await _indexRepository.UpdateAsync(doc, cancellationToken);
        }

        private async Task RenameInIndexAsync(Uri oldPath, Uri newPath, CancellationToken cancellationToken = default)
        {
            var oldId = oldPath.ToGuid();

            var document = await _indexRepository.GetByIdAsync(oldId, cancellationToken)
                ?? throw new InvalidOperationException("Why?");

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

        private async void OnChanged(object source, FileSystemEventArgs e)
        {
            var extension = Path.GetExtension(e.FullPath);
            if (!AllowedExtensions.Contains(extension, StringComparer.OrdinalIgnoreCase))
                return;

            try
            {
                switch (e.ChangeType)
                {
                    case WatcherChangeTypes.Created:
                        await AddToIndexAsync(new(e.FullPath)); break;
                    case WatcherChangeTypes.Deleted:
                        await DeleteFromIndexAsync(new(e.FullPath)); break;
                    case WatcherChangeTypes.Changed:
                        await UpdateInIndexAsync(new(e.FullPath)); break;
                    case WatcherChangeTypes.Renamed:
                        break;
                    case WatcherChangeTypes.All:
                        throw new NotImplementedException("WatcherChangeTypes.All");
                }
            }
            catch (Exception ex)
            {
                // todo
                throw;
            }
        }

        private async void OnRenamed(object source, RenamedEventArgs e)
        {
            var oldExtension = Path.GetExtension(e.OldFullPath);
            var newExtension = Path.GetExtension(e.FullPath);

            if (!AllowedExtensions.Contains(oldExtension, StringComparer.OrdinalIgnoreCase) &&
                !AllowedExtensions.Contains(newExtension, StringComparer.OrdinalIgnoreCase))
                return;

            try
            {
                await RenameInIndexAsync(new(e.OldFullPath), new(e.FullPath));
            }
            catch (Exception ex)
            {
                // todo
                throw;
            }
        }
    }
}

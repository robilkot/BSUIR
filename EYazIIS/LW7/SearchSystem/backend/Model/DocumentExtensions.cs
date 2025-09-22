using CommonLib.Models;
using System.Security.Cryptography;
using System.Text;

namespace backend.Model
{
    public static class DocumentExtensions
    {
        public static Guid ToGuid(this Uri input)
        {
            byte[] inputBytes = Encoding.UTF8.GetBytes(input.AbsoluteUri);
            byte[] hashBytes = MD5.HashData(inputBytes);
            return new Guid(hashBytes);
        }

        public static string ToTitle(this Document doc)
            => Path.GetFileName(doc.Uri.LocalPath);

        public async static Task<string?> ToSnippetAsync(this Document doc, CancellationToken cancellationToken = default)
        {
            try
            {
                var allText = await File.ReadAllTextAsync(doc.Uri.LocalPath, cancellationToken);

                return allText.Substring(0, Math.Min(allText.Length, 100));
            }
            catch
            {
                return null;
            }

        }
    }
}

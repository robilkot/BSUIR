using System.Runtime.InteropServices;

namespace LW3;

public class SecureStringWrapper : IDisposable
{
    private byte[] _encryptedData;
    private GCHandle _handle;
    private bool _disposed = false;

    public SecureStringWrapper(byte[] encryptedData)
    {
        _encryptedData = encryptedData;

        _handle = GCHandle.Alloc(_encryptedData, GCHandleType.Pinned);
    }

    public byte[] GetData()
    {
        return _disposed ? throw new ObjectDisposedException("SecureStringWrapper") : _encryptedData;
    }

    public void UpdateData(byte[] newData)
    {
        if (_disposed)
        {
            throw new ObjectDisposedException("SecureStringWrapper");
        }

        Array.Clear(_encryptedData, 0, _encryptedData.Length);

        if (_handle.IsAllocated)
            _handle.Free();

        _encryptedData = newData;
        _handle = GCHandle.Alloc(_encryptedData, GCHandleType.Pinned);
    }

    public void Dispose()
    {
        Dispose(true);
        GC.SuppressFinalize(this);
    }

    protected virtual void Dispose(bool disposing)
    {
        if (!_disposed)
        {
            if (disposing)
            {
                if (_encryptedData != null)
                {
                    Array.Clear(_encryptedData, 0, _encryptedData.Length);
                    _encryptedData = null;
                }
            }

            if (_handle.IsAllocated)
                _handle.Free();

            _disposed = true;
        }
    }

    ~SecureStringWrapper()
    {
        Dispose(false);
    }
}

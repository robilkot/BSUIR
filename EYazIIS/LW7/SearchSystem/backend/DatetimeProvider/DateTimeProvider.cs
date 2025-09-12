namespace backend.DatetimeProviders
{
    public interface IDatetimeProvider
    {
        public DateTimeOffset Now { get; }
    }

    public class DatetimeProvider : IDatetimeProvider
    {
        public DateTimeOffset Now => DateTimeOffset.Now;
    }
}

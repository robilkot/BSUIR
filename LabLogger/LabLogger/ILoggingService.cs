namespace LabLogger
{
    public interface ILoggingService
    {
        public void Log(object message, Logger.Levels level = Logger.Levels.Info);
    }
}

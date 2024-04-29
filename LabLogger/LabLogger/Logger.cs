namespace LabLogger
{
    public static class Logger
    {
        public static Levels Level = 0;
        [Flags]
        public enum Levels
        {
            Error = 1,
            Warning = 2,
            Info = 4,
            Debug = 8
        }
        private static HashSet<ILoggingService> s_loggingService = [];
        public static void Log(string message, Levels level = Levels.Info)
        {
            foreach (var service in s_loggingService)
            {
                service.Log(message, level);
            }
        }

        public static void UseConsoleLogger()
        {
            s_loggingService.Add(new ConsoleLogger());
        }
    }
}

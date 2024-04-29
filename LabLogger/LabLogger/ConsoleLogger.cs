using LabLogger;
using System.Diagnostics;
using System.Diagnostics.CodeAnalysis;

namespace LabLogger
{
    [ExcludeFromCodeCoverage]
    internal class ConsoleLogger : ILoggingService
    {
        public static Dictionary<Logger.Levels, ConsoleColor> LevelsColors = new()
        {
            { Logger.Levels.Debug, ConsoleColor.DarkGreen },
            { Logger.Levels.Info, ConsoleColor.DarkCyan },
            { Logger.Levels.Warning, ConsoleColor.DarkYellow },
            { Logger.Levels.Error, ConsoleColor.DarkRed },
        };
        public ConsoleLogger()
        {
            Console.ForegroundColor = ConsoleColor.White;
        }
        public void Log(object message, Logger.Levels level = Logger.Levels.Info)
        {
            if (Logger.Level.HasFlag(level))
            {
                if (LevelsColors.TryGetValue(level, out ConsoleColor color))
                {
                    Console.ForegroundColor = color;
                } else
                {
                    Console.ForegroundColor = ConsoleColor.White;
                }

                var className = new StackTrace().GetFrame(2)?.GetMethod()?.ReflectedType!.Name;

                Console.Write($"[{level}] ");
                Console.ForegroundColor = ConsoleColor.DarkGray;
                Console.Write($"[{className}] ");
                Console.ForegroundColor = ConsoleColor.White;
                Console.WriteLine($"{message}");
            }
        }
    }
}

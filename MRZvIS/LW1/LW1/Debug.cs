namespace LW1
{
    public static class Debug
    {
        public static bool Enabled = false;

        public static void Log(object? obj = null)
        {
            if(Enabled)
            {
                Console.WriteLine(obj?.ToString());
            }
        }
        public static void Log(params object[] args)
        {
            foreach(object arg in args)
            {
                Log(arg);
            }
        }
        public static void Clear()
        {
            if(Enabled)
            {
                Console.Clear();
            }
        }
    }
}

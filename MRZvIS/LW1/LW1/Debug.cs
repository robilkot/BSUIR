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
        public static void Clear()
        {
            Console.Clear();
        }
    }
}

using BenchmarkDotNet.Running;

namespace LW3;

class Program
{
    static void Main(string[] args)
    {
        //SecureDataManager.WriteToConsole = false;
        //BenchmarkSwitcher.FromAssembly(typeof(Program).Assembly).Run(args);
        //return;

        SecureDataManager.WriteToConsole = true;
        var manager = new SecureDataManager();

        Console.WriteLine("Secure Memory Management Application");
        Console.WriteLine("====================================");

        while (true)
        {
            Console.WriteLine("\nOptions:");
            Console.WriteLine("1. Add non-confidential data");
            Console.WriteLine("2. Add confidential data");
            Console.WriteLine("3. Update confidential data");
            Console.WriteLine("31.Update non-confidential data");
            Console.WriteLine("4. Delete confidential data");
            Console.WriteLine("41.Delete non-confidential data");
            Console.WriteLine("5. View non-confidential data");
            Console.WriteLine("6. View confidential data summary");
            Console.WriteLine("7. Get confidential data (decrypt)");
            Console.WriteLine("8. Exit");
            Console.Write("Choose option: ");

            var choice = Console.ReadLine();

            try
            {
                switch (choice)
                {
                    case "1":
                        Console.Write("Enter non-confidential data: ");
                        var nonConfData = Console.ReadLine();
                        manager.AddNonConfidentialData(nonConfData);
                        break;

                    case "2":
                        Console.Write("Enter confidential data: ");
                        var confData = Console.ReadLine();
                        manager.AddConfidentialData(confData);
                        break;

                    case "3":
                        Console.Write("Enter index: ");
                        var updateIndex = int.Parse(Console.ReadLine());
                        Console.Write("Enter new confidential data: ");
                        var newData = Console.ReadLine();
                        manager.UpdateConfidentialData(updateIndex, newData);
                        break;

                    case "31":
                        Console.Write("Enter index: ");
                        var updateIndex2 = int.Parse(Console.ReadLine());
                        Console.Write("Enter new non-confidential data: ");
                        var newData2 = Console.ReadLine();
                        manager.UpdateNonConfidentialData(updateIndex2, newData2);
                        break;

                    case "4":
                        Console.Write("Enter index to delete: ");
                        var deleteIndex = int.Parse(Console.ReadLine());
                        manager.DeleteConfidentialData(deleteIndex);
                        break;

                    case "41":
                        Console.Write("Enter index to delete: ");
                        var deleteIndex2 = int.Parse(Console.ReadLine());
                        manager.DeleteNonConfidentialData(deleteIndex2);
                        break;

                    case "5":
                        manager.DisplayNonConfidentialData();
                        break;

                    case "6":
                        manager.DisplayConfidentialDataSummary();
                        break;

                    case "7":
                        Console.Write("Enter index to view: ");
                        var viewIndex = int.Parse(Console.ReadLine());
                        var decrypted = manager.GetConfidentialData(viewIndex);
                        Console.WriteLine($"Decrypted data: {decrypted}");
                        break;

                    case "8":
                        Console.WriteLine("Exiting...");
                        return;

                    default:
                        Console.WriteLine("Invalid option");
                        break;
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }

            Console.WriteLine("\nPress any key to continue...");
            Console.ReadKey();
            Console.Clear();
        }
    }
}
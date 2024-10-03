using static LW4.MathHelper;

namespace LW4
{
    public static class SecretGenerator
    {
        public static int Generate(int prime)
        {
            var P = prime; // Given prime number
            var g = P.ToPrimitiveElement(); // Find primitive element from P

            var a = new Random((int)DateTime.Now.Ticks).Next(); // Alice secret number
            var b = new Random((int)DateTime.Now.Ticks).Next(); // Bob secret number

            var A = PowerByModule(g, a, P); // Alice open number
            var B = PowerByModule(g, b, P); // Bobs open number

            var KAlice = PowerByModule(B, a, P); // Calculate common secret for both
            var KBob = PowerByModule(A, b, P);

            Console.WriteLine($"P: {P}");
            Console.WriteLine($"g: {g}\n");
            Console.WriteLine($"a: {a}");
            Console.WriteLine($"b: {b}\n");
            Console.WriteLine($"A: {A}");
            Console.WriteLine($"B: {B}\n");
            Console.WriteLine($"K (Alice): {KAlice}");
            Console.WriteLine($"K (Bob): {KBob}\n");

            return KAlice;
        }   
    }
}

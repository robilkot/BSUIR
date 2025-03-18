namespace LW1
{
    public static class Arithmetics
    {
        public static Pipeline.PipelineStageFunction PipelineStageFunction = (MultiplicationTriple triple) =>
        {
            /*printf("input triple (index %zu):\n", triple->index);
            triple->print();*/

            if ((triple.Factor & 1) == 1)
            {
                triple.PartialSum += triple.Multiplicand;
            }

            triple.Multiplicand <<= 1;
            triple.Factor >>= 1;

            //printf("output triple:\n");
            //triple->print();
        };

        public static List<Number> MultiplyPairs(List<(Number A, Number B)> pairs)
        {
            Pipeline pipeline = new();

            var sourceBitDepth = pairs.First().A.BitDepth;
            var resultBitDepth = sourceBitDepth * 2;

            int index = 0;
            foreach (var pair in pairs)
            {
                pipeline.Input.Enqueue(new()
                {
                    Index = index++,
                    Multiplicand = pair.A with { BitDepth = resultBitDepth },
                    Factor = pair.B with { BitDepth = resultBitDepth },
                    PartialSum = new Number(0, resultBitDepth)
                });
            }

            for (var i = 0; i < sourceBitDepth; i++)
            {
                pipeline.AddStage(PipelineStageFunction);
            }

            for (var i = 0; i < sourceBitDepth + pairs.Count; i++)
            {
                Console.Clear();

                pipeline.Tick();

                Console.ReadKey();
            }

            var output = pipeline.Output.Select(triple => new Number(triple.PartialSum, resultBitDepth)).ToList();

            Console.WriteLine($" Количество тактов: {pipeline.CurrentTick - 1}\n");

            return output;
        }
    }
}

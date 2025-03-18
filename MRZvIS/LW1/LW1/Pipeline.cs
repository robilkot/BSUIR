namespace LW1
{
    public class Pipeline
    {
        public delegate void PipelineStageFunction(MultiplicationTriple triple);
        private class PipelineStage(int index, PipelineStageFunction func)
        {
            public int Index { get; init; } = index;
            public PipelineStageFunction Function { get; init; } = func;
            public MultiplicationTriple? Data;

            public void Execute()
            {
                if (Data is not null)
                {
                    Function.Invoke(Data);
                }
            }
        }

        private readonly List<PipelineStage> Stages = [];

        public Queue<MultiplicationTriple> Input { get; private set; } = [];
        public Queue<MultiplicationTriple> Output { get; private set; } = [];
        public int CurrentTick { get; private set; }

        public void AddStage(PipelineStageFunction func)
        {
            Stages.Add(new PipelineStage(Stages.Count, func));
        }

        public void Tick()
        {
            Console.WriteLine($"\nТАКТ {CurrentTick}\n\n");

            Console.WriteLine("Входная очередь:\n");
            foreach (var triple in Input)
            {
                Console.WriteLine($"{triple.Multiplicand}, {triple.Factor}\n");
            }
            Console.WriteLine();

            foreach (var stage in Stages)
            {
                Console.WriteLine($"Этап {stage.Index}\n");
                stage.Execute();
                Console.WriteLine();
            }

            var lastData = Stages.Last().Data;
            if (lastData is not null)
            {
                Output.Enqueue(lastData);
            }

            for (int i = Stages.Count - 1; i > 0; i--)
            {
                Stages[i].Data = Stages[i - 1].Data;
            }

            Stages.First().Data = Input.Count > 0 ? Input.Dequeue() : null;

            Console.WriteLine("Выход:\n");
            foreach (var triple in Output)
            {
                Console.WriteLine($"{triple.PartialSum}\n");
            }
            Console.WriteLine();

            CurrentTick++;
        }
    };
}
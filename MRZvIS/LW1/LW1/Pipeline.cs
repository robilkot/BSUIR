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

        public bool Tick()
        {
            if(Stages.Count == 0)
            {
                CurrentTick++;
                return false;
            }

            Debug.Log($"\nТАКТ {CurrentTick++}\nВходная очередь:");
            foreach (var triple in Input)
            {
                Debug.Log($"{(uint)triple.Multiplicand}\t({triple.Multiplicand}), {(uint)triple.Factor}\t({triple.Factor})");
            }
            Debug.Log();

            foreach (var stage in Stages)
            {
                Debug.Log($"Этап {stage.Index}");
                stage.Execute();
                Debug.Log();
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

            Debug.Log("Выход:");
            foreach (var triple in Output)
            {
                Debug.Log($"{(uint)triple.PartialSum}\t({triple.PartialSum})");
            }
            Debug.Log();

            var nonEmptyStagesCount = Stages.Count(stage => stage.Data is not null);
            return nonEmptyStagesCount > 0 || CurrentTick == 1;
        }
    };
}
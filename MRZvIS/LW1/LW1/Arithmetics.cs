// Лабораторная работа №1 по дисциплине МРЗвИС
// Вариант 1: алгоритм вычисления произведения пары 4-разрядных чисел умножением с младших разрядов со сдвигом множимого (частичного произведения) влево
// Выполнил студент группы 221701 БГУИР Робилко Тимур Маркович
//
// Файл, содержащий операции над числами с использованием конвейера согласно варианту
//
// Источники:
// - Формальные модели обработки информации и параллельные модели решения задач : учеб.-метод. пособие / В. П. Ивашенко. – Минск : БГУИР, 2020


namespace LW1
{
    public static class Arithmetics
    {
        public static Pipeline.PipelineStageFunction PipelineStageFunction => (MultiplicationTriple triple) =>
        {
            //Debug.Log($"Вход (тройка с индексом {triple.Index}):", triple);

            if ((triple.Factor & 1) == 1)
            {
                triple.PartialSum += triple.Multiplicand;
            }

            triple.Multiplicand <<= 1;
            triple.Factor >>= 1;

            Debug.Log("Выход:", triple);
        };

        public static (int tacts, List<Number> numbers) Multiply(this List<(Number A, Number B)> pairs)
        {
            if (pairs.Count == 0)
            {
                return (0, []);
            }

            Pipeline pipeline = new();

            var sourceBitDepth = pairs.First().A.BitDepth;
            var resultBitDepth = sourceBitDepth * 2;

            int index = 0;
            foreach (var (A, B) in pairs)
            {
                pipeline.Input.Enqueue(new()
                {
                    Index = index++,
                    Multiplicand = A with { BitDepth = resultBitDepth },
                    Factor = B with { BitDepth = resultBitDepth },
                    PartialSum = new Number(0, resultBitDepth)
                });
            }

            for (var i = 0; i < sourceBitDepth; i++)
            {
                pipeline.AddStage(PipelineStageFunction);
            }

            bool still_active = false;
            do
            {
                if (Debug.Enabled && still_active)
                {
                    if (Console.ReadKey().Key != ConsoleKey.Enter)
                    {
                        continue;
                    }
                }

                Debug.Clear();

                still_active = pipeline.Tick();

            } while (still_active);

            return (
                pipeline.CurrentTick - 1,
                pipeline.Output
                    .Select(triple => new Number(triple.PartialSum, resultBitDepth))
                    .ToList()
                    );
        }
    }
}

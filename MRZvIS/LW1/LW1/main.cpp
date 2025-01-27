// Лабораторная работа №1 по дисциплине МРЗвИС
// Вариант 1: алгоритм вычисления произведения пары 4-разрядных чисел умножением с младших разрядов со сдвигом множимого (частичного произведения) влево
// Выполнил студент группы 221701 БГУИР Робилко Тимур Маркович
//
// Главный файл программы
//
// Источники:
// - Формальные модели обработки информации и параллельные модели решения задач : учеб.-метод. пособие / В. П. Ивашенко. – Минск : БГУИР, 2020


#include <stdio.h>
#include <cstdint>
#include <malloc.h>

#include "Arithmetics.h"
#include "Pipeline.h"
#include "MultiplicationTriple.h"


void multiply_with_multiplicand_shift(PipelineData input)
{
    MultiplicationTriple* triple = (MultiplicationTriple*)input;

    printf("input triple (index %zu):\n", triple->index);
    triple->print();

    if (triple->factor & 1) {
        triple->partial_sum += triple->multiplicand;
    }

    triple->multiplicand <<= 1;
    triple->factor >>= 1;

    printf("output triple:\n");
    triple->print();
}

int main(int argc, char** argv)
{
    uint32_t m; // length
    uint32_t p; // depth

    m = 3;
    p = 4;

    //scanf_s("%u %u", &m, &p);

    std::vector<uint32_t> A;
    A.reserve(m);
    for (size_t i = 0; i < m; i++)
    {
        A.emplace_back(i);
    }

    std::vector<uint32_t> B;
    B.reserve(m);
    for (size_t i = 0; i < m; i++)
    {
        B.emplace_back(2 * i);
    }

    // init triples for multiplication
    std::vector<MultiplicationTriple> input;
    input.reserve(m);
    
    for(size_t i = 0; i < m; i++)
    {
        input.emplace_back(MultiplicationTriple{ A[i], B[i], 0, i});
    }

    // init pipe
    Pipeline pipe{};

    // init pipe steps (we need p shifts for p-digit numbers)
    std::vector<PipelineStep> steps;
    steps.reserve(p);

    for(size_t i = 0; i < p; i++)
    {
        steps.emplace_back(PipelineStep{i, NULL, multiply_with_multiplicand_shift});
    };

    pipe.steps = steps;
    
    // init input data struct for pipe referencing actual input data
    std::queue<PipelineData> pipe_input;
    
    for (size_t i = 0; i < m; i++)
    {
        pipe_input.emplace((PipelineData) &(input[i]));
    }

    pipe.input = pipe_input;
    
    // show input data
    printf("\nsource pairs:\n");
    for (int i = 0; i < m; i++) {
        printf("%d: {%d, %d}\n", i, A[i], B[i]);
    }
    printf("\n");

    // run model
    for (size_t i = 0; i < p + m - 1; i++) {
        pipe.tick();
    }

    // show output data
    printf("\nprocessed data:\n");
    for (size_t i = 0; !pipe.output.empty(); i++) {
        printf("%zu: %d\n", i, ((MultiplicationTriple*)pipe.output.front())->partial_sum);
        pipe.output.pop();
    }
    printf("\n\n");
}

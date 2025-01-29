// Лабораторная работа №1 по дисциплине МРЗвИС
// Вариант 1: алгоритм вычисления произведения пары 4-разрядных чисел умножением с младших разрядов со сдвигом множимого (частичного произведения) влево
// Выполнил студент группы 221701 БГУИР Робилко Тимур Маркович
//
// Файл, содержащий функции умножения согласно варианту работу
//
// Источники:
// - Формальные модели обработки информации и параллельные модели решения задач : учеб.-метод. пособие / В. П. Ивашенко. – Минск : БГУИР, 2020


#pragma once

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

std::vector<uint32_t> multiply_pairs(const std::vector<uint32_t>& A, const std::vector<uint32_t>& B, size_t bit_size = 4)
{
    // init triples for multiplication
    std::vector<MultiplicationTriple> input;
    std::vector<uint32_t> output;

    for (size_t i = 0; i < A.size(); i++)
    {
        input.push_back(MultiplicationTriple{ A[i], B[i], 0, i });
    }

    // init pipe
    Pipeline pipe{};

    // init pipe steps (we need p shifts for p-digit numbers)
    std::vector<PipelineStep> steps;
    steps.reserve(bit_size);

    for (size_t i = 0; i < bit_size; i++)
    {
        steps.emplace_back(PipelineStep{ i + 1, NULL, multiply_with_multiplicand_shift });
    };

    pipe.stages = steps;

    // init input data struct for pipe referencing actual input data
    std::queue<PipelineData> pipe_input;

    for (size_t i = 0; i < A.size(); i++)
    {
        pipe_input.emplace((PipelineData) & (input[i]));
    }

    pipe.input = pipe_input;

    // run model
    for (size_t i = 0; i < bit_size + A.size(); i++) {
        system("cls");
        pipe.tick();
        getchar();
    }

    for (size_t i = 0; !pipe.output.empty(); i++) {
        auto product = ((MultiplicationTriple*)pipe.output.front())->partial_sum;
        output.push_back(product);
        pipe.output.pop();
    }

    std::cout << "\ntotal tacts: " << pipe.current_tick - 1 << "\n";

    return output;
}
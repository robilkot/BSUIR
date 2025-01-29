// Лабораторная работа №1 по дисциплине МРЗвИС
// Вариант 1: алгоритм вычисления произведения пары 4-разрядных чисел умножением с младших разрядов со сдвигом множимого (частичного произведения) влево
// Выполнил студент группы 221701 БГУИР Робилко Тимур Маркович
//
// Файл, содержащий типы данных для представления конвейера
//
// Источники:
// - Формальные модели обработки информации и параллельные модели решения задач : учеб.-метод. пособие / В. П. Ивашенко. – Минск : БГУИР, 2020

#pragma once

#include <cstdint>
#include <stdio.h>
#include <vector>
#include <queue>
#include <functional>
#include "MultiplicationTriple.h"

typedef void* PipelineData;


class PipelineStep 
{
    public:
    size_t index;
    PipelineData data;
    std::function<void(PipelineData)> function;

    void execute() const
    {
        if (data != NULL)
        {
            function(data);
        }
    }
};

class Pipeline
{
    public:
    std::vector<PipelineStep> stages;
    std::queue<PipelineData> input;
    std::queue<PipelineData> output;

    size_t current_tick;

    void tick()
    {
        std::cout << "\nTACT " << current_tick << "\n\n";

        std::cout << "Input queue:\n";
        auto input_copy = input;
        while(!input_copy.empty())
        {
            auto ptr = input_copy.front();
            input_copy.pop();
            auto x = *((MultiplicationTriple*)ptr);
            
            std::cout << x.multiplicand << ", " <<  x.factor << "\n";
        }
        std::cout << "\n";

        // invoke pipeline steps
        for (auto& stage : stages)
        {
            std::cout << "Stage " << stage.index << "\n";
            stage.execute();
            std::cout << "\n";
        }
        // save output if ready
        if (stages.back().data != NULL)
        {
            output.push(stages.back().data);
        }

        // move output to next steps' input
        for (auto it = stages.end() - 1; it != stages.begin(); it--)
        {
            it->data = (it - 1)->data;
        }

        // move input data for first step
        if (input.empty())
        {
            stages[0].data = NULL; // if input queue is exhausted
        }
        else
        {
            stages[0].data = input.front();
            input.pop();
        }

        std::cout << "Output:\n";
        auto output_copy = output;
        while (!output_copy.empty())
        {
            auto ptr = output_copy.front();
            output_copy.pop();
            auto x = *((MultiplicationTriple*)ptr);

            std::cout << x.partial_sum << "\n";
        }
        std::cout << "\n";

        current_tick++;
    }
};

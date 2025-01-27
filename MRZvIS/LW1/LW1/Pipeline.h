// ������������ ������ �1 �� ���������� ������
// ������� 1: �������� ���������� ������������ ���� 4-��������� ����� ���������� � ������� �������� �� ������� ��������� (���������� ������������) �����
// �������� ������� ������ 221701 ����� ������� ����� ��������
//
// ����, ���������� ���� ������ ��� ������������� ���������
//
// ���������:
// - ���������� ������ ��������� ���������� � ������������ ������ ������� ����� : ����.-�����. ������� / �. �. ��������. � ����� : �����, 2020

#pragma once

#include <cstdint>
#include <stdio.h>
#include <vector>
#include <queue>
#include <functional>

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
    std::vector<PipelineStep> steps;
    std::queue<PipelineData> input;
    std::queue<PipelineData> output;

    size_t current_tick;

    void tick()
    {
        printf("\n# TICK %zu\n", current_tick);

        // move output to next steps' input
        for (auto it = steps.end() - 1; it != steps.begin(); it--)
        {
            it->data = (it - 1)->data;
        }

        // move input data for first step
        if (input.empty())
        {
            steps[0].data = NULL; // if input queue is exhausted
        }
        else
        {
            steps[0].data = input.front();
            input.pop();
        }

        size_t step_index = 0;
        // invoke pipeline steps
        for (auto& step : steps)
        {
            printf("## STEP %zu:\n", step_index++);
            step.execute();
        }
        // save output if ready
        if (steps.back().data != NULL)
        {
            output.push(steps.back().data);
        }

        current_tick++;
    }
};

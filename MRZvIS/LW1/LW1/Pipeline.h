#pragma once

#include <cstdint>
#include <stdio.h>


typedef void(*PipelineFunction_t)(void*);
typedef void(*PipelineData_t);

struct PipelineStepStruct {
    size_t index;
    PipelineData_t p_data;
    PipelineFunction_t p_function;

    void execute() const;
};

typedef PipelineStepStruct PipelineStep_t;


struct PipelineStruct {
    uint32_t current_tick;

    size_t steps_count;
    PipelineStep_t* p_steps;

    size_t input_count;
    PipelineData_t* p_input;

    void tick();
};

typedef PipelineStruct Pipeline_t;

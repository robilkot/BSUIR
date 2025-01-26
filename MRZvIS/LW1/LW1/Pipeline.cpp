#include "Pipeline.h"


void PipelineStepStruct::execute() const
{
	p_function(p_data);
}

void PipelineStruct::tick()
{
    static size_t s_steps_count = steps_count;
    static size_t s_current_input = 0;
    static size_t s_current_output = 0;

    printf("\n# TICK %u\n", current_tick);

    // move output to next steps' input
    for (size_t i = s_steps_count - 1; i > 0; i--) {
        p_steps[i].p_data = p_steps[i - 1].p_data;
    }

    // move input data for first step
    if (s_current_input < input_count) {
        p_steps[0].p_data = p_input[s_current_input];
        p_input[s_current_input] = NULL;
        s_current_input++;
    }
    else {
        p_steps[0].p_data = NULL; // if input array is exhausted
    }

    // invoke pipeline steps
    for (size_t i = 0; i < s_steps_count; i++) {
        printf("## STEP %d:\n", i);

        if (p_steps[i].p_data != NULL) {
            p_steps[i].execute();
        }
        else {
            printf("no input data\n");
        }
    }

    current_tick++;
}
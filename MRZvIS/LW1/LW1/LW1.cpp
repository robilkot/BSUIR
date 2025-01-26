#include <stdio.h>
#include <cstdint>
#include <malloc.h>

static void print_number(uint32_t number, uint32_t depth)
{
    for (int i = depth - 1; i >= 0; i--) {
        printf("%d", number >> i & 1);

        if (i && i % 4 == 0) {
            printf(" ");
        }
    }
    printf("\n");
}

typedef void* (*PipelineFunction_t)(void*);
typedef void (*PipelineData_t);

struct PipelineStepStruct {
    PipelineData_t p_data;
    PipelineFunction_t p_function;

    void execute()
    {
        p_data = p_function(p_data);
    }
};

typedef PipelineStepStruct PipelineStep_t;

struct PipelineStruct {
    uint32_t current_tick;

    size_t steps_count;
    PipelineStep_t* p_steps;

    size_t input_count;
    PipelineData_t* p_input;

    size_t output_count;
    PipelineData_t* p_output;

    void tick()
    {
        static size_t s_steps_count = steps_count;
        static size_t s_current_input = 0;
        static size_t s_current_output = 0;

        printf("tick %u\n", current_tick);

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
            if (p_steps[i].p_data != NULL) {
                p_steps[i].execute();
            }
        }

        // move output data from last step
        if (p_steps[s_steps_count - 1].p_data != NULL) {
            p_output[s_current_output] = p_steps[s_steps_count - 1].p_data;
            s_current_output++;
        }

        current_tick++;
    }
};

typedef PipelineStruct Pipeline_t;


void* pipe_func1(void* input)
{
    printf("test1 - %d\n", *(int*)input);
    return input;
}

void* pipe_func2(void* input)
{
    printf("test2 - %d\n", *(int*)input);
    return input;
}

void* pipe_func3(void* input)
{
    printf("test3 - %d\n", *(int*)input);
    return input;
}



int main()
{
    //uint32_t m; // length
    //uint32_t p; // depth

    //m = 20;
    //p = 4;

    //scanf_s("%u %u", &m, &p);

    //uint32_t* A = new uint32_t[m];
    //uint32_t* B = new uint32_t[m];
    //uint32_t* C = new uint32_t[m];

    //printf("%u, %u", m, p);

    //for (uint32_t i = 0; i < 16; i++)
    //{
    //    print_number(i, 4);
    //}

    Pipeline_t pipe{};

    PipelineStep_t steps[3]{};
    steps[0].p_function = pipe_func1;
    steps[1].p_function = pipe_func2;
    steps[2].p_function = pipe_func3;

    pipe.steps_count = 3;

    int input[3]{};
    input[0] = 11;
    input[1] = 22;
    input[2] = 33;

    int output[3]{};
    output[0] = 0;
    output[1] = 0;
    output[2] = 0;

    PipelineData_t pipe_input[3]{};
    pipe_input[0] = input + 0;
    pipe_input[1] = input + 1;
    pipe_input[2] = input + 2;

    PipelineData_t pipe_output[3]{};
    pipe_output[0] = output + 0;
    pipe_output[1] = output + 1;
    pipe_output[2] = output + 2;

    pipe.input_count = 3;
    pipe.output_count = 3;


    pipe.p_steps = steps;
    pipe.p_input = pipe_input;
    pipe.p_output = pipe_output;


    for (size_t i = 0; i < 10; i++) {
        pipe.tick();
    }
    
    //delete A;
    //delete B;
    //delete C;
}

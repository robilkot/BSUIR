#include <stdio.h>
#include <cstdint>
#include <malloc.h>

#include "Arithmetics.h"
#include "Pipeline.h"
#include "MultiplicationTriple.h"


void multiply_with_multiplicand_shift(void* input)
{
    MultiplicationTriple_t* triple = (MultiplicationTriple_t*)input;

    printf("input triple (index %d):\n", triple->index);
    triple->print();

    if (triple->factor & 1) {
        triple->partial_sum += triple->multiplicand;
    }

    triple->multiplicand <<= 1;
    triple->factor >>= 1;

    printf("output triple:\n");
    triple->print();
}


int main()
{
    uint32_t m; // length
    uint32_t p; // depth

    m = 3;
    p = 4;

    //scanf_s("%u %u", &m, &p);

    // init given vectors
    uint32_t* A = new uint32_t[m];
    for (size_t i = 0; i < m; i++)
    {
        A[i] = i + 1;
    }

    uint32_t* B = new uint32_t[m];
    for (size_t i = 0; i < m; i++)
    {
        B[i] = (i + 1) * 2;
    }

    // init triples for multiplication
    MultiplicationTriple_t* input = new MultiplicationTriple_t[m];

    for(size_t i = 0; i < m; i++)
    {
        input[i] = MultiplicationTriple_t{ A[i], B[i], 0, i};
    }

    // init pipe
    Pipeline_t pipe{};

    // init pipe steps (we need p shifts for p-digit numbers)
    PipelineStep_t* steps = new PipelineStep_t[p];

    for(size_t i = 0; i < p; i++)
    {
        steps[i] = PipelineStep_t{ i, NULL, multiply_with_multiplicand_shift };
    };

    pipe.p_steps = steps;
    pipe.steps_count = p;

    // init input data struct for pipe referencing actual input data
    PipelineData_t* pipe_input = new PipelineData_t[m];
    
    for (size_t i = 0; i < m; i++)
    {
        pipe_input[i] = input + i;
    };

    pipe.p_input = pipe_input;
    pipe.input_count = m;

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
    for (int i = 0; i < pipe.input_count; i++) {
        printf("%d ", input[i].partial_sum);
    }
    printf("\n\n");
    

#pragma warning (disable: 6278)
#pragma warning (disable: 6283)
    delete steps;
    delete input;
    delete pipe_input;
    delete A;
    delete B;
#pragma warning (restore: 6278)
#pragma warning (restore: 6283)
}

#include "Arithmetics.h"


void multiply_with_multiplicand_shift(void* input)
{
    MultiplicationTriple_t* triple = (MultiplicationTriple_t*)input;

    //printf("input triple (index %d):\n", triple->index);
    triple->print();

    if (triple->factor & 1) {
        triple->partial_sum += triple->multiplicand;
    }

    triple->multiplicand <<= 1;
    triple->factor >>= 1;

    printf("output data:\n");
    triple->print();
    printf("\n");
}

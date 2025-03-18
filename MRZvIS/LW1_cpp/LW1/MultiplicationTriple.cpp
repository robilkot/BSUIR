#include "MultiplicationTriple.h"

void MultiplicationTriple::print() const
{
    printf("mul: ");
    print_number(multiplicand, bit_depth);
    printf("\n");
    printf("fac: ");
    print_number(factor, bit_depth);
    printf("\n");
    printf("sum: ");
    print_number(partial_sum, bit_depth);
    printf("\n");
}
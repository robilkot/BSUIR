#include "MultiplicationTriple.h"


void MultiplicationTripleStruct::print() const
{
    printf("mul: ");
    print_number(multiplicand, 8);
    printf("\n");
    printf("fac: ");
    print_number(factor, 8);
    printf("\n");
    printf("sum: ");
    print_number(partial_sum, 8);
    printf("\n");
}
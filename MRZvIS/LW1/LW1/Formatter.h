#pragma once

#include <cstdint>
#include <stdio.h>

static void print_number(uint32_t number, uint32_t bit_depth)
{
    for (int i = bit_depth - 1; i >= 0; i--) {
        printf("%d", number >> i & 1);

        if (i && i % 4 == 0) {
            printf(" ");
        }
    }
}
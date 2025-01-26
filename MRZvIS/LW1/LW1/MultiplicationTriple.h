#pragma once

#include <cstdint>
#include <stdio.h>
#include "Formatter.h"


struct MultiplicationTripleStruct {
    uint32_t multiplicand;
    uint32_t factor;
    uint32_t partial_sum;
    size_t index;

    void print() const;
};

typedef MultiplicationTripleStruct MultiplicationTriple_t;
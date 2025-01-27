// Лабораторная работа №1 по дисциплине МРЗвИС
// Вариант 1: алгоритм вычисления произведения пары 4-разрядных чисел умножением с младших разрядов со сдвигом множимого (частичного произведения) влево
// Выполнил студент группы 221701 БГУИР Робилко Тимур Маркович
//
// Файл, содержащий тип данных для представления тройки { множимое, множитель, частичная сумма }
//
// Источники:
// - Формальные модели обработки информации и параллельные модели решения задач : учеб.-метод. пособие / В. П. Ивашенко. – Минск : БГУИР, 2020

#pragma once

#include <cstdint>
#include <stdio.h>
#include "Formatter.h"


struct MultiplicationTriple {
    uint32_t multiplicand;
    uint32_t factor;
    uint32_t partial_sum;
    size_t index;

    void print() const
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
};
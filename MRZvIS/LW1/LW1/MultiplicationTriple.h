// ������������ ������ �1 �� ���������� ������
// ������� 1: �������� ���������� ������������ ���� 4-��������� ����� ���������� � ������� �������� �� ������� ��������� (���������� ������������) �����
// �������� ������� ������ 221701 ����� ������� ����� ��������
//
// ����, ���������� ��� ������ ��� ������������� ������ { ��������, ���������, ��������� ����� }
//
// ���������:
// - ���������� ������ ��������� ���������� � ������������ ������ ������� ����� : ����.-�����. ������� / �. �. ��������. � ����� : �����, 2020

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
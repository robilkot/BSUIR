// ������������ ������ �1 �� ���������� ������
// ������� 1: �������� ���������� ������������ ���� 4-��������� ����� ���������� � ������� �������� �� ������� ��������� (���������� ������������) �����
// �������� ������� ������ 221701 ����� ������� ����� ��������
//
// ������� ���� ���������
//
// ���������:
// - ���������� ������ ��������� ���������� � ������������ ������ ������� ����� : ����.-�����. ������� / �. �. ��������. � ����� : �����, 2020


#include <cstdint>
#include <iostream>

#include "Arithmetics.h"
#include "InputReader.h"

constexpr int BitDepth = 4;


int main(int argc, char** argv)
{
    try {
        const auto& input = read_input("input.txt");
        const auto& A = input.first;
        const auto& B = input.second;

        // show input data
        std::cout << "\nsource pairs:\n";
        for (int i = 0; i < A.size(); i++) {
            std::cout << i << ": {" << A[i] << ", " << B[i] << "}\n";
        }
        std::cout << "\n";


        const auto& output = multiply_pairs(A, B);


        // show output data
        std::cout << "\nprocessed data:\n";
        for (size_t i = 0; i < output.size(); i++) {
            std::cout << i << ": " << output[i] << "\n";
        }
        std::cout << "\n\n";
    }
    catch(const std::exception& ex) {
        std::cerr << ex.what();
    }
}

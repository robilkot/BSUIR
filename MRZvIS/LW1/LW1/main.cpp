// Лабораторная работа №1 по дисциплине МРЗвИС
// Вариант 1: алгоритм вычисления произведения пары 4-разрядных чисел умножением с младших разрядов со сдвигом множимого (частичного произведения) влево
// Выполнил студент группы 221701 БГУИР Робилко Тимур Маркович
//
// Главный файл программы
//
// Источники:
// - Формальные модели обработки информации и параллельные модели решения задач : учеб.-метод. пособие / В. П. Ивашенко. – Минск : БГУИР, 2020


#include <cstdint>
#include <iostream>

#include "Arithmetics.h"
#include "InputReader.h"


void process(int n, int r, bool debug)
{
    try {
        //const auto& input = read_input("input.txt");
        //const auto& A = input.first;
        //const auto& B = input.second;
        std::vector<uint32_t> A;
        std::vector<uint32_t> B;
        for (int i = 0; i < r; i++)
        {
            A.push_back(i);
            B.push_back(i);
        }

        // show input data
        if (debug) {
            std::cout << "\nsource pairs:\n";
            for (int i = 0; i < A.size(); i++) {
                std::cout << i << ": {" << A[i] << ", " << B[i] << "}\n";
            }
            std::cout << "\n";
        }


        const auto& output = multiply_pairs(A, B, n, debug);


        // show output data
        if (debug)
        {
            std::cout << "\nprocessed data:\n";
            for (size_t i = 0; i < output.size(); i++) {
                std::cout << i << ": " << output[i] << "\n";
            }
            std::cout << "\n\n";
        }
    }
    catch (const std::exception& ex) {
        std::cerr << ex.what();
    }
}

int main(int argc, char** argv)
{
    int max_n = 1;
    int max_r = 20;

    for (int r = 1; r <= max_r; r++)
    {
        int n = 1;
        std::cout << "r=" << r << ", n=" << n << ",";
        process(n, r, false);
    }
    std::cout << "\n";

    for (int r = 1; r <= max_r; r++)
    {
        int n = 8;
        std::cout << "r=" << r << ", n=" << n << ",";
        process(n, r, false);
    }
}

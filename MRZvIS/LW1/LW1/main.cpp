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

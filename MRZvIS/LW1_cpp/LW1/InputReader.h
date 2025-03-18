// ������������ ������ �1 �� ���������� ������
// ������� 1: �������� ���������� ������������ ���� 4-��������� ����� ���������� � ������� �������� �� ������� ��������� (���������� ������������) �����
// �������� ������� ������ 221701 ����� ������� ����� ��������
//
// ����, ���������� �� ������ ������� ������ �� �����
//
// ���������:
// - ���������� ������ ��������� ���������� � ������������ ������ ������� ����� : ����.-�����. ������� / �. �. ��������. � ����� : �����, 2020


#pragma once

#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

std::pair<std::vector<uint32_t>, std::vector<uint32_t>> read_input(const std::string& filename)
{
    std::vector<uint32_t> A;
    std::vector<uint32_t> B;

    std::ifstream inputFile(filename);

    if (!inputFile.is_open()) {
        throw std::exception("Can't open file");
    }

    std::string content((std::istreambuf_iterator<char>(inputFile)),
        std::istreambuf_iterator<char>());

    // split file content into lines
    std::istringstream iss(content);
    std::vector<std::string> lines;
    std::string line;
    while (std::getline(iss, line)) {
        lines.push_back(line);
    }

    for (size_t i = 0; i < lines.size(); ++i) {
        std::istringstream lineStream(lines[i]);
        uint32_t value;
        if (lineStream >> value) {
            A.push_back(value);

            if (lineStream >> value) {
                B.push_back(value);
            }
            else {
                throw std::exception("No number in pair");
            }
        }
    }

    return std::make_pair(A, B);
}
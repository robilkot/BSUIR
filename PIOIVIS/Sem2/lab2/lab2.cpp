#include <iostream>
#include <fstream>
#include <algorithm>

#include <string>
#include <vector>
#include <set>

// Парсинг строки во множество
std::set<std::string> stringToSet(std::string string)
{
	std::set<std::string> currentSet;
	std::string currentElement;
	size_t depth = 0; // "Глубина" подмножества, в котором мы сейчас находимся

	if (string.empty()) return {};

	for (size_t index = 1; index < string.size() - 1; index++) // Индексация без крайних элементов т.к. это скобки всего множества
	{
		switch (string[index]) {
		case '{':
		case '<': {
			currentElement += string[index];
			depth++;
			break;
		}
		case '}':
		case '>': {
			currentElement += string[index];
			if (depth) --depth;
			break;
		}
		case ',': {
			if (depth) {
				currentElement = currentElement + string[index] + ' ';
			}
			else if (!currentElement.empty()) {
				currentSet.emplace(currentElement);
				currentElement.clear();
			}
			break;
		}
		case ' ': break;
		default: {
			currentElement += string[index];
			break;
		}
		}
	}
	if (!currentElement.empty()) currentSet.emplace(currentElement);

	return currentSet;
}

std::string sortSet(std::string set)
{
	std::set<std::string> currentSet;
	std::string currentElement;
	size_t depth = 0; // "Глубина" подмножества, в котором мы сейчас находимся

	if (set.empty()) return {};

	for (size_t index = 1; index < set.size() - 1; index++) // Индексация без крайних элементов т.к. это скобки всего множества
	{
		switch (set[index]) {
		case '{':
		case '<': {
			currentElement += set[index];
			depth++;
			break;
		}
		case '}':
		case '>': {
			currentElement += set[index];
			if (depth) --depth;
			break;
		}
		case ',': {
			if (depth) {
				currentElement = currentElement + set[index] + ' ';
			}
			else if (!currentElement.empty()) {
				if (currentElement[0] == '{') currentElement = sortSet(currentElement);

				currentSet.emplace(currentElement);
				currentElement.clear();
			}
			break;
		}
		case ' ': break;
		default: {
			currentElement += set[index];
			break;
		}
		}
	}
	if (!currentElement.empty()) {
		if (currentElement[0] == '{') currentElement = sortSet(currentElement);

		currentSet.emplace(currentElement);
	}

	std::string output = "{";
	for (const auto& element : currentSet)
		output += element + ", ";

	if (output.size() > 1 ) {
		output.resize(output.size() - 2);
	}
	output += '}';
	
	return output;
}

// Чтение вектора множеств из файла
std::vector<std::set<std::string>> readFromFile(std::string fileName)
{
	std::ifstream file(fileName);
	if (!file) {
		std::cout << "Couldn't open file!\n";
		return {};
	}

	std::vector<std::set<std::string>> result;

	std::string currentLine;
	while (getline(file, currentLine)) {
		currentLine = sortSet(currentLine);
		result.push_back(stringToSet(currentLine));
	}

	return result;
}

// Объединения вектора множеств в одно множество
std::set<std::string> uniteSets(const std::vector<std::set<std::string>>& sets)
{
	std::set<std::string> result;

	for (const auto& set : sets)
		for (const auto& element : set) {
			result.emplace(element); // Добавляем все элементы в итоговое множество
		}
	return result;
}

// Вывод на экран множества
void showSet(std::set<std::string> set)
{
	std::cout << "Showing set:\n{";

	for (auto it = set.begin(); it != set.end(); ++it) std::cout << *it << ", ";

	if (!set.empty()) std::cout << "\b\b";
	std::cout << "}  \n\n";
}

int main(int argc, char** argv)
{
	std::string fileName = argv[1] == NULL ? "test.txt" : argv[1];
	std::vector<std::set<std::string>> sets = readFromFile(fileName); // Читаем из данного файла или из дефолтного test.txt
	for (const auto& set : sets) showSet(set); // Показываем прочитанное

	std::cout << "--- Uniting all given sets ---\n\n";

	auto set = uniteSets(sets);
	showSet(set); // Показываем результат объединения
}
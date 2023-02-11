//Написать программу обработки файла данных, состоящих из структур, в
//которой реализованы следующие функции: стандартная обработка файла (создание, просмотр, добавление); линейный поиск в файле; сортировка массива
//(файла) методами прямого выбора и QuickSort; двоичный поиск в отсортированном массиве. 

//6. Информация о сотрудниках фирмы включает: ФИО, табельный номер,
//количество отработанных часов за месяц, почасовой тариф. Рабочее время
//свыше 144 ч считается сверхурочным и оплачивается в двойном размере.
//Вывести размер заработной платы каждого сотрудника фирмы за вычетом подоходного налога (12 % от суммы заработка). Ключ: размер заработной платы

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <conio.h>

#define FEE 12

struct Worker
{
	std::string name = std::string(30,'\0');
	int number = 0,
		hoursPerMonth = 0,
		moneyPerHour = 0,
		salary = 0;

	void calculateSalary() {
		salary = hoursPerMonth > 144 ?
			(moneyPerHour * (144 + 2 * (hoursPerMonth - 144))) * (1 - FEE) :
			moneyPerHour * hoursPerMonth * (100 - FEE);
	}
};

inline void calculateAllSalary(std::vector<Worker>& workers) {
	for (Worker& worker : workers) worker.calculateSalary();
}

void displayWorker(const Worker& worker) {
	std::cout << worker.name << " has number " << worker.number <<
		",\n" << worker.hoursPerMonth << " working hours per month and " << worker.moneyPerHour << " per hour income\n" <<
		"Salary is " << worker.salary << "\n\n";
}

void displayAllWorkers(std::vector<Worker>& workers) {
	if (workers.empty()) {
		std::cout << "No workers :(\n\n";
		return;
	}

	std::cout << "Here are all workers:\n\n";
	for (Worker& worker : workers) displayWorker(worker);
}

std::vector<Worker> readFile(std::string path)
{
	std::ifstream file(path);
	if (!file.is_open()) {
		std::cout << "Error opening file.\n";
		return {};
	}

	std::vector<Worker> workers;

	while (!file.eof()) {
		Worker worker;

		std::getline(file, worker.name);
		if (worker.name.empty()) break;

		file >> worker.number >> worker.hoursPerMonth >> worker.moneyPerHour;
		workers.push_back(worker);

		std::getline(file, worker.name);
	} 

	file.close();
	return workers;
}

void writeFile(std::string path, std::vector<Worker>& workers)
{
	std::ofstream file(path);
	for (const Worker& worker : workers) {
		file << worker.name << "\n" << worker.number << " " << worker.hoursPerMonth << " " << worker.moneyPerHour << "\n";
	}
}

Worker inputWorker() {
	Worker worker;
	std::cout << "Input name:\n";
	std::getline(std::cin, worker.name);

	std::cout << "Input number of worker, hours of works per month, money per hour for worker:\n";
	std::cin >> worker.number >> worker.hoursPerMonth >> worker.moneyPerHour;

	worker.calculateSalary();
	return worker;
}

void linearSearch(std::vector<Worker>& workers, int lowestSalary) {
	std::cout << "List of workers with salary >= than " << lowestSalary << "\n";
	for (Worker& worker : workers)
		if (worker.salary >= lowestSalary) displayWorker(worker);
}

void directChoiseSort(std::vector<Worker>& workers) {
	for (int i = 0; i < workers.size() - 1; i++) {
		for (int j = i + 1; j < workers.size(); j++)
			if (workers[j].salary < workers[i].salary) std::swap(workers[i], workers[j]);
	}
}

void quickSort(std::vector<Worker>& workers, std::size_t start, std::size_t end)
{
	if (start > end) return;
	int i = start;
	int j = end;
	int pivot = workers[(i + j) / 2].salary;

	while (i < j)
	{
		while (workers[i].salary < pivot)
			i++;
		while (workers[j].salary > pivot)
			j--;
		if (i <= j)
		{
			std::swap(workers[i], workers[j]);
			i++;
			j--;
		}
	}
	if (j > start && j != end)
		quickSort(workers, start, j);
	if (i < end && i != start)
		quickSort(workers, i, end);
}

void binarySearch(std::vector<Worker>& workers, int value, std::size_t start, std::size_t end) {
	if (start > end) return;

	std::size_t pivot = (start + end) / 2;
	if (workers[pivot].salary < value) {
		binarySearch(workers, value, pivot + 1, end);
	}
	else if (workers[pivot].salary > value) {
		binarySearch(workers, value, start, pivot - 1);
	}
	else displayWorker(workers[pivot]);
}

int main() {
	std::vector<Worker> workers;
	std::string path = "workers.txt";

	char option = 'q';
	do {
		std::cout << "Pls choose action.\n1 - show all workers\n2 - write to file\n" << 
					"3 - read from file\n4 - manually append worker\n5 - delete last worker\n" <<
					"6 - linear search\n7 - sorting with direct choise algorithm\n" <<
					"8 - sorting with quicksort\n9 - binary search (quicksort included)\nq - exit" << "\n\n";
		option = _getch();

		switch (option)
		{
		case '1': displayAllWorkers(workers); break;
		case '2': writeFile(path, workers); break;
		case '3': workers = readFile(path); calculateAllSalary(workers); break;
		case '4': workers.push_back(inputWorker()); break;
		case '5': workers.pop_back(); break;
		case '6': {
			int lowestSalary = 0;
			std::cout << "Input lowest salary to search from workers:\n";
			std::cin >> lowestSalary;
			linearSearch(workers, lowestSalary);
			break;
		}
		case '7': {
			directChoiseSort(workers);
			break;
		}
		case '8': {
			quickSort(workers, 0, workers.size() - 1);
			break;
		}
		case '9': {
			if (!workers.empty()) {
				int salary = 0;
				std::cout << "Input salary to search from workers:\n";
				std::cin >> salary;
				quickSort(workers, 0, workers.size() - 1);

				binarySearch(workers, salary, 0, workers.size() - 1);
			}
			break;
		}
		case 'q': break;
		default: std::cout << "You entered wrong number, try again\n";
		}
	} while (option != 'q');
}
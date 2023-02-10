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

constexpr int FEE = 12;

struct Worker
{
	std::string name = std::string(30, ' ');
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

void displayWorkers(std::vector<Worker>& workers) {
	for (int i = 0; i < workers.size(); i++) {
		workers[i].calculateSalary();
		std::cout << workers[i].name << " " << workers[i].number << "\n" <<
			workers[i].hoursPerMonth << " " << workers[i].moneyPerHour << "\n" <<
			"Salary is " << workers[i].salary << "\n\n";
	}
}

void readFile(std::string path, std::vector<Worker>& workers)
{
	std::ifstream file(path, std::ios::binary);
	if (!file.is_open()) {
		std::cout << "Error opening file.\n";
		return;
	}

	file.seekg(0, std::ios::end);
	std::streampos fileSize = file.tellg();
	file.seekg(0, std::ios::beg);

	workers.reserve(fileSize);

	Worker worker;
	while (!file.eof()) {
		file.read((char*)&worker, sizeof(Worker));
		workers.push_back(worker);
	} 
}

void writeFile(std::string path, std::vector<Worker>& workers)
{
	std::ofstream file(path, std::ios::ate | std::ios::binary);
	if(!workers.empty()) file.write((char*) &workers[0], workers.size());
}

Worker inputWorker() {
	Worker worker;
	std::cout << "Input name:\n";
	std::cin.clear();
	std::getline(std::cin, worker.name);

	std::cout << "Input number of worker, hours of works per month, money per hour for worker:\n";
	std::cin >> worker.number >>
		worker.hoursPerMonth >> worker.moneyPerHour;

	return worker;
}

void linearSearch() {

}

/*quicksort, прямой выбор*/

int main() {
	std::vector<Worker> workers;
	std::string path = "workers.txt";

	bool exit = 0;
	do {
		std::cout << "Pls choose action:\n";
		switch (_getch()) {
		case '1': {
			displayWorkers(workers);
			break;
		}
		case '2': { 
			writeFile(path, workers);
			break;
		}
		case '3': { 
			readFile(path, workers);
			break;
		}
		case '4': { 
			workers.push_back(inputWorker());
			break;
		}
		case '5': {

			break;
		}
		case '6': {

			break;
		}
		case '7': {

			break;
		case '8': {

			break;
		}
		case 'q': exit = 1; break;
		default: {

		}
		}
		}
	} while (!exit);
}
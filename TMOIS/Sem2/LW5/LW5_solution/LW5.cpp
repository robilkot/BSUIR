#include <iostream>
#include <set>
#include <tuple>

using namespace std;

typedef set<pair<int, int>> Graphic;
typedef set<int> Set;
typedef tuple<Set, Set, Graphic> Match;

void showGraphic(const Graphic& graphic) //Функция вывода графика в консоль
{
	int i = 0;
	cout << "(";
	for (const auto& a : graphic) {
		cout << '<' << a.first << ',' << a.second << ">"; //Поэлементный вывод графика D в консоль
		if (i != graphic.size() - 1) cout << ", ";
		i++;
	}
	cout << ")\n";
}

Graphic createGraphic(char x) //Функция создания графика с вводом элементов пользователем
{
	cout << "Input cardinality of graphic " << x << "\n";
	size_t graphSize = 0;
	cin >> graphSize;

	Graphic result;
	cout << "Input elemets of graphic " << x << " (" << graphSize << " pairs)\n";
	for (size_t i = 0; i < graphSize; i++) {
		int first = 0, second = 0;
		cin >> first >> second; //Ввод пользователем каждого элемента графика
		result.emplace(pair<int,int>(first,second));
	}

	return result;
}

void showSet(const Set& set)
{
	int i = 0;
	cout << "(";
	for (const auto& a : set) {
		cout << a; //Поэлементный вывод графика D в консоль
		if (i != set.size() - 1) cout << ", ";
		i++;
	}
	cout << ")\n";
}

Set createSet(char x) //Функция создания множества с вводом элементов пользователем
{
	cout << "Input cardinality of set " << x << "\n";
	size_t setSize = 0;
	cin >> setSize;

	Set result;
	cout << "Input elemets of set " << x << " (" << setSize << " elements)\n";
	for (size_t i = 0; i < setSize; i++) {
		int element = 0;
		cin >> element; //Ввод пользователем каждого элемента множества
		result.emplace(element);
	}
	return result;
}

Match createMatch(char name, char x, char y, char g) //Функция создания соответствия с вводом элементов пользователем
{
	cout << "Creating match " << name << "\n";
	return { createSet(x), createSet(y), createGraphic(g) };
}

void showMatch(const Match& match, char name)
{
	cout << "Showing match " << name << "\n";
	showSet(get<0>(match));
	showSet(get<1>(match));
	showGraphic(get<2>(match));
}

int main() {
	Match A = createMatch('A', 'X', 'Y', 'G');
	showMatch(A, 'A');

	Match B = createMatch('B', 'U', 'V', 'F');
	showMatch(B, 'B');


	cout << "\nChoose operation on Graphics: \n"
		<< "1 - union\n"
		<< "2 - intersection\n"
		<< "3 - A\\B\n"
		<< "4 - B\\A\n"
		<< "5 - symmetrical difference\n"
		<< "6 - Complement of A\n"
		<< "7 - Complement of B\n"
		<< "8 - Inversion of A\n"
		<< "9 - Composition of A and B\n"
		<< "Input number : \n"; // Предложение пользователю выбрать операцию из списка

	do {
		switch (_getch()) {
		case '1': { // Если пользователь выбрал объединение
			unite(A, B, D); // Выполняем объединение
			showGraphic("union", D); // Выводим в консоль результат (множество D)
			system("pause");
			return 0; // Завершаем работу программы
		}
		case '2': { // Если пользователь выбрал пересечение
			intersect(A, B, D); // Выполняем пересечение
			showGraphic("intersection", D); // Выводим в консоль результат (множество D)
			system("pause");
			return 0; // Завершаем работу программы
		}
		case '3': { // Если пользователь выбрал разность
			difference(A, B, D); // Выполняем разность
			showGraphic("difference", D); // Выводим в консоль результат (множество D)
			system("pause");
			return 0; // Завершаем работу программы
		}
		case '4': { // Если пользователь выбрал разность
			difference(B, A, D); // Выполняем разность
			showGraphic("difference", D); // Выводим в консоль результат (множество D)
			system("pause");
			return 0; // Завершаем работу программы
		}
		case '5': { // Если пользователь выбрал симметрическую разность
			symdifference(A, B, D); // Выполняем симметрическую разность
			showGraphic("symmetrical difference", D); // Выводим в консоль результат (множество D)
			system("pause");
			return 0; // Завершаем работу программы
		}
		case '6': { // Если пользователь выбрал декартово произведение
			complement(U, A, D); // Находим дополнение
			showGraphic("complement", D); // Выводим в консоль результат (множество D)
			system("pause");
			return 0; // Завершаем работу программы
		}
		case '7': { // Если пользователь выбрал декартово произведение
			complement(U, B, D); // Находим дополнение
			showGraphic("complement", D); // Выводим в консоль результат (множество D)
			system("pause");
			return 0; // Завершаем работу программы
		}
		case '8': { // Если пользователь выбрал дополнение
			inversion(A, D); // Находим инверсию
			showGraphic("inversion", D); // Выводим в консоль результат (множество D)
			system("pause");
			return 0; // Завершаем работу программы
		}
		case '9': { // Если пользователь выбрал дополнение
			composition(A, B, D); // Находим инверсию
			showGraphic("composition", D); // Выводим в консоль результат (множество D)
			system("pause");
			return 0; // Завершаем работу программы
		}

		default: { // Если пользователь ввел неверное число
			cout << "\nYou have input wrong number, try again\n"; // Просим повторить ввод
		}
		}
	} while (true);
}
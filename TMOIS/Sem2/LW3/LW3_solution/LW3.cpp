#include <iostream>
#include <vector>
#include <conio.h>

using namespace std;

void showGraphic(string operation, const vector<pair<int, int>>& result) //Функция вывода множества в консоль
{
	cout << "\nThe result of " << operation << " is (";
	int i = 0;
	for (const auto& a : result) {
		cout << '<' << a.first << ',' << a.second << ">"; //Поэлементный вывод множества D в консоль
		if (i != result.size() - 1) cout << ", ";
		i++;
	}
	cout << ")\n";
}

void createGraphic(vector<pair<int, int>>& vec, char x) //Функция создания множества с вводом элементов пользователем
{
	cout << "Input elemets of graphic " << x << " (" << vec.size() << " pairs)\n";
	for (int i = 0; i < vec.size(); i++) cin >> vec[i].first >> vec[i].second; //Ввод пользователем каждого элемента множества
}

void unite(const vector<pair<int, int>>& A, const vector<pair<int, int>>& B, vector<pair<int, int>>& D) //Функция объединения множеств
{
	D.clear();
	for (const auto& a : A) D.push_back(a); //Копируем во множество D все элементы множества A

	bool ignore;
	for (const auto& b : B) { // Проходим по всем элементам множества B
		ignore = false;
		for (const auto& d : D) // Для каждого выбранного элемента мн-ва B проходим по всем элементам множества D
			if (b == d) ignore = true;	// и сравниваем выбранные элементы.

		if (!ignore) D.push_back(b); // Если выбранный эл-т мн-ва B не совпал ни с одним элементом мн-ва D, добавляем выбранный эл-т мн-ва B во мн-во D 
	}
}

void intersect(const vector<pair<int, int>>& A, const vector<pair<int, int>>& B, vector<pair<int, int>>& D) //Операция пересечения множеств
{
	D.clear();
	// На входе в функцию имеем пустое множество D
	for (const auto& a : A) // Проходим по всем элементам множества А
		for (const auto& b : B) // Для каждого выбранного элемента мн-ва A проходим всем по элементам множества B
			if (a == b) D.push_back(a); // и сравниваем выбранные элементы. Если совпали, добавляем выбранный элемент мн-ва A во мн-во D
}

void difference(const vector<pair<int, int>>& A, const vector<pair<int, int>>& B, vector<pair<int, int>>& D) { // Функция нахождения разности множеств ---TODO Фикс выхода за пределы (где?)
	D.clear();
	bool notinB;
	for (const auto& a : A) { // Проходим по элементам множества А
		notinB = true;
		for (const auto& b : B) { // Проходим по элементам множества В
			if (a == b) notinB = false;
		}
		if (notinB) D.push_back(a); // Если элемент мн-ва А не найден во мн-ве В, добавляем в D
	}
}

void symdifference(const vector<pair<int, int>>& A, const vector<pair<int, int>>& B, vector<pair<int, int>>& D) { // Функция нахождения симметрической разности множеств
	vector<pair<int, int>> diffAB, diffBA;
	D.clear();
	difference(A, B, diffAB); // Находим разность множеств A и B
	difference(B, A, diffBA); // Находим разность множеств B и A
	unite(diffAB, diffBA, D); // Объединяем результаты
}

void complement(const vector<pair<int, int>>& U, const vector<pair<int, int>>& A, vector<pair<int, int>>& D) { // Функция нахождения дополнения множества
	D.clear();
	difference(U, A, D); // Находим разность универсума и данного множества
}

void inversion(const vector<pair<int, int>>& A, vector<pair<int, int>>& D) { // Функция нахождения инверсии графика
	D = A;
	for (auto& x : D)
		swap(x.first, x.second);
}

void composition(const vector<pair<int, int>>& A, const vector<pair<int, int>>& B, vector<pair<int, int>>& D) { // Функция нахождения симметрической разности множеств
	D.clear();

	for (const auto& a : A) {
		for (const auto& b : B) {
			pair<int, int> currentPair = { a.first, b.second };
			if (a.second == b.first && !count(D.begin(), D.end(), currentPair)) // Если есть пары для "склейки" и новой пары нету в итоговом графике, добавляем ее туда
				D.push_back(currentPair);
		}
	}
}

int main()
{
	int n1, n2;
	cout << "\nEnter cardinality of Graphic A: \n";
	cin >> n1; //Ввод пользователем мощности множества А
	vector<pair<int, int>> A(n1);
	createGraphic(A, 'A'); //Вызов функции создания множества А

	cout << "\nEnter cardinality of Graphic B: \n";
	cin >> n2; //Ввод пользователем мощности множества B
	vector<pair<int, int>> B(n2);
	createGraphic(B, 'B'); //Вызов функции создания множества B


	showGraphic("view", A); // Вывод множеств на экран
	showGraphic("view", B);

	cout << "\nFilling the universal Set\n";

	vector<pair<int, int>> D, U; // Создаем универсум и далее заполняем
	unite(A, B, U);
	showGraphic("view", U);

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
	 << "Input number : \n"; //Предложение пользователю выбрать операцию из списка

	do {
		switch (_getch()) {
		case '1': { //Если пользователь выбрал объединение
			unite(A, B, D); //Выполняем объединение
			showGraphic("union", D); //Выводим в консоль результат (множество D)
			system("pause");
			return 0; //Завершаем работу программы
		}
		case '2': { //Если пользователь выбрал пересечение
			intersect(A, B, D); //Выполняем пересечение
			showGraphic("intersection", D); //Выводим в консоль результат (множество D)
			system("pause");
			return 0; //Завершаем работу программы
		}
		case '3': { //Если пользователь выбрал разность
			difference(A, B, D); //Выполняем разность
			showGraphic("difference", D); //Выводим в консоль результат (множество D)
			system("pause");
			return 0; //Завершаем работу программы
		}
		case '4': { //Если пользователь выбрал разность
			difference(B, A, D); //Выполняем разность
			showGraphic("difference", D); //Выводим в консоль результат (множество D)
			system("pause");
			return 0; //Завершаем работу программы
		}
		case '5': { //Если пользователь выбрал симметрическую разность
			symdifference(A, B, D); //Выполняем симметрическую разность
			showGraphic("symmetrical difference", D); //Выводим в консоль результат (множество D)
			system("pause");
			return 0; //Завершаем работу программы
		}
		case '6': { //Если пользователь выбрал декартово произведение
			complement(U, A, D); //Находим дополнение
			showGraphic("complement", D); //Выводим в консоль результат (множество D)
			system("pause");
			return 0; //Завершаем работу программы
		}
		case '7': { //Если пользователь выбрал декартово произведение
			complement(U, B, D); //Находим дополнение
			showGraphic("complement", D); //Выводим в консоль результат (множество D)
			system("pause");
			return 0; //Завершаем работу программы
		}
		case '8': { //Если пользователь выбрал дополнение
			inversion(A, D); // Находим инверсию
			showGraphic("inversion", D); //Выводим в консоль результат (множество D)
			system("pause");
			return 0; //Завершаем работу программы
		}
		case '9': { //Если пользователь выбрал дополнение
			composition(A, B, D); // Находим инверсию
			showGraphic("composition", D); //Выводим в консоль результат (множество D)
			system("pause");
			return 0; //Завершаем работу программы
		}

		default: { //Если пользователь ввел неверное число
			cout << "\nYou have input wrong number, try again\n"; //Просим повторить ввод
		}
		}
	} while (true);
}
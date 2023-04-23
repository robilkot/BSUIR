#include <iostream>
#include <string>
#include <set>
#include <tuple>
#include <conio.h>

using namespace std;

typedef set<pair<int, int>> Graphic;
typedef set<int> Set;
typedef tuple<Set, Set, Graphic> Match;

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
		result.emplace(pair<int, int>(first, second));
	}

	return result;
}

Match createMatch(char name, char x, char y, char g) //Функция создания соответствия с вводом элементов пользователем
{
	cout << "Creating match " << name << "\n";
	return { createSet(x), createSet(y), createGraphic(g) };
}

void show(const Set& set, char name = 'A')
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

void show(const Graphic& graphic, char name = 'G') //Функция вывода графика в консоль
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

void show(const Match& match, char name)
{
	cout << "Showing match " << name << "\n";
	show(get<0>(match));
	show(get<1>(match));
	show(get<2>(match));
}

template<typename T>
void unite(const T& A, const T& B, T& D) //Функция объединения множеств
{
	D.clear();
	for (const auto& a : A) D.emplace(a); // Копируем во множество D все элементы множества A

	for (const auto& b : B) // Проходим по всем элементам множества B
		D.emplace(b); // Если выбранный эл-т мн-ва B не совпал ни с одним элементом мн-ва D, добавляем выбранный эл-т мн-ва B во мн-во D 
}

void unite(const Match& A, const Match& B, Match& D)
{
	unite(get<0>(A), get<0>(B), get<0>(D));
	unite(get<1>(A), get<1>(B), get<1>(D));
	unite(get<2>(A), get<2>(B), get<2>(D));
}

template<typename T>
void intersect(const T& A, const T& B, T& D) //Операция пересечения множеств
{
	D.clear(); // На входе в функцию имеем пустое множество D

	for (auto i = A.begin(); i != A.end(); i++) // Проходим по всем элементам множества А
		for (auto k = B.begin(); k != B.end(); k++)// Для каждого выбранного элемента мн-ва A проходим всем по элементам множества B
			if (*i == *k) D.emplace(*i); // и сравниваем выбранные элементы. Если совпали, добавляем выбранный элемент мн-ва A во мн-во D
}

void intersect(const Match& A, const Match& B, Match& D)
{
	intersect(get<0>(A), get<0>(B), get<0>(D));
	intersect(get<1>(A), get<1>(B), get<1>(D));
	intersect(get<2>(A), get<2>(B), get<2>(D));
}

template<typename T>
void difference(const T& A, const T& B, T& D) { // Функция нахождения разности множеств ---TODO Фикс выхода за пределы (где?)
	D.clear();
	bool notinB;
	for (const auto& a : A) { // Проходим по элементам множества А
		notinB = true;
		for (const auto& b : B) { // Проходим по элементам множества В
			if (a == b) {
				notinB = false;
				break;
			}
		}
		if (notinB) D.emplace(a); // Если элемент мн-ва А не найден во мн-ве В, добавляем в D
	}
}

void difference(const Match& A, const Match& B, Match& D)
{
	difference(get<0>(A), get<0>(B), get<0>(D));
	difference(get<1>(A), get<1>(B), get<1>(D));
	difference(get<2>(A), get<2>(B), get<2>(D));
}

void symdifference(const Match& A, const Match& B, Match& D)
{
	Match X, Y;
	difference(A, B, X);
	difference(A, B, Y);
	unite(X, Y, D);
}

void cartesianproduct(const Set& A, const Set& B, Graphic& D) { // Функция нахождения декартова произведения множеств
	for (const auto& element1 : A) {
		for (const auto& element2 : B) {
			D.emplace(pair<int, int>(element1, element2));
		}
	}
}

void complement(const Match& A, Match& D)
{
	Match universum = A;
	cartesianproduct(get<0>(A), get<1>(A), get<2>(universum)); // График универсума делаем равным прямому произведению областей отпр. и прибытия

	difference(universum, A, D);
}

template<typename T>
void inversion(const T& A, T& D) // Функция нахождения инверсии
{
	D.clear();

	for (auto it = A.begin(); it != A.end(); it++) {
		pair<int, int> temp(it->second, it->first);
		D.emplace(temp);
	}
}

void inversion(const Match& A, Match& D) // Функция нахождения инверсии
{
	inversion(get<2>(A), get<2>(D));
}

template<typename T>
void composition(const T& A, const T& B, T& D) // Функция нахождения симметрической разности множеств
{
	D.clear();

	for (const auto& a : A) {
		for (const auto& b : B) {
			if (a.second == b.first) // Если есть пары для "склейки" и новой пары нету в итоговом графике, добавляем ее туда
				D.emplace(pair<int, int>(a.first, b.second));
		}
	}
}

void composition(const Match& A, const Match& B, Match& D) // Функция нахождения симметрической разности множеств
{
	get<0>(D) = get<0>(A); // Область отправления
	get<1>(D) = get<1>(B); // Область прибытия

	composition(get<2>(A), get<2>(B), get<2>(D));
}

void image(const Match& A, const Set& M, Set& D)
{
	for (const auto& pair : get<2>(A)) {
		for (const auto& element : M) {
			if (pair.first == element)
				D.emplace(pair.second);
		}
	}
}

void prototype(const Match& A, const Set& M, Set& D)
{
	for (const auto& pair : get<2>(A)) {
		for (const auto& element : M) {
			if (pair.second == element)
				D.emplace(pair.first);
		}
	}
}

void restriction(const Match& A, const Set& M, Match& D)
{
	D = A;
	get<0>(D) = M;

	erase_if(get<2>(D), [&](auto const& pair) { return !count(M.begin(), M.end(), pair.first); });
}

void continuation(const Match& A, Match& D)
{
	D = A;
	cartesianproduct(get<0>(D), get<1>(D), get<2>(D));
}

int main() {
	Match A = createMatch('A', 'X', 'Y', 'G');
	show(A, 'A');

	Match B = createMatch('B', 'U', 'V', 'F');
	show(B, 'B');

	Match Dmatch;
	Set Dset; // Результирующие множество и соответствие (зависит от операции)

	cout << "\nChoose operation on Graphics: \n"
		<< "1 - union\n"
		<< "2 - intersection\n"
		<< "3 - A\\B\n"
		<< "4 - B\\A\n"
		<< "5 - symmetrical difference\n"
		<< "6 - Complement of A\n"
		<< "7 - Inversion of A\n"
		<< "8 - Composition of A and B\n"
		<< "9 - Image of M for A\n"
		<< "10 - Prototype of N for A\n"
		<< "11 - Restriction of A on W\n"
		<< "12 - Continuation of A on Z\n"
		<< "Input number : \n"; // Предложение пользователю выбрать операцию из списка

	do {
		int operation;
		cin >> operation;
		
		switch (operation) {
		case 1: { // Если пользователь выбрал объединение
			unite(A, B, Dmatch);
			show(Dmatch, 'D');
			system("pause");
			return 0; // Завершаем работу программы
		}
		case 2: { // Если пользователь выбрал пересечение
			intersect(A, B, Dmatch);
			show(Dmatch, 'D');
			system("pause");
			return 0; // Завершаем работу программы
		}
		case 3: { // Если пользователь выбрал разность
			difference(A, B, Dmatch);
			show(Dmatch, 'D');
			system("pause");
			return 0; // Завершаем работу программы
		}
		case 4: { // Если пользователь выбрал разность
			difference(B, A, Dmatch);
			show(Dmatch, 'D');
			system("pause");
			return 0; // Завершаем работу программы
		}
		case 5: { // Если пользователь выбрал симметрическую разность
			symdifference(A, B, Dmatch);
			show(Dmatch, 'D');
			system("pause");
			return 0; // Завершаем работу программы
		}
		case 6: { // Если пользователь выбрал дополнение
			complement(A, Dmatch);
			show(Dmatch, 'D');
			system("pause");
			return 0; // Завершаем работу программы
		}
		case 7: { // Если пользователь выбрал инверсию
			inversion(A, Dmatch);
			show(Dmatch, 'D');
			system("pause");
			return 0; // Завершаем работу программы
		}
		case 8: { // Если пользователь выбрал дополнение
			composition(A, B, Dmatch);
			show(Dmatch, 'D');
			system("pause");
			return 0; // Завершаем работу программы
		}

		case 9: { // Если пользователь выбрал образ
			Set M = createSet('M');

			image(A, M, Dset);
			show(Dset, 'D');
			system("pause");
			return 0; // Завершаем работу программы
		}
		case 10: { // Если пользователь выбрал прообраз
			Set N = createSet('N');

			prototype(A, N, Dset);
			show(Dset, 'D');
			system("pause");
			return 0; // Завершаем работу программы
		}

		case 11: { // Если пользователь выбрал сужение
			Set W;
			for (int i = 10; i < 25; i++) // Задание множества W
				W.emplace(i);

			restriction(A, W, Dmatch);
			show(Dmatch, 'D');
			system("pause");
			return 0; // Завершаем работу программы
		}
		case 12: { // Если пользователь выбрал продолжение
			continuation(A, Dmatch);
			show(Dmatch, 'D');
			system("pause");
			return 0; // Завершаем работу программы
		}

		default: { // Если пользователь ввел неверное число
			cout << "\nYou have input wrong number, try again\n"; // Просим повторить ввод
		}
		}
	} while (true);
}
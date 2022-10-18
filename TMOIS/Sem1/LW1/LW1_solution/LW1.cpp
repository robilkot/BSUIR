#include <iostream>
#include <vector>
#include <conio.h>

using namespace std;

void Show(string operation, vector<int>& result, int n) //Функция вывода множества в консоль
{
	cout << "\nThe result of " << operation << " of sets A and B = ( ";
	for (int i = 0; i < n; i++)
	{
		cout << result[i] << " "; //Поэлементный вывод множества D в консоль
	}
	cout << ")\n";
}

void make_MN(int n, vector<int>& vec, char x) //Функция создания множества
{
	cout << "Input elemets of set " << x << " (" << n << " elements)\n";
	for (int i = 0; i < n; i++)
	{
		cin >> vec[i]; //Ввод пользователем каждого элемента множества
	}
}

int unite(vector<int>& A, vector<int>& B, int nA, int nB) //Функция объединения множеств
{
	int ignor, plus = 0;
	for (int i = 0; i < nA; i++)
	{
		ignor = 0;
		for (int k = 0; k < nB; k++)
		{
			if (A[i] == B[k]) ignor++;
		}
		if (ignor == 0) plus++, B.push_back(A[i]);
	}
	return plus;
}

int intersect(vector<int>& A, vector<int>& B, vector<int>& D, int n1, int n2) //Операция пересечния множеств
{
	int plus = 0;
	for (int i = 0; i < n1; i++)
	{
		for (int k = 0; k < n2; k++)
		{
			if (A[i] == B[k]) plus++, D.push_back(A[i]);
		}
	}
	return plus;
}

int main()
{
	setlocale(LC_ALL, "Russian");

	int n1, n2, number;

	cout << "\nEnter cardinality of set A: ";
	cin >> n1; //Ввод пользователем мощности множества А
	cout << "\nEnter cardinality of set B: ";
	cin >> n2; //Ввод пользователем мощности множества B

	vector<int> A(n1), B(n2), D;
	make_MN(n1, A, 'A'); //Вызов функции создания первого множества
	make_MN(n2, B, 'B'); //Вызов функции создания второго множества

	cout << "\nChoose operation on sets: \n1 - union\n2 - intersection\nInput number: "; //Предложение пользователю выбрать операцию (объединение или пересечение)
	do {
		switch (_getch()) {
		case '1': { //Если пользователь выбрал объединение
			number = unite(A, B, n1, n2);
			Show("union", B, n2 + number);
			system("pause");
			return 0;
		}
		case '2': { //Если пользователь выбрал пересечение
			number = intersect(A, B, D, n1, n2);
			Show("intersection", D, number);
			system("pause");
			return 0;
		}
		default: { //Если пользователь ввел неверное число (просим повторить ввод)
			cout << "\nYou have input wrong number, try again\n";
			break;
		}
		}
	} while (true);
}
#include <iostream>
#include <vector>
#include <conio.h>

using namespace std;

void showSet(string operation, vector<int>& result) //Функция вывода множества в консоль
{
	cout << "\nThe result of " << operation << " of sets A and B = ( ";
	for (int i = 0; i < result.size(); i++) cout << result[i] << " "; //Поэлементный вывод множества D в консоль
	cout << ")\n";
}

void createSet(vector<int>& vec, char x) //Функция создания множества
{
	cout << "Input elemets of set " << x << " (" << vec.size() << " elements)\n";
	for (int i = 0; i < vec.size(); i++) cin >> vec[i]; //Ввод пользователем каждого элемента множества
}

void unite(vector<int>& A, vector<int>& B, vector<int>& D) //Функция объединения множеств
{
	for (int i = 0; i < A.size(); i++) D.push_back(A[i]); //Копируем во множество D все элементы множества A

	bool ignore;
	for (int i = 0; i < B.size(); i++) { //Проходим всем по элементам множества B
			ignore = false;
			for (int k = 0; k < D.size(); k++) { //Проходим по всем элементам множества D
				if (B[i] == D[k]) ignore=true;		//и сравниваем выбранные элементы. Если совпали - помечаем совпадение с помощью логической переменной.
			}
			if (!ignore) D.push_back(B[i]); //Если выбранный эл-т мн-ва B не совпал ни с одним элементом мн-ва D, добавляем выбранный эл-т мн-ва B во мн-во D 
	}
}

void intersect(vector<int>& A, vector<int>& B, vector<int>& D) //Операция пересечения множеств
{
	//На входе в функцию имеем пустое множество D
	for (int i = 0; i < A.size(); i++) //Проходим всем по элементам множества А
	{
		for (int k = 0; k < B.size(); k++) //Проходим всем по элементам множества B
		{
			if (A[i] == B[k]) D.push_back(A[i]); //Сравниваем выбранные элементы. Если совпали, добавляем выбранный элемент мн-ва A во мн-во D
		}
	}
}

int main()
{
	int n1, n2;
	cout << "\nEnter cardinality of set A: ";
	cin >> n1; //Ввод пользователем мощности множества А
	cout << "\nEnter cardinality of set B: ";
	cin >> n2; //Ввод пользователем мощности множества B

	vector<int> A(n1), B(n2), D;
	createSet(A, 'A'); //Вызов функций создания множеств
	createSet(B, 'B'); //

	cout << "\nChoose operation on sets: \n1 - union\n2 - intersection\nInput number: "; //Предложение пользователю выбрать операцию (объединение или пересечение)
	do {
		switch (_getch()) {
		case '1': { //Если пользователь выбрал объединение
			unite(A, B, D); //Выполняем объединение
			showSet("union", D); //Выводим в консоль результат (множество D)
			system("pause");
			return 0;
		}
		case '2': { //Если пользователь выбрал пересечение
			intersect(A, B, D); //Выполняем пересечение
			showSet("intersection", D); //Выводим в консоль результат (множество D)
			system("pause");
			return 0;
		}
		default: { //Если пользователь ввел неверное число
			cout << "\nYou have input wrong number, try again\n"; //Просим повторить ввод
			break;
		}
		}
	} while (true);
}
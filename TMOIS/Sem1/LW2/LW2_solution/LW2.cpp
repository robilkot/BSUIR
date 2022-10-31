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

void createSet(vector<int>& vec, char x) //Функция создания множества с вводом элементов пользователем
{
	cout << "Input elemets of set " << x << " (" << vec.size() << " elements)\n";
	for (int i = 0; i < vec.size(); i++) cin >> vec[i]; //Ввод пользователем каждого элемента множества
}

void generateSets(vector<int>& vec1, vector<int>& vec2) { //Функция заполнения множеств высказываниями
	for (int i = 0; i < vec1.size(); i++) vec1[i] = pow((i + 1), 2) - 5 * (i + 1) + 4; 
	for (int i = 0; i < vec2.size(); i++) vec2[i] = 2*pow((i + 1), 2) - (i + 1) + 7;
	cout << "Sets filled by the expressions\n";
}

void unite(vector<int>& A, vector<int>& B, vector<int>& D) //Функция объединения множеств
{
	for (int i = 0; i < A.size(); i++) D.push_back(A[i]); //Копируем во множество D все элементы множества A

	bool ignore;
	for (int i = 0; i < B.size(); i++) { //Проходим по всем элементам множества B
		ignore = false;
		for (int k = 0; k < D.size(); k++) { //Для каждого выбранного элемента мн-ва B проходим по всем элементам множества D
			if (B[i] == D[k]) ignore = true;	//и сравниваем выбранные элементы.
		}
		if (!ignore) D.push_back(B[i]); //Если выбранный эл-т мн-ва B не совпал ни с одним элементом мн-ва D, добавляем выбранный эл-т мн-ва B во мн-во D 
	}
}

void intersect(vector<int>& A, vector<int>& B, vector<int>& D) //Операция пересечения множеств
{
	//На входе в функцию имеем пустое множество D
	for (int i = 0; i < A.size(); i++) //Проходим по всем элементам множества А
	{
		for (int k = 0; k < B.size(); k++) {	//Для каждого выбранного элемента мн-ва A проходим всем по элементам множества B
			if (A[i] == B[k]) D.push_back(A[i]); //и сравниваем выбранные элементы. Если совпали, добавляем выбранный элемент мн-ва A во мн-во D
		}
	}
}

void difference(vector<int>& A, vector<int>& B, vector<int>& D) { // Функция нахождения разности множеств
	bool notinB;
	for (int i = 0; i < A.size(); i++) { // Проходим по элементам множества А
		notinB = true;
		for (int k = 0; k < B.size(); i++) { // Проходим по элементам множества В
			if (A[i] == B[k]) notinB=false;
		}
		if (notinB) D.push_back(A[i]); // Если элемент мн-ва А не найден во мн-ве В, добавляем в D
	}
}

void symdifference(vector<int>& A, vector<int>& B, vector<int>& D) { // Функция нахождения симметрической разности множеств
	vector<int> AB, BA;
	difference(A, B, AB); // Находим разность множеств A и B
	difference(B, A, BA); // Находим разность множеств B и A
	unite(AB, BA, D); // Объединяем результаты
}

void filluniversum(vector<int>& U) { // Функция заполнения универсума
	for (int i = 1; i < 100; i++) U.push_back(i);
}

void complement(vector<int>& U, vector<int>& A, vector<int>& D) { // Функция нахождения дополнения множества
	difference(U, A, D); // Находим разность универсума и данного множества
}

vector<vector<int>> cartesianproduct(vector<int>& A, vector<int>& B) { // Функция нахождения декартова произведения множеств
	vector<vector<int>> Output;
	for (int i = 0; i < A.size(); i++) {
		for (int k = 0; k < B.size(); k++) Output.push_back({ A[i], B[k] });
	}
	return Output;
}

int main()
{
	int n1, n2;
	cout << "\nEnter cardinality of set A: ";
	cin >> n1; //Ввод пользователем мощности множества А
	vector<int> A(n1);
	createSet(A, 'A'); //Вызов функции создания множества А

	cout << "\nEnter cardinality of set B: ";
	cin >> n2; //Ввод пользователем мощности множества B
	vector<int> B(n2);
	createSet(B, 'B'); //Вызов функции создания множества B

	vector<int> D;

	cout << "\nChoose operation on sets: \n1 - union\n2 - intersection\nInput number: "; //Предложение пользователю выбрать операцию (объединение или пересечение)
	do {
		switch (_getch()) {
		case '1': { //Если пользователь выбрал объединение
			unite(A, B, D); //Выполняем объединение
			showSet("union", D); //Выводим в консоль результат (множество D)
			system("pause");
			return 0; //Завершаем работу программы
		}
		case '2': { //Если пользователь выбрал пересечение
			intersect(A, B, D); //Выполняем пересечение
			showSet("intersection", D); //Выводим в консоль результат (множество D)
			system("pause");
			return 0; //Завершаем работу программы
		}
		default: { //Если пользователь ввел неверное число
			cout << "\nYou have input wrong number, try again\n"; //Просим повторить ввод
		}
		}
	} while (true);
}
#include <iostream>
#include <vector>
#include <conio.h>

using namespace std;

void showSet(string operation, vector<float>& result) //Функция вывода множества в консоль
{
	cout << "\nThe result of " << operation << " of sets A and B = ( ";
	for (int i = 0; i < result.size(); i++) cout << result[i] << " "; //Поэлементный вывод множества D в консоль
	cout << ")\n";
}

void createSet(vector<float>& vec, char x) //Функция создания множества с вводом элементов пользователем
{
	cout << "Input elemets of set " << x << " (" << vec.size() << " elements)\n";
	for (int i = 0; i < vec.size(); i++) cin >> vec[i]; //Ввод пользователем каждого элемента множества
}

void generateSets(vector<float>& vec1, vector<float>& vec2) { //Функция заполнения множеств высказываниями
	for (int i = 0; i < vec1.size(); i++) vec1[i] = sqrt(i) + 2; 
	for (int i = 0; i < vec2.size(); i++) vec2[i] = sqrt(i + 12);
	cout << "Sets filled by the expressions\n";
}

void unite(vector<float>& A, vector<float>& B, vector<float>& D) //Функция объединения множеств
{
	D.clear();
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

void intersect(vector<float>& A, vector<float>& B, vector<float>& D) //Операция пересечения множеств
{
	D.clear();
	//На входе в функцию имеем пустое множество D
	for (int i = 0; i < A.size(); i++) //Проходим по всем элементам множества А
	{
		for (int k = 0; k < B.size(); k++) {	//Для каждого выбранного элемента мн-ва A проходим всем по элементам множества B
			if (A[i] == B[k]) D.push_back(A[i]); //и сравниваем выбранные элементы. Если совпали, добавляем выбранный элемент мн-ва A во мн-во D
		}
	}
}

void difference(vector<float>& A, vector<float>& B, vector<float>& D) { // Функция нахождения разности множеств ---TODO Фикс выхода за пределы (где?)
	D.clear();
	bool notinB;
	for (int i = 0; i < A.size(); i++) { // Проходим по элементам множества А
		notinB = true;
		for (int k = 0; k < B.size(); k++) { // Проходим по элементам множества В
			if (A[i] == B[k]) notinB=false;
		}
		if (notinB) D.push_back(A[i]); // Если элемент мн-ва А не найден во мн-ве В, добавляем в D
	}
}

void symdifference(vector<float>& A, vector<float>& B, vector<float>& D) { // Функция нахождения симметрической разности множеств
	vector<float> diffAB, diffBA;
	D.clear();
	difference(A, B, diffAB); // Находим разность множеств A и B
	difference(B, A, diffBA); // Находим разность множеств B и A
	unite(diffAB, diffBA, D); // Объединяем результаты
}

void filluniversum(vector<float>& U) { // Функция заполнения универсума натуральными числами от 1 до 100
	for (int i = 1; i < 101; i++) U.push_back(i);
}

void complement(vector<float>& U, vector<float>& A, vector<float>& D) { // Функция нахождения дополнения множества
	D.clear();
	difference(U, A, D); // Находим разность универсума и данного множества
}

void cartesianproduct(vector<float>& A, vector<float>& B) { // Функция нахождения декартова произведения множеств
	vector<vector<float>> Output;
	for (int i = 0; i < A.size(); i++) {
		for (int k = 0; k < B.size(); k++) Output.push_back({ A[i], B[k] });
	}

	cout << "\nThe cartesian product is (";
	for (int i = 0; i < Output.size(); i++) {
		cout << "<";
		for (int k = 0; k < Output[i].size(); k++) {
			cout << Output[i][k];
			if(k!= Output[i].size()-1) cout << " ";
		}
		cout << ">";
		if (i != Output.size() - 1) cout << ", ";
	}
	cout << ")\n";
}

int main()
{
	cout << "\nChoose way of defining sets: \n1 - manually\n2 - by expression\nInput number: "; //Предложение пользователю выбрать операцию (объединение или пересечение)
	switch (_getch()) {
	case '1': {
		cout << "Defining set manually\n";
		break;
	}
	case '2': {
		cout << "Defining sets by expressions\n";
		break;
	}
	default: {
		cout << "\nYou have input wrong number, try again\n"; //Просим повторить ввод
		return 0;
	}
	}

	// ---TODO выбор способа задания множества
	int n1, n2;
	cout << "\nEnter cardinality of set A: ";
	cin >> n1; //Ввод пользователем мощности множества А
	vector<float> A(n1);
	createSet(A, 'A'); //Вызов функции создания множества А

	cout << "\nEnter cardinality of set B: ";
	cin >> n2; //Ввод пользователем мощности множества B
	vector<float> B(n2);
	createSet(B, 'B'); //Вызов функции создания множества B

	vector<float> D,U;

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
		case '3': { //Если пользователь выбрал разность
			difference(A, B, D); //Выполняем разность
			showSet("difference", D); //Выводим в консоль результат (множество D)
			system("pause");
			return 0; //Завершаем работу программы
		}
		case '4': { //Если пользователь выбрал симметрическую разность
			symdifference(A, B, D); //Выполняем симметрическую разность
			showSet("symmetrical difference", D); //Выводим в консоль результат (множество D)
			system("pause");
			return 0; //Завершаем работу программы
		}
		case '5': { //Если пользователь выбрал дополнение
			filluniversum(U); // Задаём универсум
			complement(U, A, D); //Находим дополнение
			showSet("complement", D); //Выводим в консоль результат (множество D)
			//complement(U, B, D); //Находим дополнение
			//showSet("complement", D); //Выводим в консоль результат (множество D)
			system("pause");
			return 0; //Завершаем работу программы
		}
		case '6': { //Если пользователь выбрал декартово произведение
			cartesianproduct(A, B); //Находим декартово произведение и выводим в консоль результат (множество D)
			system("pause");
			return 0; //Завершаем работу программы
		}
		default: { //Если пользователь ввел неверное число
			cout << "\nYou have input wrong number, try again\n"; //Просим повторить ввод
		}
		}
	} while (true);
}
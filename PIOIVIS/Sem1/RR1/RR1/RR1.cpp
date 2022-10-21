#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>

//#define DEBUG

using namespace std;

// СТРУКТУРЫ

struct vertex // Структура вершины: Имя, Список инцидентности (СИ), Функция вывода своего СИ
{
	string name;
	vector<int> IncidenceList;

	void DisplayInfo() {
		cout << "\n For vertex " << name << ": ";
		for (int i = 0; i < IncidenceList.size(); i++) cout << IncidenceList[i] << " ";
	}
};

struct graph // Структура графа: Список вершин, Функция вывода СИ всех своих вершин
{
	vector<vertex> Vertices;

	void DisplayAllIncidenceList() {
		for (int i = 0; i < Vertices.size(); i++) Vertices[i].DisplayInfo();
	}
};

// ФУНКЦИИ

vertex GetVertexFromString(string& str) { //Парсинг строки как запись вершины
	vertex Output;

	Output.name = str.substr(0, str.find(" ")); //Парсинг имени вершины
	str.erase(0, Output.name.size() + 1);

	istringstream currentstring(str); 
	string temp;
	while (getline(currentstring, temp, ' ')) { //Парсинг списка инцидентности
		try {
			Output.IncidenceList.push_back(stoi(temp));
		}
		catch (...) {
#ifdef DEBUG
			cout << "Ingnored invalid edge number input!\n";
#endif
		}
	}

	return Output;
}

graph GetGraphFromFile(const char* filename) { // Парсинг графа из файла
	ifstream input(filename);
	if (!input.is_open()) {
		cout << "Error opening file, try again.\n";
		return {};
	}

	graph Output;
	string temp;
	while (getline(input, temp)) {
		Output.Vertices.push_back(GetVertexFromString(temp));
	}

	input.close();
	return Output;
}

void WriteGraphToFile(graph& inp, const char* filename) { // Запись графа в файл
	if (inp.Vertices.empty()) {
		cout << "Tried to write empty graph, aborting\n";
		return;
	}

	ofstream fout(filename);
	if (!fout.is_open()) {
		cout << "Error accesing specified file, try again.\n";
		return;
	}

	for (int i = 0; i < inp.Vertices.size(); i++) {
		fout << inp.Vertices[i].name; // Запись имени вершин
		if (inp.Vertices[i].IncidenceList.empty()) { fout << '\n'; continue; }
		fout << ' ';
		for (int k = 0; k < inp.Vertices[i].IncidenceList.size(); k++) {
			fout << inp.Vertices[i].IncidenceList[k];						// Запись СИ
			if (k != inp.Vertices[i].IncidenceList.size()-1) fout << ' ';	// В частности пробелов между элементами списка
		}
		/*if (i != inp.Vertices.size() - 1)*/ fout << '\n'; // Переходим на новую строку после каждой вершины кроме последней (опционально)
	}

	fout.close();
	cout << "\nGraph succesfully saved in file " << filename << "\n";
}

void FindNeighboorVertices(graph& inpG, int inpV, vector<int>& NeighboorArray) { //Поиск смежных вершин для заданной в графе. Нумерация вершин - с нуля!
	for (int i = 0; i < inpG.Vertices.size(); i++) {
			for (int m = 0; m < inpG.Vertices[i].IncidenceList.size(); m++) {
				for (int n = 0; n < inpG.Vertices[inpV].IncidenceList.size(); n++) {
					if (inpG.Vertices[i].IncidenceList[m] == inpG.Vertices[inpV].IncidenceList[n] && i!=inpV) {
						NeighboorArray.push_back(i);
					}
				}
			}
	}
}

bool CanBeExcluded(graph& inpG, int inpV) { // Проверка на возможность исключения вершины без нарушения гомеоморфизма
	vector<int> check;
	FindNeighboorVertices(inpG, inpV, check);

	if (check.size() != 2) return false; //---TODO дописать проверку для подграфа вида "...-(v)---"
	for (int i = 0; i < inpG.Vertices[check[0]].IncidenceList.size(); i++) {
		for (int k = 0; k < inpG.Vertices[check[1]].IncidenceList.size(); k++) {
			if (inpG.Vertices[check[0]].IncidenceList[i] == inpG.Vertices[check[1]].IncidenceList[k]) return false;
		}
	}
	return true;
}

void ExcludeVertices(graph& inp) { //---TODO Исключение вершин степени 2 из данного графа
	do
	{

	} while (true); //---TODO Проверка весь ли мусор мы удалили
}

graph FindNonPlanarSubgraph(graph& inp) { //---TODO Поиск подграфа данного графа, гомеоморфного К5 или К3,3 (критерий непланарности)
	return {};
}

// MAIN

int main() {
	graph inp = GetGraphFromFile("E:/work/BSUIR/PIOIVIS/Sem1/RR1/RR1/x64/Debug/test.txt");
	
	inp.DisplayAllIncidenceList();

	vector<int> test;
	FindNeighboorVertices(inp, 4, test);
	for (int i = 0; i < test.size(); i++) {
		cout << "\n neighboor for 5: " << test[i] << endl;
	}
	cout << "\n can be excluded 3: "<< CanBeExcluded(inp, 2) << endl;
	cout << "\n can be excluded 2: " << CanBeExcluded(inp, 1) << endl;

	//WriteGraphToFile(inp, "E:/work/BSUIR/PIOIVIS/Sem1/RR1/RR1/x64/Debug/test2.txt");

	system("pause");
	return 0;
}
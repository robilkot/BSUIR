#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>

//#define DEBUG

using namespace std;

// Структура вершины: Имя, Список инцидентности (СИ), Функция вывода своего СИ
//
struct vertex
{
	string name;
	vector<int> IncidenceList;

	void DisplayInfo() {
		cout << "\n For vertex " << name << ": ";
		for (int i = 0; i < IncidenceList.size(); i++) cout << IncidenceList[i] << " ";
	}
};

// Структура графа: Список вершин, Функция вывода СИ всех своих вершин
//
struct graph
{
	vector<vertex> Vertices;

	void DisplayAllIncidenceList() {
		for (int i = 0; i < Vertices.size(); i++) Vertices[i].DisplayInfo();
	}
};

vertex GetVertexFromString(string& str) { //Парсим строку как запись вершины
	vertex Output;

	Output.name = str.substr(0, str.find(" ")); //Парсим имя вершины
	str.erase(0, Output.name.size() + 1);

	istringstream currentstring(str); 
	string temp;
	while (getline(currentstring, temp, ' ')) { //Парсинг списка инцидентности (делимитер - пробел)
		Output.IncidenceList.push_back(stoi(temp)); //----TODO: обработка исключений stoi
	}

	return Output;
}

graph GetGraphFromFile(const char* filename) { //Построчный парсинг файла как граф
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

void WriteGraphToFile(graph inp, const char* filename) { // Запись графа в файл
	ofstream fout(filename);
	if (!fout.is_open()) {
		cout << "Error accesing specified file, try again.\n";
		return;
	}

	for (int i = 0; i < inp.Vertices.size(); i++) {
		fout << inp.Vertices[i].name << ' '; // Запись имени вершин ---TODO сделать проверку на пустой СИ и убрать для таких пробелы
		for (int k = 0; k < inp.Vertices[i].IncidenceList.size(); k++) {
			fout << inp.Vertices[i].IncidenceList[k]; // Запись СИ
			if (k != inp.Vertices[i].IncidenceList.size()-1) fout << ' '; //В частности пробелов между элементами списка
		}
		if(i != inp.Vertices.size()-1) fout << '\n'; //Также переходим на новую строку после каждой вершины кроме последней
	}

	fout.close();
	cout << "\nGraph succesfully saved in file " << filename << "\n";
}

int main() {
	//vertex first{ "test1", {8,2} }, second{ "test2", {1,2,4,5}};
	//graph Gfirst{ {first,second} };
	//Gfirst.DisplayAllIncidenceList();
	
	graph inp = GetGraphFromFile("E:/work/BSUIR/PIOIVIS/Sem1/RR1/RR1/x64/Debug/test.txt");
	
	inp.DisplayAllIncidenceList();

	WriteGraphToFile(inp, "E:/work/BSUIR/PIOIVIS/Sem1/RR1/RR1/x64/Debug/test2.txt");

	system("pause");
	return 0;
}
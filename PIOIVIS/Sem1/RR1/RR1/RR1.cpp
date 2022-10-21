#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>

//#define DEBUG

using namespace std;

// Структура вершины
// Содержит имя и список инцидентности (СИ)
// Содержит функцию вывода своего СИ
//
struct vertex
{
	string name;
	vector<int> Incidence;

	void DisplayInfo() {
		cout << "\n For vertex " << name << ": ";
		for (int i = 0; i < Incidence.size(); i++) cout << Incidence[i] << " ";
	}
};

// Структура графа
// Содержит список вершин
// Содержит функции вывода СИ всех своих вершин
//
struct graph
{
	vector<vertex> Vertices;

	void DisplayAllIncidence() {
		for (int i = 0; i < Vertices.size(); i++) Vertices[i].DisplayInfo();
	}
};

vertex GetFromLine(string str) { //Парсим строку как запись вершины
	vertex Output;

	Output.name = str.substr(0, str.find(" ")); //Парсим имя вершины
	str.erase(0, Output.name.size() + 1);

	istringstream currentstring(str); 
	string temp;
	while (getline(currentstring, temp, ' ')) { //Парсинг списка инцидентности (делимитер - пробел)
		Output.Incidence.push_back(stoi(temp)); //----TODO: обработка исключений stoi
	}

	return Output;
}

graph GetFromFile(const char* filename) { //Построчный парсинг файла как граф
	ifstream input(filename);
	if (!input.is_open()) {
		cout << "Error opening file, try again.\n";
		return {};
	}

	graph Output;
	string temp;
	while (getline(input, temp)) {
		Output.Vertices.push_back(GetFromLine(temp));
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
		fout << inp.Vertices[i].name << ' '; // Запись имени вершин
		for (int k = 0; k < inp.Vertices[i].Incidence.size(); k++) {
			fout << inp.Vertices[i].Incidence[k]; // Запись СИ
			if (k != inp.Vertices[i].Incidence.size()-1) fout << ' '; //В частности пробелов между элементами списка
		}
		if(i != inp.Vertices.size()-1) fout << '\n'; //Также переходим на новую строку после каждой вершины кроме последней
	}

	fout.close();
	cout << "\nGraph succesfully saved in file " << filename << "\n";
}

int main() {
	//vertex first{ "test1", {8,2} }, second{ "test2", {1,2,4,5}};
	//graph Gfirst{ {first,second} };
	//Gfirst.DisplayAllIncidence();
	
	graph inp = GetFromFile("E:/work/BSUIR/PIOIVIS/Sem1/RR1/RR1/x64/Debug/test.txt");
	
	inp.DisplayAllIncidence();

	WriteGraphToFile(inp, "E:/work/BSUIR/PIOIVIS/Sem1/RR1/RR1/x64/Debug/test2.txt");

	system("pause");
	return 0;
}
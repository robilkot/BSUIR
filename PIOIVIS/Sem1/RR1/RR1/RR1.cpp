#include <iostream>
#include <vector>
#include <string>
#include <fstream>

//#define DEBUG

using namespace std;

// Структура вершины
// Содержит имя и список инцидентности (СИ)
// Содержит функцию вывода своего СИ
//
struct Vertex
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
	vector<Vertex> Vertices;

	void DisplayAllIncidence() {
		for (int i = 0; i < Vertices.size(); i++) Vertices[i].DisplayInfo();
	}
};

Vertex GetFromLine(string str) { //Парсим строку как запись вершины
	Vertex Output;
	size_t pos = 0;

	Output.name = str.substr(0, str.find(" ")); //Парсим имя вершины
	str.erase(0, pos + Output.name.size() + 1);

	while ((pos = str.find(" ")) != string::npos) { //Парсим список инцидентности
		int adding;
		try {
			adding = stoi(str.substr(0, pos));
		}
		catch(...) { //На случай нечислового значения в списке инцидентности
		#ifdef DEBUG
		cout << "\nInvalid argument ingnored!\n";
		#endif // DEBUG
		str.erase(0, pos + 1 + str.substr(0, pos).size());
		continue;
		}

		Output.Incidence.push_back(adding);
		str.erase(0, pos + 1 + str.substr(0, pos).size());
	}
	try {
		Output.Incidence.push_back(stoi(str)); //И добавляем последний элемент списка
	}
	catch (...) {
	#ifdef DEBUG
		cout << "\nInvalid argument ingnored!\n";
	#endif // DEBUG
	}

	return Output;
}

graph GetFromFile(const char* filename) {
	ifstream input(filename);
	string gotfromfile;

	if (!input.is_open()) {
		cout << "Error opening file, try again.\n";
		return {};
	}

	graph Output;

	string currentline;
	while (currentline != "") {
		getline(input, gotfromfile);
	}
	

	return Output;
}

int main() {
	//Vertex first{ "test1", {8,2} }, second{ "test2", {1,2,4,5}};
	//graph Gfirst{ {first,second} };
	//Gfirst.DisplayAllIncidence();
	
	//graph inp = ReadFromFile("text.txt");
	
	Vertex test = GetFromLine("Vertex1 1 2 3 4 5");
	test.DisplayInfo();

	system("pause");
	return 0;
}
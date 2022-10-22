#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <conio.h>

#define DEBUG

using namespace std;

// СТРУКТУРЫ

struct vertex // Структура вершины: Имя, Список инцидентности (СИ), Функция вывода своего СИ
{
	string name;
	vector<int> IncidenceList;

	void DisplayInfo() {
		cout << "For vertex " << name << ": ";
		for (int i = 0; i < IncidenceList.size(); i++) cout << IncidenceList[i] << " ";
		cout << "\n";
	}
};

struct graph // Структура графа: Список вершин, Функция вывода СИ всех своих вершин
{
	vector<vertex> Vertices;

	void DisplayAllIncidenceList() {
		for (int i = 0; i < Vertices.size(); i++) Vertices[i].DisplayInfo();
		cout << "\n";
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

#ifdef DEBUG
	cout << "Incidence list for graph from file:\n";
	Output.DisplayAllIncidenceList();
#endif // DEBUG

	return Output;
}

void WriteGraphToFile(graph& inpG, const char* filename) { // Запись графа в файл
	if (inpG.Vertices.empty()) {
		cout << "Tried to write empty graph, aborting\n";
		return;
	}

	ofstream fout(filename);
	if (!fout.is_open()) {
		cout << "Error accesing specified file, try again.\n";
		return;
	}

	for (int i = 0; i < inpG.Vertices.size(); i++) {
		fout << inpG.Vertices[i].name; // Запись имени вершин
		if (inpG.Vertices[i].IncidenceList.empty()) { fout << '\n'; continue; }
		fout << ' ';
		for (int k = 0; k < inpG.Vertices[i].IncidenceList.size(); k++) {
			fout << inpG.Vertices[i].IncidenceList[k];						// Запись СИ
			if (k != inpG.Vertices[i].IncidenceList.size()-1) fout << ' ';	// В частности пробелов между элементами списка
		}
		/*if (i != inp.Vertices.size() - 1)*/ fout << '\n'; // Переходим на новую строку после каждой вершины кроме последней (опционально)
	}

	fout.close();
	cout << "\nGraph succesfully saved in file " << filename << "\n";
}

void FindNeighboorVertices(graph& inpG, int inpV, vector<int>& NeighboorArray) { // Получение номеров смежных вершин для заданной в графе в данный список
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

	if (check.size() != 2) return false;
	for (int i = 0; i < inpG.Vertices[check[0]].IncidenceList.size(); i++) {
		for (int k = 0; k < inpG.Vertices[check[1]].IncidenceList.size(); k++) {
			if (inpG.Vertices[check[0]].IncidenceList[i] == inpG.Vertices[check[1]].IncidenceList[k]) return false;
		}
	}
	return true;
}

void FindCommonEdges(graph& inpG, int inpV1, int inpV2, vector<int>& CommonEdgeArray) { // Получение [из СИ первой данной вершины] имени ребра, инцидентного данным вершинам
	for (int i = 0; i < inpG.Vertices[inpV1].IncidenceList.size(); i++) {
		for (int k = 0; k < inpG.Vertices[inpV2].IncidenceList.size(); k++) {
			if (inpG.Vertices[inpV1].IncidenceList[i] == inpG.Vertices[inpV2].IncidenceList[k]) {
				CommonEdgeArray.push_back(inpG.Vertices[inpV1].IncidenceList[i]);
			}
		}
	}
}

int GetEdgeNumber(graph& inpG, int inpV, int edgeName) { // Получение номера [из СИ данной вершины] ребра по его имени.
	for (int i = 0; i < inpG.Vertices[inpV].IncidenceList.size(); i++) {
		if (inpG.Vertices[inpV].IncidenceList[i] == edgeName) return i;
	}
#ifdef DEBUG
	cout << "No match for edge " << edgeName << " and vertex " << inpG.Vertices[inpV].name << "\n";
#endif // DEBUG
	return 0;
}

bool ExcludeVertex(graph& inpG, int inpV) { // Исключение вершины из данного графа. [Опционально] todo: сделать выбор какое именно ребро сохранять при исключении
	if (CanBeExcluded(inpG, inpV)) {
		vector<int> neighboors;
		FindNeighboorVertices(inpG, inpV, neighboors);

		vector<int> commonEdges;
		FindCommonEdges(inpG, inpV, neighboors[0], commonEdges); // Запись в СИ смежных вершин ребра, инцидентного удаляемому
		inpG.Vertices[neighboors[1]].IncidenceList.push_back(commonEdges[0]);

		commonEdges.clear();
		FindCommonEdges(inpG, neighboors[1], inpV, commonEdges); // Удаление из СИ второго соседа ребра, смежного с удаляемым
		inpG.Vertices[neighboors[1]].IncidenceList.erase(inpG.Vertices[neighboors[1]].IncidenceList.begin() + GetEdgeNumber(inpG, neighboors[1], commonEdges[0]));

#ifdef DEBUG
		cout << "Vertex " << inpG.Vertices[inpV].name << " was excluded.\n";
#endif
		
		inpG.Vertices.erase(inpG.Vertices.begin()+inpV);
		return 1;
	}
	else {
#ifdef DEBUG
		cout << "Vertex " << inpG.Vertices[inpV].name << " can not be excluded.\n";
#endif
		return 0;
	}
}

void ExcludeAllVertices(graph& inpG) { // Исключение [не нарушающее гомеоморфизм исходному графу] всех вершин из данного графа
	bool isReady;
	do
	{
		for (int i = 0; i < inpG.Vertices.size(); ) {
			if(!ExcludeVertex(inpG, i)) i++; // Удаление всех возможных вершин
		}

		isReady = true;
		for (int i = 0; i < inpG.Vertices.size(); i++) { // Проверка все ли удалено
			CanBeExcluded(inpG, i) ? isReady = false: NULL;
		}
	} while (!isReady); 
#ifdef DEBUG
	cout << "Excluded all odd vertices.\n";
#endif // DEBUG
}

graph FindSubgraph_K5(graph& inpG) {
	return {};
}

graph FindSubgraph_K33(graph& inpG) {
	return {};
}

graph FindNonPlanarSubgraph(graph& inpG) { //---TODO Поиск подграфа данного графа, гомеоморфного К5 или К3,3 (критерий непланарности)
	return {};
}

// MAIN

int main() {
	graph inp;
	do {
		inp = GetGraphFromFile("test.txt");

		ExcludeAllVertices(inp);

		WriteGraphToFile(inp, "test2.txt");

		cout << "\n--- Press q to exit ---\n\n";
	} while (_getch() != 'q');
	return 0;
}
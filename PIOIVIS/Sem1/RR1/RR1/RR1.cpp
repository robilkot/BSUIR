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

// Парсинг строки как запись вершины
vertex GetVertexFromString(string& str) { 
	vertex Output;

	Output.name = str.substr(0, str.find(" ")); // Парсинг имени вершины
	str.erase(0, Output.name.size() + 1);

	istringstream currentstring(str); 
	string temp;
	while (getline(currentstring, temp, ' ')) { // Парсинг списка инцидентности
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

// Парсинг графа из файла
graph GetGraphFromFile(const char* filename) { 
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
#endif

	return Output;
}

// Запись графа в файл
void WriteGraphToFile(graph& inpG, const char* filename) { 
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

// Получение номеров смежных вершин для заданной в графе в данный список
void GetNeighboorVertices(graph& inpG, int inpV, vector<int>& NeighboorArray) { 
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

// Проверка на возможность исключения вершины без нарушения гомеоморфизма исходному графу
bool CanBeExcluded(graph& inpG, int inpV) { 
	vector<int> check;
	GetNeighboorVertices(inpG, inpV, check);

	if (check.size() != 2) return false;
	for (int i = 0; i < inpG.Vertices[check[0]].IncidenceList.size(); i++) {
		for (int k = 0; k < inpG.Vertices[check[1]].IncidenceList.size(); k++) {
			if (inpG.Vertices[check[0]].IncidenceList[i] == inpG.Vertices[check[1]].IncidenceList[k]) return false;
		}
	}
	return true;
}

// Получение [из СИ первой данной вершины] имени ребра, инцидентного данным вершинам
void GetCommonEdges(vertex& inpV1, vertex inpV2, vector<int>& CommonEdgeArray) { 
	for (int i = 0; i < inpV1.IncidenceList.size(); i++) {
		for (int k = 0; k < inpV2.IncidenceList.size(); k++) {
			if (inpV1.IncidenceList[i] == inpV2.IncidenceList[k]) {
				CommonEdgeArray.push_back(inpV1.IncidenceList[i]);
			}
		}
	}
}

// Получение номера [из СИ данной вершины] ребра по его имени.
int GetEdgeNumber(vertex& inpV, int edgeName) { 
	for (int i = 0; i < inpV.IncidenceList.size(); i++) {
		if (inpV.IncidenceList[i] == edgeName) return i;
	}
#ifdef DEBUG
	cout << "No match for edge " << edgeName << " and vertex " << inpV.name << "\n";
#endif // DEBUG
	return 0;
}

// Исключение вершины из данного графа. [Опционально] ---TODO: сделать выбор какое именно ребро сохранять при исключении
bool ExcludeVertex(graph& inpG, int inpV) { 
	if (CanBeExcluded(inpG, inpV)) {
		vector<int> neighboors;
		GetNeighboorVertices(inpG, inpV, neighboors);

		vector<int> commonEdges;
		GetCommonEdges(inpG.Vertices[inpV], inpG.Vertices[neighboors[0]], commonEdges); // Запись в СИ смежных вершин ребра, инцидентного удаляемому
		inpG.Vertices[neighboors[1]].IncidenceList.push_back(commonEdges[0]);

		commonEdges.clear();
		GetCommonEdges(inpG.Vertices[neighboors[1]], inpG.Vertices[inpV], commonEdges); // Удаление из СИ второго соседа ребра, смежного с удаляемым
		inpG.Vertices[neighboors[1]].IncidenceList.erase(inpG.Vertices[neighboors[1]].IncidenceList.begin() + GetEdgeNumber(inpG.Vertices[neighboors[1]], commonEdges[0]));

#ifdef DEBUG
		cout << "Excluding vertex " << inpG.Vertices[inpV].name << ".\tDone.\n";
#endif
		
		inpG.Vertices.erase(inpG.Vertices.begin()+inpV);
		return 1;
	}
	else {
#ifdef DEBUG
		cout << "Excluding vertex " << inpG.Vertices[inpV].name << ".\tImpossible.\n";
#endif
		return 0;
	}
}

// Исключение [не нарушающее гомеоморфизм исходному графу] всех вершин из данного графа
void ExcludeAllVertices(graph& inpG) { 
#ifdef DEBUG
	cout << "\n";
#endif // DEBUG
	bool isReady;
	int excluded = 0;
	do
	{
		for (int i = 0; i < inpG.Vertices.size(); ) {
			if (!ExcludeVertex(inpG, i)) i++; else excluded++; // Удаление всех возможных вершин
		}

		isReady = true;
		for (int i = 0; i < inpG.Vertices.size(); i++) { // Проверка все ли удалено
			CanBeExcluded(inpG, i) ? isReady = false: NULL;
		}
	} while (!isReady); 
#ifdef DEBUG
	cout << "Excluded all odd vertices (" << excluded << " vertices)\n";
#endif // DEBUG
}

// Получение степени вершины
int GetVertexDegree(vertex& inpV) { 
	return inpV.IncidenceList.size();
}

// Проверка, являются ли данные вершины смежными
bool Neighboors(graph& inpG, int inpV1, int inpV2) { 
	vector<int> NeighboorCheck;
	GetNeighboorVertices(inpG, inpV1, NeighboorCheck);
	return count(NeighboorCheck.begin(), NeighboorCheck.end(), inpV2); // Проходим по массиву соседей вершины 1 и ищем там вершину 2
}

//---TODO Удаление вершины и инцидентных ей ребер из графа (НЕ ИСКЛЮЧЕНИЕ ВЕРШИНЫ!)
void DeleteVertex(graph& inpG, int inpV) { 

}

// Поиск подграфа, изоморфного К5
graph FindSubgraph_K5(graph& inpG) { 
#ifdef DEBUG
	cout << "\n";
#endif

	vector<int> CandidatesLevel1; // 1 уровень кандидатов (по степени вершины >3)
	for (int i = 0; i < inpG.Vertices.size(); i++) {
		if (GetVertexDegree(inpG.Vertices[i]) > 3) {
			CandidatesLevel1.push_back(i);
#ifdef DEBUG
			cout << "Added vertex " << inpG.Vertices[i].name << " to the 1 level candidates\n";
#endif
		}
	}
#ifdef DEBUG
	cout << "\n";
#endif
	if (CandidatesLevel1.size() < 5) { // Возвращаем пустой подграф если кандидатов 1 уровня < 5
		cout << "No K5-isomorphic subgraph found\n";
		return {};
	}

	vector<int> CandidatesLevel2; // 2 уровень кандидатов (по смежности с 4 вершинами-кандидитами 1 уровня)
	for (int i = 0; i < CandidatesLevel1.size(); i++) {
		int NeighboorCandidatesLevel1 = 0;

		for (int k = 0; k < CandidatesLevel1.size(); k++) {
			if(Neighboors(inpG, i, k) && i!=k) NeighboorCandidatesLevel1++;
		}
		if (NeighboorCandidatesLevel1 > 3) {
#ifdef DEBUG
			cout << "Added vertex " << inpG.Vertices[CandidatesLevel1[i]].name << " to the 2 level candidates\n";
#endif
			CandidatesLevel2.push_back(CandidatesLevel1[i]); // ---TODO По готовности функции от вектора кандидатов можно избавиться и писать сразу в аутпут и с ним работать
		}
	}
#ifdef DEBUG
	cout << "\n";
#endif
	if (CandidatesLevel2.size() < 5) { // Возвращаем пустой подграф если кандидатов 2 уровня < 5
		cout << "No K5-isomorphic subgraph found\n";
		return {};
	}

	graph Output;
	for (int i = 0; i < CandidatesLevel2.size(); i++) Output.Vertices.push_back(inpG.Vertices[CandidatesLevel2[i]]); // Добавление всех кандидатов 2 уровня в аутпут
	while (Output.Vertices.size() > 5) DeleteVertex(Output, 0); // Удаление лишних вершин (т.к. граф может быть больше чем К5)
	return Output;
}

graph FindSubgraph_K33(graph& inpG) {
	return {};
}

//---TODO Поиск непланарного подграфа
graph FindNonPlanarSubgraph(graph& inpG) { 
	return {};
}

// MAIN

int main() {
	graph inp;
	do {
		inp = GetGraphFromFile("test.txt");

		ExcludeAllVertices(inp);

		graph temp = FindSubgraph_K5(inp);

		WriteGraphToFile(temp, "test2.txt");

		cout << "\n--- Press q to exit ---\n\n";
	} while (_getch() != 'q');
	return 0;
}
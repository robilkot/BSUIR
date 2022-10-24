#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <conio.h>
#include <algorithm>

#define DEBUG
//#define DeleteOddVertsInSubgraphs

using namespace std;

// СТРУКТУРЫ

// Структура вершины: Имя, Список инцидентности (СИ), Функция вывода своего СИ
struct vertex
{
	string name;
	vector<int> IncidenceList;

	void DisplayInfo() {
		cout << "For vertex " << name << ": ";
		for (int i = 0; i < IncidenceList.size(); i++) cout << IncidenceList[i] << " ";
		cout << "\n";
	}
};

// Структура графа: Список вершин, Функция вывода СИ всех своих вершин
struct graph
{
	vector<vertex> Vertices;

	void DisplayAllIncidenceList() {
		for (int i = 0; i < Vertices.size(); i++) Vertices[i].DisplayInfo();
	}
	bool empty() {
		return !Vertices.size();
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
	cout << "Graph succesfully saved in file " << filename << "\n";
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

// Получение общих вершин данных графов (нумерация по первому графу)
void GetCommonVertices(graph& inpG1, graph& inpG2, vector<int>& commonVertices) {
	cout << "\n";
	for (int i = 0; i < inpG1.Vertices.size(); i++) {
		for (int k = 0; k < inpG2.Vertices.size(); k++) {
			if (inpG1.Vertices[i].name == inpG2.Vertices[k].name) {
				sort(inpG1.Vertices[i].IncidenceList.begin(), inpG1.Vertices[i].IncidenceList.end());
				sort(inpG2.Vertices[k].IncidenceList.begin(), inpG2.Vertices[k].IncidenceList.end());
				if (inpG1.Vertices[i].IncidenceList == inpG2.Vertices[k].IncidenceList) {
					commonVertices.push_back(i);
#ifdef DEBUG
					cout << "Found common vertex " << inpG1.Vertices[i].name << "\n";
#endif // DEBUG
				}
			}
		}
	}
#ifdef DEBUG
	if (!commonVertices.size()) cout << "No common vertices found.\n";
	else cout << "Found " << commonVertices.size() << " common vertices\n\n";
#endif // DEBUG
}

// Получение имён рёбер, инцидентных данным вершинам
void GetCommonEdges(vertex& inpV1, vertex inpV2, vector<int>& CommonEdgeArray) {
	for (int i = 0; i < inpV1.IncidenceList.size(); i++) {
		for (int k = 0; k < inpV2.IncidenceList.size(); k++) {
			if (inpV1.IncidenceList[i] == inpV2.IncidenceList[k]) {
				CommonEdgeArray.push_back(inpV1.IncidenceList[i]);
			}
		}
	}
}

// Получение имён общих рёбер данных графов
void GetCommonEdges(graph& inpG1, graph& inpG2, vector<int>& CommonEdgeArray) {
	vector<int> commonVertices;
	GetCommonVertices(inpG1, inpG2, commonVertices);
	for (int i=0; i < commonVertices.size(); i++) {
		for (int k = 0; k < commonVertices.size(); k++) {
			GetCommonEdges(inpG1.Vertices[commonVertices[i]], inpG2.Vertices[commonVertices[k]], CommonEdgeArray);
		}
	}
	CommonEdgeArray.erase(unique(CommonEdgeArray.begin(), CommonEdgeArray.end()), CommonEdgeArray.end()); // Чистка от дубликатов

#ifdef DEBUG
	if (!CommonEdgeArray.size()) {
		cout << "No common edges found.\n";
		return;
	}
	for (int i = 0; i < CommonEdgeArray.size(); i++) {
		cout << "Found common edge " << CommonEdgeArray[i] << "\n";
	}
	cout << "Found " << CommonEdgeArray.size() << " common edges\n\n";
#endif // DEBUG
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

// Исключение [не нарушающее гомеоморфизм исходному графу] вершины из данного графа. [Опционально] ---TODO: сделать выбор какое именно ребро сохранять при исключении
bool ExcludeVertex(graph& inpG, int inpV) { 
	if (CanBeExcluded(inpG, inpV)) {
		vector<int> neighboors;
		GetNeighboorVertices(inpG, inpV, neighboors);

		vector<int> commonEdges;
		GetCommonEdges(inpG.Vertices[inpV], inpG.Vertices[neighboors[0]], commonEdges); // Запись в СИ первого соседа ребра, инцидентного удаляемой вершине и второму соседу
		inpG.Vertices[neighboors[1]].IncidenceList.push_back(commonEdges[0]);

		commonEdges.clear();
		GetCommonEdges(inpG.Vertices[neighboors[1]], inpG.Vertices[inpV], commonEdges); // Удаление из СИ второго соседа ребра, инцидентного с ним и удаляемой вершиной
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

// Исключение всех возможных вершин из данного графа
void ExcludeAllVertices(graph& inpG) { 
#ifdef DEBUG
	cout << "\nExcluding all odd vertices.\n";
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
	cout << "Excluded all odd vertices. (" << excluded << " vertices)\n\n";
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

// Удаление вершины и инцидентных ей ребер из графа (НЕ ИСКЛЮЧЕНИЕ ВЕРШИНЫ!)
void DeleteVertex(graph& inpG, int inpV) { 
	vector<int> neighboors;
	GetNeighboorVertices(inpG, inpV, neighboors);
	for (int i = 0; i < neighboors.size(); i++) {
		vector<int> commonEdges;
		GetCommonEdges(inpG.Vertices[neighboors[i]], inpG.Vertices[inpV], commonEdges);
		for (int k = 0; k < commonEdges.size(); k++) { // Для каждой смежной вершины удаляем из её СИ номер ребра, инцидентного удаляемой вершине
			inpG.Vertices[neighboors[i]].IncidenceList.erase(inpG.Vertices[neighboors[i]].IncidenceList.begin()+GetEdgeNumber(inpG.Vertices[neighboors[i]],commonEdges[k]));
		}
	}
#ifdef DEBUG
	cout << "Deleted vertex " << inpG.Vertices[inpV].name << "\n";
#endif
	inpG.Vertices.erase(inpG.Vertices.begin() + inpV);
}

// Очистка СИ вершин от ребёр, не ведущих ни в одну вершину
void CleanIncidenceList(graph& inpG, int inpV) {
	vector<int> neighboors;
	GetNeighboorVertices(inpG, inpV, neighboors);
	if (neighboors.size() == 0) {
		inpG.Vertices[inpV].IncidenceList.clear();
		return;
	}

	vector<int> nonOddEdges;
	for (int i = 0; i < inpG.Vertices[inpV].IncidenceList.size(); i++) {
		for (int k = 0; k < neighboors.size(); k++) {
			if (count(inpG.Vertices[neighboors[k]].IncidenceList.begin(), inpG.Vertices[neighboors[k]].IncidenceList.end(), inpG.Vertices[inpV].IncidenceList[i])) {
				//cout << "\nFound not odd edge " << inpG.Vertices[inpV].IncidenceList[i] << " in list for vertex " << inpG.Vertices[inpV].name << "\n";
				nonOddEdges.push_back(inpG.Vertices[inpV].IncidenceList[i]);
			}
		}
	}
	inpG.Vertices[inpV].IncidenceList.clear();
	for (int i = 0; i < nonOddEdges.size(); i++) inpG.Vertices[inpV].IncidenceList.push_back(nonOddEdges[i]);

#ifdef DEBUG
	cout << "Cleaned incidence list for vertex " << inpG.Vertices[inpV].name << "\n";
#endif
}

void CleanAllIncidenceList(graph& inpG) {
#ifdef DEBUG
	cout << "Cleaning incidence lists for all vertices.\n";
#endif
	for (int i = 0; i < inpG.Vertices.size(); i++) {
		CleanIncidenceList(inpG, i);
	}
#ifdef DEBUG
	cout << "Cleaned incidence lists for " << inpG.Vertices.size() << " vertices.\n\n";
#endif
}

// Поиск подграфа, изоморфного К5
graph GetSubgraph_K5(graph& inpG) { 
#ifdef DEBUG
	cout << "Trying to find K5-isomorphic subgraph.\n";
#endif

	vector<int> CandidatesLevel1; // 1 уровень кандидатов (по степени вершины >3)
	for (int i = 0; i < inpG.Vertices.size(); i++) {
		if (GetVertexDegree(inpG.Vertices[i]) > 3) {
			CandidatesLevel1.push_back(i);
#ifdef DEBUG
			cout << "Added vertex " << inpG.Vertices[i].name << " to the 1 level candidates.\n";
#endif
		}
	}
#ifdef DEBUG
	cout << "\n";
#endif
	if (CandidatesLevel1.size() < 5) { // Возвращаем пустой подграф если кандидатов 1 уровня < 5
		cout << "No K5-isomorphic subgraph found.\n\n";
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
			cout << "Added vertex " << inpG.Vertices[CandidatesLevel1[i]].name << " to the 2 level candidates.\n";
#endif
			CandidatesLevel2.push_back(CandidatesLevel1[i]); // ---TODO По готовности функции от вектора кандидатов можно избавиться и писать сразу в аутпут и с ним работать
		}
	}
#ifdef DEBUG
	cout << "\n";
#endif
	if (CandidatesLevel2.size() < 5) { // Возвращаем пустой подграф если кандидатов 2 уровня < 5
		cout << "No K5-isomorphic subgraph found.\n\n";
		return {};
	}

	graph Output;
	for (int i = 0; i < CandidatesLevel2.size(); i++) Output.Vertices.push_back(inpG.Vertices[CandidatesLevel2[i]]); // Добавление всех кандидатов 2 уровня в аутпут

#ifdef DeleteOddVertsInSubgraphs
	while (Output.Vertices.size() > 5) DeleteVertex(Output, 0); // Удаление лишних вершин (т.к. граф может быть больше чем К5)
#endif // DeleteOddVertsInSubgraphs

	CleanAllIncidenceList(Output);
#ifdef DEBUG
	cout << "Succesfully returned K5-isomorphic subgraph.\n\n";
#endif
	return Output;
}

// Поиск подграфа, изоморфного К3,3
graph GetSubgraph_K33(graph& inpG) {
#ifdef DEBUG
	cout << "Trying to find K3,3-isomorphic subgraph.\n\n";
#endif

	vector<int> CandidatesLevel1; // 1 уровень кандидатов (по степени вершины >2)
	for (int i = 0; i < inpG.Vertices.size(); i++) {
		if (GetVertexDegree(inpG.Vertices[i]) > 2) {
			CandidatesLevel1.push_back(i);
#ifdef DEBUG
			cout << "Added vertex " << inpG.Vertices[i].name << " to the 1 level candidates.\n";
#endif
		}
	}
#ifdef DEBUG
	cout << "\n";
#endif
	if (CandidatesLevel1.size() < 6) { // Возвращаем пустой подграф если кандидатов 1 уровня < 6
		cout << "No K3,3-isomorphic subgraph found.\n\n";
		return {};
	}
	
	// ПОИСК ДОЛЬ ГРАФА СРЕДИ КАНДИДАТОВ 1 УРОВНЯ
	//
	vector<int> PartsSizes; // Список где указаны размеры доль (разметка списка ниже) --- ПРОВЕРИТЬ БУДЕТ ЛИ ЭТО ИСПОЛЬЗОВАТЬСЯ ДАЛЕЕ
	vector<int> Parts; // Список вершин, образующих графа
	for (int i = 0; i < CandidatesLevel1.size(); i++) {

#ifdef DeleteOddVertsInSubgraphs
		if (PartsSizes.size() == 2) break; // Если уже есть две доли то новые не формируем
#endif // DeleteOddVertsInSubgraphs

		if (count(Parts.begin(), Parts.end(), i)) continue; // Пропуск формирования доли с вершиной если она уже есть в какой-то доле
		
		vector<int> NeighboorsI;
		GetNeighboorVertices(inpG, i, NeighboorsI);
		sort(NeighboorsI.begin(), NeighboorsI.end());

		int CurrentPartSize = 0; // Счетчик для записи размера текущей доли
		vector<int> CurrentPart; // Доля, которую пытаемся сформировать на данной итерации
		for (int k = 0; k < CandidatesLevel1.size(); k++) {
			vector<int> NeighboorsK;
			GetNeighboorVertices(inpG, k, NeighboorsK);
			sort(NeighboorsK.begin(), NeighboorsK.end());
			if (NeighboorsI==NeighboorsK) {
				CurrentPart.push_back(k);
				CurrentPartSize++;
			}
		}
		if (CurrentPart.size() > 2) { // Для наших целей подходят только доли из 3+ вершин
			PartsSizes.push_back(CurrentPartSize);

			cout << "Part of size " << CurrentPartSize << " formed of vertices:\n";
			for (int k = 0; k < CurrentPartSize; k++) {
				cout << inpG.Vertices[CurrentPart[k]].name << "\n";
				Parts.push_back(CurrentPart[k]);
			}
			cout << "\n";
		}
		else {
			cout << "Failed forming part of size " << CurrentPartSize << "\n";
		}
	}

#ifdef DeleteOddVertsInSubgraphs
	for (int i = 0; i < PartsSizes.size(); i++) { // Удаление лишних вершин из доль (т.к. может быть > 3)
#ifdef DEBUG
		cout << "Deleting odd vertices from part " << i+1 << ":\n";
		int deletedCount = 0;
#endif
		while (PartsSizes[i]>3) {
			cout << "Deleted vertex " << inpG.Vertices[Parts[3*i]].name << "\n";
			Parts.erase(Parts.begin() + 3 * i);
			PartsSizes[i]--;
#ifdef DEBUG
			deletedCount++;
#endif
		}
#ifdef DEBUG
		cout << "Deleted " << deletedCount << " vertices\n\n";
#endif
	}
#endif // DeleteOddVertsInSubgraphs

	graph Output;
	for (int i = 0; i < Parts.size(); i++) Output.Vertices.push_back(inpG.Vertices[Parts[i]]);
	CleanAllIncidenceList(Output);
#ifdef DEBUG
	cout << "Succesfully returned K3,3-isomorphic subgraph.\n\n";
#endif
	return Output;
}

// ---TODO Удаление ребёр для превращения графа в планарный.
void MakePlanar(graph inpG) {
	// Алгоритм:
	// Возвращать К5, К3,3 БЕЗ УДАЛЕНИЯ ВЕРШИН!
	// Искать общие рёбра К5 и К3,3 если оба графа не пусты
	// Удалять рёбра из списка общих рёбер непланарных подграфов. Ищем минимум.
	// ---Иначе удалять ребро принадлежащее К5/К3,3
	// ---Проверять результат. Если граф все еще не планарен, удаляем ребро и еще одно.
	// ---Повторяем цикл пока граф не планарен

	graph Subgraph_K5 = GetSubgraph_K5(inpG);
	graph Subgraph_K33 = GetSubgraph_K33(inpG);
	
	if (!Subgraph_K5.empty() && !Subgraph_K33.empty()) {
		vector<int> commonEdges;
		GetCommonEdges(Subgraph_K5, Subgraph_K33, commonEdges);

		/// do while
	}
}

// MAIN

int main() {
	graph inp1;
	graph inp2;
	do {
		inp1 = GetGraphFromFile("test_input1.txt");
		inp2 = GetGraphFromFile("test_input2.txt");
		//ExcludeAllVertices(inp1);
		vector<int> common;
		GetCommonEdges(inp1, inp2, common);
		//MakePlanar(inp);
		//graph temp = GetSubgraph_K33(inp);
		//WriteGraphToFile(temp, "test2.txt");
		cout << "\n--- Press q to exit ---\n\n";
	} while (_getch() != 'q');
	return 0;
}
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <conio.h>
#include <algorithm>

#define DEBUG
//#define DEBUG_K5
#define DEBUG_K33
#define DEBUG2
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
graph GetGraphFromFile(string filename) { 
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
void WriteGraphToFile(graph& inpG, string filename) { 
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

// Чистка вектора от дубликатов
void CleanVector(vector<int>& inp) {
	auto end = inp.end();
	for (auto it = inp.begin(); it != end; ++it) end = remove(it + 1, end, *it);
	inp.erase(end, inp.end());
}

// Получение номеров смежных вершин для заданной в графе в данный список
void GetNeighboorVertices(graph& inpG, int inpV, vector<int>& NeighboorArray) { 
	for (int i = 0; i < inpG.Vertices.size(); i++) {
		if (i == inpV) continue;
			for (int m = 0; m < inpG.Vertices[i].IncidenceList.size(); m++) {
				if (count(inpG.Vertices[inpV].IncidenceList.begin(), inpG.Vertices[inpV].IncidenceList.end(), inpG.Vertices[i].IncidenceList[m])) {
					NeighboorArray.push_back(i);
				}
				/*for (int n = 0; n < inpG.Vertices[inpV].IncidenceList.size(); n++) { // ЛЕГАСИ
					if (inpG.Vertices[i].IncidenceList[m] == inpG.Vertices[inpV].IncidenceList[n] && i != inpV) {
						NeighboorArray.push_back(i);
					}
				}*/
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

// Получение номеров общих вершин данных графов (нумерация по первому графу)
void GetCommonVertices(graph& inpG1, graph& inpG2, vector<int>& commonVertices) {
	cout << "\n";
	for (int i = 0; i < inpG1.Vertices.size(); i++) {
		for (int k = 0; k < inpG2.Vertices.size(); k++) {
			if (inpG1.Vertices[i].name == inpG2.Vertices[k].name) {
				//sort(inpG1.Vertices[i].IncidenceList.begin(), inpG1.Vertices[i].IncidenceList.end()); ---TODO check if necessary
				//sort(inpG2.Vertices[k].IncidenceList.begin(), inpG2.Vertices[k].IncidenceList.end());
				//if (inpG1.Vertices[i].IncidenceList == inpG2.Vertices[k].IncidenceList) {
					commonVertices.push_back(i);
#ifdef DEBUG
					cout << "Found common vertex " << inpG1.Vertices[i].name << "\n";
#endif // DEBUG
				//}
			}
		}
	}
#ifdef DEBUG
	if (!commonVertices.size()) cout << "No common vertices found.\n";
	else cout << "Found " << commonVertices.size() << " common vertices\n\n";
#endif // DEBUG
}

// Получение имён рёбер, инцидентных данным вершинам
void GetCommonEdges(vertex& inpV1, vertex inpV2, vector<int>& commonEdgesArray) {
	for (int i = 0; i < inpV1.IncidenceList.size(); i++) {
		for (int k = 0; k < inpV2.IncidenceList.size(); k++) {
			if (inpV1.IncidenceList[i] == inpV2.IncidenceList[k]) {
				commonEdgesArray.push_back(inpV1.IncidenceList[i]);
			}
		}
	}
}

// Получение имён общих рёбер данных графов
void GetCommonEdges(graph& inpG1, graph& inpG2, vector<int>& commonEdgesArray) {
	if (inpG1.empty() || inpG2.empty()) return; // Если хотя бы один входной граф пустой, не тратим драгоценные ресурсы компутера
	vector<int> commonVertices;
	GetCommonVertices(inpG1, inpG2, commonVertices);
	for (int i=0; i < commonVertices.size(); i++) {
		for (int k = 0; k < commonVertices.size(); k++) {
			GetCommonEdges(inpG1.Vertices[commonVertices[i]], inpG2.Vertices[commonVertices[k]], commonEdgesArray);
		}
	}
	

#ifdef DEBUG
	if (!commonEdgesArray.size()) {
		cout << "No common edges found.\n";
		return;
	}
#endif // DEBUG
	CleanVector(commonEdgesArray); // Чистка от дубликатов
#ifdef DEBUG
	for (int i = 0; i < commonEdgesArray.size(); i++) {
		cout << "Found common edge " << commonEdgesArray[i] << "\n";
	}
	cout << "Found " << commonEdgesArray.size() << " common edges\n\n";
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

// Удаление ребра из графа (по имени ребра)
void DeleteEdge(graph& inpG, int inpE) {
	for (int i = 0; i < inpG.Vertices.size(); i++) {
		for (int k = 0; k < inpG.Vertices[i].IncidenceList.size(); k++) {
			if (inpG.Vertices[i].IncidenceList[k] == inpE) {
				inpG.Vertices[i].IncidenceList.erase(inpG.Vertices[i].IncidenceList.begin() + k);
				cout << "deleted edge number " << k+1 << " from vertex " << inpG.Vertices[i].name << "\n";
			}
		}
	}
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
				nonOddEdges.push_back(inpG.Vertices[inpV].IncidenceList[i]);
			}
		}
	}
	inpG.Vertices[inpV].IncidenceList.clear();
	for (int i = 0; i < nonOddEdges.size(); i++) inpG.Vertices[inpV].IncidenceList.push_back(nonOddEdges[i]);
}

void CleanAllIncidenceList(graph& inpG) {
	for (int i = 0; i < inpG.Vertices.size(); i++) {
		CleanIncidenceList(inpG, i);
	}
#ifdef DEBUG2
	cout << "Cleaned incidence lists for " << inpG.Vertices.size() << " vertices.\n\n";
#endif
}

// Поиск подграфа, изоморфного К5 (Вернее максимального подграфа, где содержатся несколько таковых)
graph GetSubgraph_K5(graph& inpG) { 
#ifdef DEBUG
	cout << "Trying to find K5-isomorphic subgraph.\n";
#endif

	vector<int> CandidatesLevel1; // 1 уровень кандидатов (по степени вершины >3)
	for (int i = 0; i < inpG.Vertices.size(); i++) {
		if (GetVertexDegree(inpG.Vertices[i]) > 3) {
			CandidatesLevel1.push_back(i);
#ifdef DEBUG_K5
			cout << "Vertex " << inpG.Vertices[i].name << "\t-> 1 level candidates.\n";
#endif
		}
	}
#ifdef DEBUG_K5
	cout << "\n";
#endif
	if (CandidatesLevel1.size() < 5) { // Возвращаем пустой подграф если кандидатов 1 уровня < 5
#ifdef DEBUG
		cout << "No K5-isomorphic subgraph found.\n\n";
#endif
		return {};
	}

	vector<int> CandidatesLevel2; // 2 уровень кандидатов (по смежности с 4 вершинами-кандидитами 1 уровня)
	for (int i = 0; i < CandidatesLevel1.size(); i++) {
		int NeighboorCandidatesLevel1 = 0;

		for (int k = 0; k < CandidatesLevel1.size(); k++) {
			if(Neighboors(inpG, i, k) && i!=k) NeighboorCandidatesLevel1++;
		}
		if (NeighboorCandidatesLevel1 > 3) {
#ifdef DEBUG_K5
			cout << "Vertex " << inpG.Vertices[CandidatesLevel1[i]].name << "\t-> 2 level candidates.\n";
#endif
			CandidatesLevel2.push_back(CandidatesLevel1[i]); // ---TODO По готовности функции от вектора кандидатов можно избавиться и писать сразу в аутпут и с ним работать
		}
	}
#ifdef DEBUG_K5
	cout << "\n";
#endif
	if (CandidatesLevel2.size() < 5) { // Возвращаем пустой подграф если кандидатов 2 уровня < 5
#ifdef DEBUG
		cout << "No K5-isomorphic subgraph found.\n\n";
#endif
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

// Поиск подграфа, изоморфного К3,3 (Вернее максимального подграфа, где содержатся несколько таковых)
graph GetSubgraph_K33(graph& inpG) { // НЕ ПРИБАВЛЯЕТ В CURRENTPARTSIZE ПОСЛЕДНЮЮ ЕДИНИЦУ
#ifdef DEBUG
	cout << "Trying to find K3,3-isomorphic subgraph.\n";
#endif
	vector<int> CandidatesLevel1; // 1 уровень кандидатов (по степени вершины >2)
	for (int i = 0; i < inpG.Vertices.size(); i++) {
		if (GetVertexDegree(inpG.Vertices[i]) > 2) {
			CandidatesLevel1.push_back(i);
#ifdef DEBUG_K33
			cout << "Vertex " << inpG.Vertices[i].name << "\t-> 1 level candidates.\n";
#endif
		}
	}
#ifdef DEBUG_K33
	cout << "\n";
#endif
	if (CandidatesLevel1.size() < 6) { // Возвращаем пустой подграф если кандидатов 1 уровня < 6
#ifdef DEBUG
		cout << "No K3,3-isomorphic subgraph found.\n\n";
#endif
		return {};
	}
	
	// ПОИСК ДОЛЬ ГРАФА СРЕДИ КАНДИДАТОВ 1 УРОВНЯ
	//
	vector<int> PartsSizes; // Список где указаны размеры доль (разметка списка ниже)
	vector<int> Parts; // Список вершин, образующих доли графа
	int CommonVertsOfIandK;
	for (int i = 0; i < CandidatesLevel1.size(); i++) {
		CommonVertsOfIandK = 0;
#ifdef DeleteOddVertsInSubgraphs
		if (PartsSizes.size() == 2) break; // Если уже есть две доли то новые не формируем
#endif // DeleteOddVertsInSubgraphs

		if (count(Parts.begin(), Parts.end(), i)) continue; // Пропуск формирования доли с вершиной если она уже есть в какой-то доле

		vector<int> CurrentPart; // Доля, которую пытаемся сформировать на данной итерации

		vector<int> NeighboorsI;
		GetNeighboorVertices(inpG, CandidatesLevel1[i], NeighboorsI);

		for (int k = 0; k < CandidatesLevel1.size(); k++) {
			CommonVertsOfIandK = 0;

			vector<int> NeighboorsK;
			GetNeighboorVertices(inpG, CandidatesLevel1[k], NeighboorsK);

			for (int m = 0; m < NeighboorsK.size(); m++) { // Считаем вершины, содержащиеся в обоих списках. Нам нужно хотя бы 3 совпадения.
				if (count(NeighboorsI.begin(), NeighboorsI.end(), NeighboorsK[m])) {
					//cout << "Found common vertex " << inpG.Vertices[NeighboorsK[m]].name << "\n";
					CommonVertsOfIandK++;
				}
			}
#ifdef DEBUG2
			cout << "For vertices " << inpG.Vertices[CandidatesLevel1[i]].name << " and " << inpG.Vertices[CandidatesLevel1[k]].name << " found " << CommonVertsOfIandK << "\n";
#endif // DEBUG2
			if (CommonVertsOfIandK>2) {
				CurrentPart.push_back(k);
			}
			cout << "Currentpart size " << CurrentPart.size() << "\n";

			for (int m = 0; m < CurrentPart.size(); m++) { //---TODO перезаписывает вершину вместо записи новой (не должно)
				for (int n = 0; n < CurrentPart.size(); n++) {
					if (Neighboors(inpG, CurrentPart[m], CurrentPart[n])) {
						CurrentPart.erase(CurrentPart.begin() + n);
					}
				}
			} // Очистка доль от вершин, которые связаны помиж собой
		}
		if (CurrentPart.size() > 2) { // Для наших целей подходят только доли из 3+ вершин
			PartsSizes.push_back(CurrentPart.size());

#ifdef DEBUG_K33
			cout << "Part of size " << CurrentPart.size() << " formed of vertices:\n";
#endif
			for (int k = 0; k < CurrentPart.size(); k++) {
#ifdef DEBUG_K33
				cout << inpG.Vertices[CurrentPart[k]].name << "\n";
#endif
				Parts.push_back(CurrentPart[k]);
			}
#ifdef DEBUG_K33
			cout << "\n";
#endif
		}
#ifdef DEBUG_K33
		else cout << "Failed forming part of size " << CurrentPart.size() << "\n";
#endif
	}
#ifdef DEBUG_K33
	cout << "\n";
#endif

#ifdef DeleteOddVertsInSubgraphs
	for (int i = 0; i < PartsSizes.size(); i++) { // Удаление лишних вершин из доль (т.к. может быть > 3)
#ifdef DEBUG
		cout << "Deleting odd vertices from part " << i+1 << ":\n";
		int deletedCount = 0;
#endif
		while (PartsSizes[i] > 3) {
			cout << "Deleted vertex " << inpG.Vertices[Parts[3 * i]].name << "\n";
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
	if (PartsSizes.size() < 2) {
#ifdef DEBUG
		cout << "No K3,3-isomorphic subgraph found.\n\n";
#endif
		return {}; // Если меньше двух доль ничего не возвращаем
	}
	graph Output;
	for (int i = 0; i < Parts.size(); i++) Output.Vertices.push_back(inpG.Vertices[Parts[i]]);
	CleanAllIncidenceList(Output);
#ifdef DEBUG
	if (Output.Vertices.size()) {
		cout << "Succesfully returned K3,3-isomorphic subgraph.\n\n";
	} else cout << "No K3,3-isomorphic subgraph found.\n\n";
#endif
	Output.DisplayAllIncidenceList();
	return Output;
}

// Проверка является ли граф планарным
bool Planar(graph& inpG) {
	if (GetSubgraph_K5(inpG).empty() && GetSubgraph_K33(inpG).empty()) return 1; else return 0;
}

// Удаление ребёр для превращения графа в планарный.
void MakePlanar(graph inpG) {
	cout << "Trying to make graph planar\n";

	ExcludeAllVertices(inpG);
	graph Subgraph_K5 = GetSubgraph_K5(inpG);
	graph Subgraph_K33 = GetSubgraph_K33(inpG);
	if (Subgraph_K5.empty() && Subgraph_K33.empty()) {
		cout << "Graph is already planar\n\n";
		return;
	}

#ifdef DEBUG
	cout << "Trying find common edges for two non-planar subgraphs\n";
#endif
	vector<int> potentialAnswer; // Массив потенциально подходящих нам рёбер. В первую очередь проверяются те, что общие для двух непланарных подграфов (при наличии таковых)	
	GetCommonEdges(Subgraph_K5, Subgraph_K33, potentialAnswer);
	for (int i=0; i < Subgraph_K5.Vertices.size(); i++) {
		for (int k=0; k < Subgraph_K5.Vertices[i].IncidenceList.size(); k++) {
			potentialAnswer.push_back(Subgraph_K5.Vertices[i].IncidenceList[k]);
		}
	}
	for (int i=0; i < Subgraph_K33.Vertices.size(); i++) {
		for (int k=0; k < Subgraph_K33.Vertices[i].IncidenceList.size(); k++) {
			potentialAnswer.push_back(Subgraph_K33.Vertices[i].IncidenceList[k]);
		}
	}
	CleanVector(potentialAnswer);

#ifdef DEBUG
	cout << "Potential edges list: ";
	for (int i = 0; i < potentialAnswer.size(); i++) {
		cout << potentialAnswer[i] << " ";
	}
	cout << "\n\n";
#endif
		int iteration = 0;
		int maxiteration = potentialAnswer.size();
		vector<int> needtodelete; // Массив рёбер, удаление которых по отдельности недостаточно для планарности
		graph t_Subgraph_K5; 
		graph t_Subgraph_K33; // Временные графы, используемые для проверки планарности после удаления рёбер в циклах

		do {
#ifdef DEBUG
			cout << "Now on iteration " << iteration + 1 << " (max iterations " << maxiteration << ")\n";
#endif
			for (int i = 0; i < needtodelete.size(); i++) { // Удаление вышеупомянутых рёбер
				DeleteEdge(Subgraph_K5, needtodelete[i]);	
				DeleteEdge(Subgraph_K33, needtodelete[i]);
			}

			bool isReadyK5=true, isReadyK33=true; // Проверка планарны ли графы после удаления рёбер
			if (!Subgraph_K5.empty()) {
				for (int i = 0; i < potentialAnswer.size(); i++) { // Разбивка на 2 цикла для оптимизации
					t_Subgraph_K5 = Subgraph_K5;
#ifdef DEBUG
					cout << "Deleted edge " << potentialAnswer[i] << " (trying to make K5 planar)\n";
#endif
					DeleteEdge(t_Subgraph_K5, potentialAnswer[i]);
					if (GetSubgraph_K5(t_Subgraph_K5).empty()) {
						isReadyK5 = true;
#ifdef DEBUG
						cout << "Made K5 planar\n";
						cout << "Added edge " << potentialAnswer[i] << " to the answer\n";
#endif
						needtodelete.push_back(potentialAnswer[i]);
						break;
					}
					isReadyK5 = false;
#ifdef DEBUG
					cout << "Did not make K5 planar\n";
#endif
				}
			}
			if (/*!isReadyK5 && */ !Subgraph_K33.empty()) {
				for (int i = 0; i < potentialAnswer.size(); i++) {
					t_Subgraph_K33 = Subgraph_K33;
#ifdef DEBUG
					cout << "Deleted edge " << potentialAnswer[i] << " (trying to make K33 planar)\n";
#endif
					DeleteEdge(t_Subgraph_K33, potentialAnswer[i]);

					if (GetSubgraph_K33(t_Subgraph_K33).empty()) {
						isReadyK33 = true;
#ifdef DEBUG
						cout << "Made K33 planar\n";
						cout << "Added edge " << potentialAnswer[i] <<" to the answer\n";
#endif
						needtodelete.push_back(potentialAnswer[i]);
						break;
					}
					isReadyK33 = false;
#ifdef DEBUG
					cout << "Did not make K33 planar\n";
#endif
				}
			}
			if (isReadyK5 && isReadyK33) {
#ifdef DEBUG
				cout << "Made graph planar\n\n";
#endif
				break;
			}
#ifdef DEBUG
			cout << "Graph in not planar yet\n";
			cout << "Added " << potentialAnswer[0] << " to the answer\n";
#endif
			needtodelete.push_back(potentialAnswer[0]); // Перенос в массив недостаточных ребра
			potentialAnswer.erase(potentialAnswer.begin());
			CleanVector(needtodelete);
			iteration++;
		} while (iteration<=maxiteration); // Принудительно завершаем проверку если проверили все рёбра и не помогло

		CleanVector(needtodelete);
		cout << "Minimal list of edges to be deleted: ";
		for (int i = 0; i < needtodelete.size(); i++) {
			cout << needtodelete[i] << " ";
		}
		cout << "(" << needtodelete.size() << " edges)\n\n";
}

// MAIN

int main() {
	do {
		graph inp;
		char filename[] = { "test_input4.txt" };
		
		cout << "\n--- Pls input example number ---\n\n";
		
		/*for (int i = 0; i < 5; i++) {
			filename[10]=char(i+49);
			cout << filename << "\n";
			inp = GetGraphFromFile(filename);
			MakePlanar(inp);
		}*/

		filename[10] = _getch();
		inp = GetGraphFromFile(filename);
		MakePlanar(inp);
		

		/*inp = GetGraphFromFile(filename);
		vector<int> common;
		GetNeighboorVertices(inp, 1, common);
		*/

		cout << "\n--- Press q to exit ---\n\n";
	} while (_getch() != 'q');
	return 0;
}
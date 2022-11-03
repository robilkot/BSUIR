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
//#define DEBUG2
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
			cout << "Ingnored invalid edge number input!\n";
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
	while (getline(input, temp)) 	Output.Vertices.push_back(GetVertexFromString(temp));
	input.close();

	cout << "Opened file " << filename << "\n";
	return Output;
}

// Запись графа в файл
void WriteGraphToFile(graph& inpG, string filename) { 
	if (inpG.empty()) {
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
			}
	}
}

// Проверка, являются ли данные вершины смежными
bool Neighboors(graph& inpG, int inpV1, int inpV2) {
	vector<int> NeighboorCheck;
	GetNeighboorVertices(inpG, inpV1, NeighboorCheck);
	return count(NeighboorCheck.begin(), NeighboorCheck.end(), inpV2); // Проходим по массиву соседей вершины 1 и ищем там вершину 2
}

// Проверка на возможность исключения вершины без нарушения гомеоморфизма исходному графу
bool CanBeExcluded(graph& inpG, int inpV) { 
	vector<int> check;
	GetNeighboorVertices(inpG, inpV, check);
	if (check.size() != 2 || Neighboors(inpG, check[0], check[1])) return false; // Если степень вершины не 2, то исключить нельзя
																				// Если две смежные вершины данной - смежны, тоже исключить нельзя (цикл)
	return true;
}

// Получение номеров общих вершин данных графов (нумерация по первому графу)
void GetCommonVertices(graph& inpG1, graph& inpG2, vector<int>& commonVertices) {
	for (int i = 0; i < inpG1.Vertices.size(); i++) {
		for (int k = 0; k < inpG2.Vertices.size(); k++) {
			if (inpG1.Vertices[i].name == inpG2.Vertices[k].name) {
				//sort(inpG1.Vertices[i].IncidenceList.begin(), inpG1.Vertices[i].IncidenceList.end()); // Если для поиска общих вершин также нужно учитывать и их СИ
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

#ifdef DEBUG2
		cout << "Excluding vertex " << inpG.Vertices[inpV].name << ".\tDone.\n";
#endif
		inpG.Vertices.erase(inpG.Vertices.begin()+inpV);
		return 1;
	}
	else return 0;
}

// Исключение всех возможных вершин из данного графа
void ExcludeAllVertices(graph& inpG) { 
	bool isReady;
	do {
		for (int i = 0; i < inpG.Vertices.size(); ) {
			if (!ExcludeVertex(inpG, i)) i++; // Удаление всех возможных вершин
		}

		isReady = true;
		for (int i = 0; i < inpG.Vertices.size(); i++) { // Проверка все ли удалено
			CanBeExcluded(inpG, i) ? isReady = false: NULL;
		}
	} while (!isReady); 
}

// Получение степени вершины
int GetVertexDegree(vertex& inpV) { 
	return inpV.IncidenceList.size();
}

// Удаление вершины и инцидентных ей ребер из графа (НЕ ИСКЛЮЧЕНИЕ ВЕРШИНЫ!)
void DeleteVertex(graph& inpG, int inpV) { 
	vector<int> neighboors, commonEdges;
	GetNeighboorVertices(inpG, inpV, neighboors);
	for (int i = 0; i < neighboors.size(); i++) {
		GetCommonEdges(inpG.Vertices[neighboors[i]], inpG.Vertices[inpV], commonEdges);
		for (int k = 0; k < commonEdges.size(); k++) { // Для каждой смежной вершины удаляем из её СИ номер ребра, инцидентного удаляемой вершине
			inpG.Vertices[neighboors[i]].IncidenceList.erase(inpG.Vertices[neighboors[i]].IncidenceList.begin()+GetEdgeNumber(inpG.Vertices[neighboors[i]],commonEdges[k]));
		}
		commonEdges.clear();
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
#ifdef DEBUG2
				cout << "deleted edge number " << k + 1 << " from vertex " << inpG.Vertices[i].name << "\n";
#endif 
			}
		}
	}
}

// Очистка СИ вершин от ребёр, не ведущих ни в одну вершину ---TODO review
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
	for (int i = 0; i < inpG.Vertices.size(); i++)	CleanIncidenceList(inpG, i);
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

	graph Output; // 2 уровень кандидатов (по смежности с 4 вершинами-кандидитами 1 уровня), сразу пишутся в аутпут

	for (int i = 0; i < CandidatesLevel1.size(); i++) {
		int NeighboorCandidatesLevel1 = 0;

		for (int k = 0; k < CandidatesLevel1.size(); k++) {
			if(Neighboors(inpG, i, k) && i!=k) NeighboorCandidatesLevel1++;
		}
		if (NeighboorCandidatesLevel1 > 3) {
#ifdef DEBUG_K5
			cout << "Vertex " << inpG.Vertices[CandidatesLevel1[i]].name << "\t-> 2 level candidates.\n";
#endif
			Output.Vertices.push_back(inpG.Vertices[CandidatesLevel1[i]]); // ---TODO По готовности функции от вектора кандидатов можно избавиться и писать сразу в аутпут и с ним работать
		}
	}
#ifdef DEBUG_K5
	cout << "\n";
#endif
	if (Output.Vertices.size() < 5) { // Возвращаем пустой подграф если кандидатов 2 уровня < 5
#ifdef DEBUG
		cout << "No K5-isomorphic subgraph found.\n\n";
#endif
		return {};
	}

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
graph GetSubgraph_K33(graph& inpG) {
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
	graph candidates1;
	for (int i = 0; i < CandidatesLevel1.size(); i++) candidates1.Vertices.push_back(inpG.Vertices[CandidatesLevel1[i]]);


	graph Output;
	// ПОИСК ДОЛЬ ГРАФА СРЕДИ КАНДИДАТОВ 1 УРОВНЯ
	//
	vector<int> PartsSizes; // Список где указаны размеры доль (разметка списка ниже)
	vector<int> Parts; // Список вершин, образующих доли графа
	int CommonVertsOfIandK;
	
	for (int i = 0; i < CandidatesLevel1.size(); i++) {
		if (count(Parts.begin(), Parts.end(), CandidatesLevel1[i])) continue; // Пропуск если вершина уже есть в доле

		
		vector<int> CurrentPart; // Список вершин в доле, которую формируем
		CurrentPart.push_back(i); // Добавляем в текущую долю И вершину
		vector<int> NeighBoorsI;
		GetNeighboorVertices(inpG, i, NeighBoorsI);
		for (int k = 0; k < CandidatesLevel1.size(); k++) {
			if (i == k) continue; // Пропуск если смотрим одинаковые вершины
			if (count(Parts.begin(), Parts.end(), CandidatesLevel1[k])) continue;
			CommonVertsOfIandK = 0;
			cout << "Looking at vertices " << inpG.Vertices[CandidatesLevel1[i]].name << " and " << inpG.Vertices[CandidatesLevel1[k]].name << "\n";
			vector<int> NeighboorsK;
			GetNeighboorVertices(inpG, k, NeighboorsK);
			for (int m = 0; m < NeighboorsK.size(); m++) { // Если в списке соседей И нашелся сосед К то увеличиваем счтчик
				if (count(NeighBoorsI.begin(), NeighBoorsI.end(), NeighboorsK[m])) { // ТУДУ ЧТОБЫ ОБА СОСЕДА БЫЛИ В КАНДИДАТАХ А НЕ ТОЛЬКО В ИНПУТЕ
					//cout << "found common vertex\n";
					CommonVertsOfIandK++;
				}
			}
			cout << "found " << CommonVertsOfIandK << " common vertices\n";
			if (CommonVertsOfIandK > 2) CurrentPart.push_back(k);
		}

		if (CurrentPart.size() < 3) {
			cout << "Failed forming part of size " << CurrentPart.size() << "\n";
		}
		else {
			for (int k = 0; k < CurrentPart.size(); k++) Parts.push_back(CurrentPart[k]); // Записываем полученную долю в общий список
			PartsSizes.push_back(CurrentPart.size());
			cout << "Wrote part of size " << CurrentPart.size() << "\n";
		}
	}

	if (PartsSizes.size() < 2) {
		cout << "No K3,3-isomorphic subgraph found.\n\n";
		return {}; // Если меньше двух доль ничего не возвращаем
	} else {
		for(int i = 0; i < Parts.size();i++) Output.Vertices.push_back(candidates1.Vertices[Parts[i]]);
	}

	//CleanAllIncidenceList(Output); // Чистим СИ от остатков оригинального графа

#ifdef DEBUG
	if (Output.Vertices.empty()) {
		cout << "No K3,3-isomorphic subgraph found.\n\n";
	} else 	cout << "Succesfully returned K3,3-isomorphic subgraph.\n\n";
#endif
#ifdef DEBUG_K33
	Output.DisplayAllIncidenceList();
#endif
	//system("pause");
	return Output;
}

// Проверка является ли граф планарным
bool Planar(graph& inpG) {
	if (GetSubgraph_K5(inpG).empty() && GetSubgraph_K33(inpG).empty()) return 1; else return 0;
}

// Удаление ребёр для превращения графа в планарный.
void MakePlanar(graph& input) {
	cout << "Trying to make graph planar\n";
	graph inpG = input; // Создаём граф внутри функции, из которого будем исключать вершины и делать иные вещи для поиска ответа. Оригинальный же затронем только удалением рёбер.
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
	vector<int> potentialAnswer; // Массив рёбер, которые будем пробовать удалить. В первую очередь - общие для двух непланарных подграфов рёбра.
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
		vector<int> needtodelete; // Массив рёбер, удаление которых необходимо для планарности
		graph t_Subgraph_K5; 
		graph t_Subgraph_K33; // Временные графы, используемые для проверки планарности после удаления рёбер в циклах

		do {
#ifdef DEBUG
			cout << "Now on iteration " << iteration + 1 << " (max iterations " << maxiteration << ")\n\n";
#endif
			for (int i = 0; i < needtodelete.size(); i++) { // Удаление вышеупомянутых рёбер из подграфов
				DeleteEdge(Subgraph_K5, needtodelete[i]);
				DeleteEdge(Subgraph_K33, needtodelete[i]);
			}

			bool isReadyK5 = true, isReadyK33 = true; // Проверка планарны ли графы после удаления рёбер

		if (!Subgraph_K5.empty()) {
			for (int i = 0; i < potentialAnswer.size(); i++) { // В первом цикле пробуем устранить К5
				t_Subgraph_K5 = Subgraph_K5;
#ifdef DEBUG
				cout << "Deleted edge " << potentialAnswer[i] << " (trying to make K5 planar)\n";
#endif
				DeleteEdge(t_Subgraph_K5, potentialAnswer[i]);
				if (GetSubgraph_K5(t_Subgraph_K5).empty()) {
					isReadyK5 = true;
#ifdef DEBUG
					cout << "Made K5 planar\n";
					cout << "Added edge " << potentialAnswer[i] << " to the answer\n\n";
#endif
					needtodelete.push_back(potentialAnswer[i]);
					DeleteEdge(input, potentialAnswer[i]);
					break;
				}
				else {
					isReadyK5 = false;
#ifdef DEBUG
					cout << "Did not make K5 planar\n";
#endif
				}
			}
		}

		if (!Subgraph_K33.empty()) {
			for (int i = 0; i < potentialAnswer.size(); i++) { // Во втором цикле пробуем устранить К3,3
				t_Subgraph_K33 = Subgraph_K33;
#ifdef DEBUG
				cout << "Deleted edge " << potentialAnswer[i] << " (trying to make K33 planar)\n";
#endif
				DeleteEdge(t_Subgraph_K33, potentialAnswer[i]);
				if (GetSubgraph_K33(t_Subgraph_K33).empty()) {
					isReadyK33 = true;
#ifdef DEBUG
					cout << "Made K33 planar\n";
					cout << "Added edge " << potentialAnswer[i] << " to the answer\n\n";
#endif
					needtodelete.push_back(potentialAnswer[i]);
					DeleteEdge(input, potentialAnswer[i]);
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
			DeleteEdge(input, potentialAnswer[0]);
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

		filename[10] = _getch();
		inp = GetGraphFromFile(filename);
		MakePlanar(inp);
		WriteGraphToFile(inp, "test_output.txt");

		cout << "\n--- Press q to exit ---\n\n";
	} while (_getch() != 'q');
	return 0;
}
#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct Vertex
{
	vector<int> Incidence;
	string name;

	void DisplayIncidence() {
		cout << "\n For vertex " << name << ": ";
		for (int i = 0; i < Incidence.size(); i++) cout << Incidence[i] << " ";
	}
};

struct Graph
{
	vector<Vertex> Vertices;

	void DisplayAllIncidence() {
		for (int i = 0; i < Vertices.size(); i++) Vertices[i].DisplayIncidence();
	}
};

int main() {
	Vertex first{ {8,2}, "test1" };

	Vertex second{ {1,2,4,5}, "test2"};

	Graph Gfirst{{first,second}};

	Gfirst.DisplayAllIncidence();
	return 0;
}
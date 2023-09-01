#include "LW1_Set.h"
#include <string>
#include <vector>

using std::string;
using std::vector;

// todo: наследовать класс с одним элементом?
class Set {
private:
	bool isEmpty = true;
	bool isSingleElement = false;

	char singleElement = 0;
	vector<Set> elements;

	Set(char element) {
		this->singleElement = element;
		isSingleElement = true;
		isEmpty = false;
	}
public:
	Set(string setNotation) {

	};
	Set(char* setNotation) {

	};

	bool empty() {
		return isEmpty;
	}

	int cardinality() {
		return isSingleElement ? 1 : elements.size();
	}

	void push(char element) {

	}

	void pop(char element) {

	}

	bool operator [](char element) {

	}

	Set operator + (const Set& set) const {

	}

	Set operator * (const Set& set) const {

	}

	Set boolean() {

	}
};
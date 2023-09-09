#include "CantorSet.h"

using std::string;
using std::set;

bool CantorSet::empty() const {
	return isEmpty;
}
bool CantorSet::isSingleElement() const {
	return !isEmpty && !elements.size();
}
size_t CantorSet::cardinality() const {
	return elements.size();
}

void CantorSet::clear() {
	isEmpty = true;
	data = 0;
	elements.clear();
}

void CantorSet::push() {
	elements.emplace(CantorSet());
	isEmpty = false;
}
void CantorSet::push(char element) {
	elements.emplace(CantorSet(element));
	isEmpty = false;
}
void CantorSet::push(const string& element) {
	elements.emplace(CantorSet(element));
	isEmpty = false;
}
void CantorSet::push(const char* const element) {
	elements.emplace(CantorSet(element));
	isEmpty = false;
}
void CantorSet::push(const CantorSet& element) {
	elements.emplace(element);
	isEmpty = false;
}

void CantorSet::pop(const char* const element) {
	CantorSet toDelete(element);
	auto equals = [&](const auto& element) { return element == toDelete; };
	std::erase_if(elements, equals);

	if (elements.empty()) isEmpty = true;
}
void CantorSet::pop(const string& element) {
	CantorSet toDelete(element);
	auto equals = [&](const auto& element) { return element == toDelete; };
	std::erase_if(elements, equals);

	if (elements.empty()) isEmpty = true;
}
void CantorSet::pop(const CantorSet& toDelete) {
	auto equals = [&](const auto& element) { return element == toDelete; };
	std::erase_if(elements, equals);

	if (elements.empty()) isEmpty = true;
}

CantorSet CantorSet::boolean() const {
	CantorSet result;

	size_t totalCombinations = pow(2, cardinality());

	for (size_t combinationIndex = 0; combinationIndex < totalCombinations; combinationIndex++) {
		CantorSet currentCombination;

		for (size_t bitMask = combinationIndex, bitShift = 0; bitMask > 0; bitMask >>= 1, bitShift++) {
			if (bitMask & 1) {
				auto it = elements.begin();
				std::advance(it, bitShift);
				currentCombination.push(*it);
			}
		}

		result.push(currentCombination);
	}

	return result;
}

CantorSet::CantorSet() {};
CantorSet::CantorSet(char element) {
	data = element;
	isEmpty = false;
};
CantorSet::CantorSet(const char* const element) {
	string setNotation(element);
	*this = CantorSet(setNotation);
};
CantorSet::CantorSet(string element) {
	if (element.length() == 1) {
		*this = CantorSet(element[0]);
		return;
	}

	size_t openBrackets = std::count(element.begin(), element.end(), '{');
	size_t closeBrackets = std::count(element.begin(), element.end(), '}');
	if (openBrackets != closeBrackets) throw std::invalid_argument("Number of brackets doesn;t match");

	*this = parseString(element);
};

CantorSet CantorSet::parseString(string& element) const {
	CantorSet result;

	if (element.size() < 2) return result;
	if (element[0] == '{') element.erase(0, 1);

	while (!element.empty()) {
		switch (element[0]) {
		default: {
			result.push(element[0]);
			element.erase(0, 1);
			break;
		}
		case '{': {
			CantorSet subset = parseString(element);
			result.push(subset);
			break;
		}
		case '}': {
			element.erase(0, 1);
			return result;
		}
		case ',': {
			element.erase(0, 1);
			break;
		}
		}
	}
}

string CantorSet::toString() const {
	string result;

	if (isSingleElement()) {
		result = data;
		return result;
	}

	if (isEmpty) {
		return "{}";
	}

	result += '{';
	for (const auto& element : this->elements)
		result += element.toString() + ',';

	result.pop_back(); // erase last comma
	result += '}';

	return result;
}

bool CantorSet::operator < (const CantorSet& set) const {
	int cardinality1 = cardinality(),
		cardinality2 = set.cardinality();

	if (cardinality1 == cardinality2) {
		if (isSingleElement() && set.isSingleElement())
			return data < set.data;

		return elements < set.elements;
	}

	return cardinality1 < cardinality2;
}
bool CantorSet::operator == (const CantorSet& set) const {
	return  elements == set.elements &&
		data == set.data &&
		isEmpty == set.isEmpty;
}
bool CantorSet::operator [](const string& element) const {
	CantorSet toFind(element);
	return elements.count(toFind);
}
bool CantorSet::operator [](const char* const element) const {
	CantorSet toFind(element);
	return elements.count(toFind);
}
bool CantorSet::operator [](const CantorSet& element) const {
	return elements.count(element);
}

CantorSet CantorSet::operator + (const CantorSet& set) const {
	CantorSet result = *this;

	for (const auto& element : set.elements)
		result.push(element);

	return result;
}
CantorSet& CantorSet::operator += (const CantorSet& set) {
	for (const auto& element : set.elements)
		push(element);

	return *this;
}

CantorSet CantorSet::operator - (const CantorSet& set) const {
	CantorSet result = *this;

	for (const auto& element : set.elements)
		result.pop(element);

	return result;
}
CantorSet& CantorSet::operator -= (const CantorSet& set) {
	for (const auto& element : set.elements)
		pop(element);

	return *this;
}

CantorSet CantorSet::operator * (const CantorSet& set) const {
	CantorSet result;

	for (const auto& element : elements) {
		if (set[element])
			result.push(element);
	}

	return result;
}
CantorSet& CantorSet::operator *= (const CantorSet& set) {
	CantorSet currentSet = *this;
	clear();

	for (const auto& element : currentSet.elements) {
		if (set[element])
			push(element);
	}

	return *this;
}

std::istream& operator>>(std::istream& cin, CantorSet& set)
{
	string input;
	cin >> input;
	set = CantorSet(input);
	return cin;
}
std::ostream& operator<<(std::ostream& cout, CantorSet& set)
{
	cout << set.toString();
	return cout;
}
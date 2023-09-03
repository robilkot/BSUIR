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
	this->isEmpty = true;
	this->data = 0;
	this->offset = 0;
	this->elements.clear();
}

void CantorSet::push() {
	this->elements.emplace(CantorSet());
	this->isEmpty = false;
}
void CantorSet::push(char element) {
	this->elements.emplace(CantorSet(element));
	this->isEmpty = false;
}
void CantorSet::push(const string& element) {
	this->elements.emplace(CantorSet(element));
	this->isEmpty = false;
}
void CantorSet::push(const CantorSet& element) {
	this->elements.emplace(element);
	this->isEmpty = false;
}

void CantorSet::pop(const string& element) {
	CantorSet toDelete(element);
	auto equals = [&](auto const& element) { return element == toDelete; };
	std::erase_if(this->elements, equals);

	if (this->elements.size() == 0) this->isEmpty = true;
}
void CantorSet::pop(const CantorSet& toDelete) {
	auto equals = [&](auto const& element) { return element == toDelete; };
	std::erase_if(this->elements, equals);

	if (this->elements.size() == 0) this->isEmpty = true;
}

CantorSet CantorSet::boolean() const {
	CantorSet result;

	size_t totalCombinations = pow(2, this->cardinality());

	for (size_t combinationIndex = 0; combinationIndex < totalCombinations; combinationIndex++) {
		CantorSet currentCombination;

		for (size_t bitMask = combinationIndex, bitShift = 0; bitMask > 0; bitMask >>= 1, bitShift++) {
			if (bitMask & 1) {
				auto it = this->elements.begin();
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
	this->data = element;
	this->isEmpty = false;
};
CantorSet::CantorSet(string element) {
	if (element.length() == 1) {
		*this = CantorSet(element[0]);
		return;
	}

	for (int i = 1; i < element.size(); i++, this->offset++) {
		switch (element[i]) {
		default: {
			this->push(element[i]);
			break;
		}
		case '{': {
			CantorSet subset(element.substr(i));
			this->push(subset);
			this->offset += subset.offset;
			i += subset.offset;
			break;
		}
		case '}': {
			this->offset++; // needed because cycle increment doesn't work after returning
			return;
		}
		case ',': break;
		}
	}
};

string CantorSet::toString() const {
	string result;

	if (this->isSingleElement()) {
		result = this->data;
		return result;
	}
	if (this->isEmpty)
		return "{}";

	result += '{';
	for (const auto& element : this->elements)
		result += element.toString() + ',';

	result.pop_back(); // erase last comma
	result += '}';

	return result;
}

bool CantorSet::operator < (const CantorSet& set) const {
	int cardinality1 = this->cardinality(),
		cardinality2 = set.cardinality();

	if (cardinality1 == cardinality2) {
		if (this->isSingleElement() && set.isSingleElement())
			return this->data < set.data;

		return this->elements < set.elements;
	}

	return cardinality1 < cardinality2;
}
bool CantorSet::operator == (const CantorSet& set) const {
	return  this->elements == set.elements &&
		this->data == set.data &&
		this->isEmpty == set.isEmpty;
}
bool CantorSet::operator [](string element) const {
	CantorSet toFind(element);
	return this->elements.count(toFind);
}
bool CantorSet::operator [](const CantorSet& element) const {
	return this->elements.count(element);
}

CantorSet CantorSet::operator + (const CantorSet& set) const {
	CantorSet result = *this;

	for (const auto& element : set.elements)
		result.push(element);

	return result;
}
CantorSet& CantorSet::operator += (const CantorSet& set) {
	for (const auto& element : set.elements)
		this->push(element);

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
		this->pop(element);

	return *this;
}

CantorSet CantorSet::operator * (const CantorSet& set) const {
	CantorSet result;

	for (const auto& element : this->elements) {
		if (set[element])
			result.push(element);
	}

	return result;
}
CantorSet& CantorSet::operator *= (const CantorSet& set) {
	CantorSet currentSet = *this;
	this->clear();

	for (const auto& element : currentSet.elements) {
		if (set[element])
			this->push(element);
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
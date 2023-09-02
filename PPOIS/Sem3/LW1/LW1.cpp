#include <iostream>
#include <string>
#include <set>

using std::string;
using std::set;

class CantorSet {
public:
	mutable bool isEmpty = true;
	char data = 0;
	mutable set<CantorSet> elements;
	unsigned int offset = 0;

	bool isSingleElement() const {
		return !isEmpty && !elements.size();
	}

	bool empty() const {
		return isEmpty;
	}

	int cardinality() const {
		if (isEmpty) return 0;
		if (!elements.empty()) return elements.size();
		return 1;
	}

	void push() const {
		this->elements.emplace(CantorSet());
		this->isEmpty = false;
	}
	void push(char element) const {
		this->elements.emplace(CantorSet(element));
		this->isEmpty = false;
	}
	void push(string element) const {
		this->elements.emplace(CantorSet(element));
		this->isEmpty = false;
	}
	void push(CantorSet element) const {
		this->elements.emplace(element);
		this->isEmpty = false;
	}

	void pop(string element) {
		CantorSet toDelete(element);
		auto equals = [&](auto const& element) { return element == toDelete; };
		std::erase_if(this->elements, equals);

		if (this->elements.size() == 0) this->isEmpty = true;
	}

	CantorSet() {};
	CantorSet(char element) { // надо private потому что это элемент а не множество?
		this->data = element;
		this->isEmpty = false;
	};
	CantorSet(string element) {
		if (element.length() == 1) {
			*this = CantorSet(element[0]);
			return;
		}

		for (int i = 1; i < element.size(); i++) {
			switch (element[i]) {
			default: {
				this->push(element[i]);
				this->offset++;
				break;
			}
			case '{': {
				CantorSet subset(element.substr(i));
				this->push(subset);
				this->offset += subset.offset + 1;
				i += subset.offset + 1;
				break;
			}
			case '}': {
				this->offset++;
				return;
			}
			case ',': {
				this->offset++;
				break;
			}
			}
		}
	};

	bool operator < (const CantorSet& set) const {
		int cardinality1 = this->cardinality(),
			cardinality2 = set.cardinality();

		if (cardinality1 != cardinality2)
			return this->cardinality() < set.cardinality();

		return this->data * !this->isEmpty < set.data * !set.isEmpty;
	}
	bool operator == (const CantorSet& set) const {
		return this->elements == set.elements &&
			this->data == set.data &&
			this->isEmpty == set.isEmpty;
	}

	bool operator [](string element) {
		CantorSet toFind(element);
		return this->elements.count(toFind);
	}
	bool operator [](CantorSet element) {
		return this->elements.count(element);
	}

	// А копирование надо вообще?
	//CantorSet& operator = (const CantorSet set) {
	//	this->elements = set.elements;
	//	this->isEmpty = set.isEmpty;
	//	this->offset = set.offset;
	//	this->data = set.data;
	//	return *this;
	//}

	// Операторы не працюють
	//
	/*CantorSet operator + (const CantorSet& set) const {
		CantorSet result = *this;

		for (auto it = set.elements.begin(); it != set.elements.end(); it++)
			result.push(*it);

		result.isEmpty = this->isEmpty || set.isEmpty;
		return result;
	}

	CantorSet& operator += (const CantorSet& set) {
		for (const auto& element : set.elements)
			this->push(element);

		return *this;
	}

	CantorSet operator * (const CantorSet& set) const {
		CantorSet result;

		for (auto it = set.elements.begin(); it != set.elements.end(); it++)
			if(this->elements.count(*it)) result.elements.emplace(*it);

		result.isEmpty = this->isEmpty && set.isEmpty;
		return result;
	}*/

	//CantorSet boolean() { }
};

int main() {
	string set;

	set = "{a,{b,c}}";
	CantorSet test1(set);

	set = "{a,{b,{c,d}}}";
	CantorSet test2(set);

	// Я обязательно выживу
	//test1 += test2;

	return 0;
}
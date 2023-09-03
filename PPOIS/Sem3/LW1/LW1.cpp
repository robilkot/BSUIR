#include <iostream>
#include <string>
#include <set>

using std::string;
using std::set;
using std::cout;
using std::cin;

class CantorSet {
public:
	mutable bool isEmpty = true;
	char data = 0;
	size_t offset = 0;
	mutable set<CantorSet> elements;

	bool empty() const {
		return isEmpty;
	}
	bool isSingleElement() const {
		return !isEmpty && !elements.size();
	}
	size_t cardinality() const {
		return elements.size();
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
	void pop(CantorSet toDelete) {
		auto equals = [&](auto const& element) { return element == toDelete; };
		std::erase_if(this->elements, equals);

		if (this->elements.size() == 0) this->isEmpty = true;
	}

	CantorSet boolean() {
		CantorSet result;

		size_t resultCardinality = pow(2, this->cardinality());

		// Я не хочу рекурсию писать(((

		return result;
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

	string toString() const {
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

	bool operator < (const CantorSet& set) const {
		int cardinality1 = this->cardinality(),
			cardinality2 = set.cardinality();

		if (cardinality1 == cardinality2) {
			if (this->isSingleElement() && set.isSingleElement())
				return this->data < set.data;

			return this->elements < set.elements;
		}

		return cardinality1 < cardinality2;
	}
	bool operator == (const CantorSet& set) const {
		return  this->elements == set.elements &&
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
	bool operator [](const CantorSet element) const {
		return this->elements.count(element);
	}
	
	CantorSet operator + (const CantorSet& set) const {
		CantorSet result = *this;

		for (const auto& element : set.elements)
			result.push(element);

		return result;
	}
	CantorSet& operator += (const CantorSet& set) {
		for (const auto& element : set.elements)
			this->push(element);

		return *this;
	}

	CantorSet operator - (const CantorSet& set) const {
		CantorSet result = *this;

		for (const auto& element : set.elements)
			result.pop(element);

		return result;
	}
	CantorSet& operator -= (const CantorSet& set) {
		for (const auto& element : set.elements)
			this->pop(element);

		return *this;
	}

	CantorSet operator * (const CantorSet& set) const {
		CantorSet result;

		for (const auto& element : this->elements) {
			if (set[element])
				result.push(element);
		}

		return result;
	}
	CantorSet& operator *= (const CantorSet& set) {
		CantorSet temp = *this;
		*this = CantorSet();

		for (const auto& element : temp.elements) {
			if (set[element])
				this->push(element);
		}
		
		return *this;
	}

	friend std::istream& operator>>(std::istream& cin, CantorSet& set)
	{
		string input;
		cin >> input;
		set = CantorSet(input);
		return cin;
	}
	friend std::ostream& operator<<(std::ostream& cout, CantorSet& set)
	{
		cout << set.toString();
		return cout;
	}
};

int main() {
	string set;

	set = "{{b,c},{d,e},a,e}";
	CantorSet test1(set);

	set = "{{b,c},a,d,f}";
	CantorSet test2(set);

	test1 *= test2;
	//CantorSet test3 = test1 * test2;
	cout << test1;

	return 0;
}
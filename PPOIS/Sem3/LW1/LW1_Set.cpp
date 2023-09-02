#include <string>
#include <set>

using std::string;
using std::set;

class CantorSet {
public:
	bool isEmpty = true;
	char data = 0;
	set<CantorSet> elements;
	
	void push(CantorSet element) {
		elements.emplace(element);
	}

	CantorSet stringToSet(string& setNotation)
	{
		CantorSet toReturn; 

		for (int i = 1; i < setNotation.size(); i++) {
			switch (setNotation[i]) {
			case '{': {
				//toReturn.push(setNotation.substr(i));
				break;
			}
			case '}': {
				//setNotation = setNotation.substr(i+1);
				return toReturn;
			}
			case ',': 
			case ' ': break;
			default: {
				toReturn.elements.emplace(CantorSet(setNotation[i]));
				break;

			}
			}
		}
		
		return toReturn;
	}

	CantorSet() {
		
	};
	CantorSet(string setNotation) {
		*this = stringToSet(setNotation);
	};
	CantorSet(char singleElement) {
		this->isEmpty = false;
		this->data = singleElement;
	};

	bool empty() {
		return isEmpty;
	}

	int cardinality() const {
		if (isEmpty) return 0;
		if(!elements.empty()) return elements.size();
		return 1;
	}

	void push(string element) {
		isEmpty = false;
	}
	void push(char element) {
		isEmpty = false;
		CantorSet toPush(element);
		elements.emplace(toPush);
	}

	/*void pop(string element) {

	}*/

	//bool operator [](string element) {

	//}

	bool operator > (const CantorSet& set) const {
		//return cardinality() > set.cardinality();
		return this->data > set.data;
	}
	bool operator < (const CantorSet& set) const {
		return this->data < set.data;
	}
	
	const CantorSet operator + (const CantorSet& set) {
		CantorSet result;
		for (const auto& element : set.elements) {
			result.elements.emplace(element);
		}
		return result;
	}

	CantorSet operator * (const CantorSet& set) const {
		CantorSet result;
		for (const auto& element : set.elements) {
			if (this->elements.count(element)) result.elements.emplace(element);
		}
		return result;
	}

	//CantorSet boolean() {

	//}
};
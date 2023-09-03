#pragma once

#include <iostream>
#include <string>
#include <set>

using std::string;
using std::set;

class CantorSet {
private:
	bool isEmpty = true;
	char data = 0;
	size_t offset = 0;
	set<CantorSet> elements;

public:
	bool empty() const;

	bool isSingleElement() const;

	size_t cardinality() const;

	void clear();

	void push();
	void push(char element);
	void push(const string& element);
	void push(const CantorSet& element);

	void pop(const string& element);
	void pop(const CantorSet& toDelete);

	CantorSet boolean() const;

	CantorSet();
	CantorSet(char element);
	CantorSet(string element);

	string toString() const;

	bool operator<(const CantorSet& set) const;
	bool operator==(const CantorSet& set) const;

	bool operator[](string element) const;
	bool operator[](const CantorSet& element) const;

	CantorSet operator+(const CantorSet& set) const;
	CantorSet& operator+=(const CantorSet& set);
	CantorSet operator-(const CantorSet& set) const;
	CantorSet& operator-=(const CantorSet& set);
	CantorSet operator*(const CantorSet& set) const;
	CantorSet& operator*=(const CantorSet& set);

	friend std::istream& operator>>(std::istream& cin, CantorSet& set);
	friend std::ostream& operator<<(std::ostream& cout, CantorSet& set);
};
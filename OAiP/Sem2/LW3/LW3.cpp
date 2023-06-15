#include <iostream>

using namespace std;

struct StackNode {
	StackNode* next = nullptr;
	int data = 0;
};

struct Stack {
	StackNode* top = nullptr;

	Stack() {}
	~Stack() {
		clear();
	}

	void show() {
		if (top == nullptr) {
			cout << "Stack is empty!\n";
			return;
		}
		cout << "Stack:\n";
		StackNode* it = top;
		while (it != nullptr) {
			cout << it->data << "\n";
			it = it->next;
		}
	}

	void clear() {
		while (top != nullptr) {
			StackNode* toDelete = top;
			top = top->next;
			delete toDelete;
		}
	}

	void push(int data) {
		StackNode* newElement = new StackNode;
		newElement->data = data;
		newElement->next = top;
		top = newElement;
	}

	int pop() {
		int toReturn = 0;
		if (top == nullptr) {
			cout << "Stack is empty!\n";
		}
		else {
			toReturn = top->data;
			StackNode* toDelete = top;
			top = top->next;
			delete toDelete;
		}
		return toReturn;
	}

	int peek() {
		int toReturn = 0;
		if (top == nullptr) {
			cout << "Stack is empty!\n";
		}
		else {
			toReturn = top->data;
		}
		return toReturn;
	}

	bool empty() {
		return !top;
	}
};
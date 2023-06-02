#include <iostream>
#include <string>

using namespace std;

struct DataNode {
	size_t key = 0;
	string data = "empty";
};

struct Stack {
	Stack* next = nullptr;
	DataNode dataNode;
};

void pushToStack(Stack*& stack, DataNode dataNode) {
	Stack* newElement = new Stack;
	newElement->dataNode = dataNode;
	newElement->next = stack;
	stack = newElement;
}

void deleteStack(Stack*& stack) {
	while (stack != nullptr) {
		Stack* toDelete = stack;
		stack = stack->next;
		delete toDelete;
	}
}

DataNode popFromStack(Stack*& stack) {
	DataNode dataNode;
	if (stack == nullptr) {
		cout << "Stack is empty!\n";
	}
	else {
		dataNode = stack->dataNode;
		Stack* toDelete = stack;
		stack = stack->next;
		delete toDelete;
	}
	return dataNode;
}


void showStack(Stack* stack) {
	if (stack == nullptr) {
		cout << "Stack is empty!\n";
		return;
	}
	cout << "Stack:\n";
	while (stack != nullptr) {
		cout << stack->dataNode.key << " - " << stack->dataNode.data << "\n";
		stack = stack->next;
	}
}

void swapMinAndMax(Stack*& stack) {
	if (stack == nullptr) return;

	Stack* iterStack = stack;

	size_t maxKey = stack->dataNode.key,
		minKey = stack->dataNode.key;

	Stack* min = stack;
	Stack* minPrev = stack;
	Stack* max = stack;
	Stack* maxPrev = stack;

	while (iterStack->next != nullptr) {
		if (iterStack->next->dataNode.key > maxKey) {
			maxKey = iterStack->next->dataNode.key;
			max = iterStack->next;
			maxPrev = iterStack;
		}
		if (iterStack->next->dataNode.key < minKey) {
			minKey = iterStack->next->dataNode.key;
			min = iterStack->next;
			minPrev = iterStack;
		}

		iterStack = iterStack->next;
	}

	if (minPrev != min) minPrev->next = max; else stack = max;
	if (maxPrev != max) maxPrev->next = min; else stack = min;

	swap(min->next, max->next);
}

int main()
{
	Stack* stack = nullptr;

	pushToStack(stack, { 2, "one" });
	pushToStack(stack, { 1, "two" });
	pushToStack(stack, { 8, "three" });
	pushToStack(stack, { 4, "four" });
	pushToStack(stack, { 5, "one" });
	pushToStack(stack, { 6, "two" });
	pushToStack(stack, { 7, "four" });
	pushToStack(stack, { 3, "three" });

	//showStack(stack);

	//cout << dataNode.data << "\n";

	showStack(stack);

	swapMinAndMax(stack);

	showStack(stack);

	DataNode popTest;
	for (int i = 0; i < 10; i++) popTest = popFromStack(stack);

	deleteStack(stack);
}

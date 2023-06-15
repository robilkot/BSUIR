#include <iostream>

using namespace std;

struct Qnode {
	int data = 0;
	Qnode* next = nullptr;
	Qnode* prev = nullptr;

	Qnode(int data) {
		this->data = data;
	}
};

struct Queue {
	Qnode* begin = nullptr;
	Qnode* end = nullptr;

	Queue() {}

	void pushBack(int data) {
		Qnode* pushed = new Qnode(data);

		if (!end) {
			begin = end = pushed;
		}
		else {
			Qnode* pushed = new Qnode(data);
			end->next = pushed;
			pushed->prev = end;
			end = pushed;
		}
	}

	void pushFront(int data) {
		Qnode* pushed = new Qnode(data);

		if (!begin) {
			begin = end = pushed;
		}
		else {
			begin->prev = pushed;
			pushed->next = begin;
			begin = pushed;
		}
	}

	int popBack() {
		if (!end) {
			cout << "Empty\n";
			return 0;
		}
		int toReturn = end->data;
		if (end->prev) end->prev->next = nullptr;
		else begin = nullptr;

		Qnode* toDelete = end;
		end = end->prev;

		delete toDelete;
		return toReturn;
	}

	int popFront() {
		if (!begin) {
			cout << "Empty\n";
			return 0;
		}
		int toReturn = begin->data;
		if (begin->next) begin->next->prev = nullptr;
		else end = nullptr;

		Qnode* toDelete = begin;
		begin = begin->next;

		delete toDelete;
		return toReturn;
	}

	void show() {
		if (!begin) {
			cout << "Queue is empty\n";
			return;
		}
		cout << "Queue from begin to end:\n";
		Qnode* iter = begin;
		while (iter) {
			cout << iter->data << "\n";
			iter = iter->next;
		}
	}

	bool empty() {
		return !begin;
	}

	~Queue() {
		while (begin && end) {
			cout << "deleted " << begin->data << "\n";
			Qnode* toDelete = begin;
			begin = begin->next;
			delete toDelete;
		}
	}
};


void DeleteElement(Queue& queue, Qnode* element) {
	if (element == queue.begin) {
		queue.popFront();
		return;
	}
	else if (element == queue.end) {
		queue.popBack();
		return;
	}

	if (element->prev) {
		element->prev->next = element->next;
	}
	if (element->next) {
		element->next->prev = element->prev;
	}
	delete element;
}

void SwapElements(Queue& queue) {
	if (!queue.begin || queue.begin == queue.end) return;

	Qnode* min = queue.begin;
	Qnode* max = queue.begin;

	// Находим минимальный и максимальный узлы
	for (Qnode* iter = queue.begin; iter; iter = iter->next) {
		if (iter->data < min->data) min = iter;
		else if (iter->data > max->data) max = iter;
	}

	min = queue.begin->next->next;
	max = queue.begin->next;

	// Проверка на то, не являются ли заменяемые элементы крайними
	if (min == queue.end) queue.end = max;
	else if (max == queue.end) queue.end = min;

	if (max == queue.begin) queue.begin = min;
	else if (min == queue.begin) queue.begin = max;

	// Непосредственно замена элементов
	swap(min->prev, max->prev);

	if (min->prev) min->prev->next = min;
	if (max->prev) max->prev->next = max;

	swap(min->next, max->next);

	if (min->next) min->next->prev = min;
	if (max->next) max->next->prev = max;
}

int main() {
	Queue queue;

	for(int i = 1; i <= 9; i++)
		queue.pushFront(i);

	//queue.show();

	//Qnode* iter1 = queue.begin, *iter2 = queue.begin;
	//while(iter1->next)
	//{
	//	iter1 = iter1->next;
	//	iter2 = iter1->next;

	//	Qnode* pushed = new Qnode(69);

	//	pushed->prev = iter1;
	//	pushed->next = iter2;

	//	iter1->next = pushed;
	//	iter2->prev = pushed;

	//	iter1 = iter2;
	//}

	queue.show();

	//DeleteElement(queue, queue.begin);
	//DeleteElement(queue, queue.end);

	//DeleteElement(queue, queue.end->prev->prev);

	Qnode* iter = queue.begin->next->next->next;
	SwapElements(queue);

	queue.show();

	//SwapElements(queue, iter, iter->next);

	//queue.show();
}
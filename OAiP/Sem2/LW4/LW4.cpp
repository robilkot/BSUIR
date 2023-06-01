#include <iostream>
#include <string>

using namespace std;

struct DataNode {
    int key = 0;
    string value = "empty";
};

struct Queue {
    DataNode dataNode;
    Queue* next = nullptr;
    Queue* prev = nullptr;
};

void showQueue(Queue* queue) {
    if (queue == nullptr) {
        cout << "queue is empty\n";
        return;
    }
    else {
        cout << "queue from back to front:\n";
        while (queue != nullptr) {
            cout << queue->dataNode.key << " - " << queue->dataNode.value << "\n";
            queue = queue->prev;
        }
    }
}

void deleteQueue(Queue*& queue) {
    Queue* iter = queue;
    queue = nullptr;

    while (iter != nullptr) {
        Queue* toDelete = iter;
        iter = iter->prev;
        delete toDelete;
    }
}

void pushFront(Queue*& queue, DataNode dataNode) {
    if (queue == nullptr) {
        queue = new Queue;
        queue->dataNode = dataNode;
        return;
    }

    Queue* iter = queue;
    while (iter->prev != nullptr) {
        iter = iter->prev;
    }
    iter->prev = new Queue;
    iter->prev->next = iter;
    iter->prev->dataNode = dataNode;
}

void pushBack(Queue*& queue, DataNode dataNode) {
    if (queue == nullptr) {
        queue = new Queue;
        queue->dataNode = dataNode;
        return;
    }

    queue->next = new Queue;
    queue->next->prev = queue;
    queue->next->dataNode = dataNode;

    queue = queue->next;
}

DataNode popFront(Queue*& queue) {
    if (queue == nullptr) return { 0, "empty " };

    Queue* toDelete = queue;
    while (toDelete->prev != nullptr)
        toDelete = toDelete->prev;
   
    DataNode toReturn = toDelete->dataNode;
    
    if (toDelete->next == nullptr) queue = nullptr;
    else {
        toDelete->next->prev = nullptr;
        delete toDelete;
    }
    return toReturn;
}

DataNode popBack(Queue*& queue) {
    if (queue == nullptr) return { 0, "empty "};

    Queue* toDelete = queue;
    queue = queue->prev;
    if(queue) queue->next = nullptr;

    DataNode toReturn = toDelete->dataNode;

    delete toDelete;
    return toReturn;
}

int main()
{
    Queue* queue = nullptr;
    DataNode popTest;

    for (int i = 0; i < 10; i++) pushBack(queue, { i, to_string(i)});
    showQueue(queue);
    for (int i = 0; i < 20; i++) popTest = popBack(queue);


    for (int i = 0; i < 10; i++) pushBack(queue, { i, to_string(i) });
    showQueue(queue);
    for (int i = 0; i < 8; i++) popTest = popFront(queue);

    deleteQueue(queue);
}
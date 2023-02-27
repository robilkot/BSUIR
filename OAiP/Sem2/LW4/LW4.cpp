#include <iostream>
#include <conio.h>

struct Queue
{
    int info = 0;
    Queue* next = nullptr;
    Queue* prev = nullptr;
};

Queue* pushBack(Queue* back, int in)
{
    Queue* t = new Queue;
    t->info = in;
    
    if (back != nullptr) {
        t->prev = back;
        back->next = t;
    }
    
    return t;
}

Queue* pushFront(Queue* back, int in)
{
    Queue* t = new Queue;
    t->info = in;
        
    if (back == nullptr) {
        return t;
    }
    
    Queue* front = back;
    while (front->prev != nullptr)
            front = front->prev;
    
    t->next = front;
    front->prev = t;

    return back;
}

void popBack(Queue* back) {
    if (back != nullptr) {
        if (back->prev != nullptr) {
            back->prev->next = nullptr;
        }
    delete back;
    }
}

void popFront(Queue* back) {
    Queue* front = back;
    while (front->next != nullptr)
        front = front->next;

    if (front != nullptr) {
        if (front->next != nullptr) {
            front->next->prev = nullptr;
        }
        delete front;
    }
}

void viewQueue(Queue* back)
{
    std::cout << "Queue:\n";
    Queue* t = back;
    while (t != NULL) {
        std::cout << t->info << "\n";
        t = t->prev;
    }
}

void deleteAll(Queue* back)
{
    while (back != NULL) {
        Queue* t = back;
        back = back->prev;
        delete t;
    }
}

void swapMaxAndMin(Queue* back)
{
    if (back == nullptr) return;

    int max = back->info, min = back->info;
    Queue *maxptr = back, *minptr = back;

    for (Queue* node = back; node != NULL; node = node->prev) {
        if (node->info > max) {
            max = node->info; // find max
            maxptr = node;
        }
        else if (node->info < min) {
            min = node->info; // find min
            minptr = node;
        }
    }

    std::swap(minptr->info, maxptr->info);
}

int main()
{
    Queue* back = nullptr;
    bool exit = 0;

    do {
        std::cout << "Press q to exit, 1 to push element to front, 2 to push element to back,\n" <<
            "3 to pop from front, 4 to pop from back, 5 to view queue, 6 to swap max and min in queue\n";

        switch (_getch()) {
        case 'q': exit = 1; break;
        case '1': {
            int pushed = 0;
            std::cout << "Input new value:\n";
            std::cin >> pushed;
            back = pushFront(back, pushed);
            break;
        }
        case '2': {
            int pushed = 0;
            std::cout << "Input new value:\n";
            std::cin >> pushed;
            back = pushBack(back, pushed);
            break;
        }
        case '3': {
            popFront(back);
            break;
        }
        case '4': {
            popBack(back);
            break;
        }
        case '5': {
            viewQueue(back);
            break;
        }
        case '6': {
            swapMaxAndMin(back);
            break;
        }
        }
    } while (!exit);

    deleteAll(back);
    return 0;
}
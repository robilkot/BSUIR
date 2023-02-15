#include <iostream>
#include <conio.h>

struct Stack
{
    int info = 0;
    Stack* next = nullptr;
};

Stack* pushOntoStack(Stack* top, int in)
{
    Stack* t = new Stack;
    t->info = in;
    t->next = top;
    return t;
}

void viewStack(Stack* top)
{
    std::cout << "Stack:\n";
    Stack* t = top;
    while (t != NULL) {
        std::cout << t->info << "\n";
        t = t->next;
    }
}

void deleteAll(Stack* top)
{
    while (top != NULL) {
        Stack* t = top;
        top = (top)->next;
        delete t;
    }
}

void swapMaxAndMin(Stack* top)
{
    if (top == nullptr) return;

    int max = top->info, min = top->info;
    Stack* maxptr = top, * minptr = top;

    for (Stack* node = top; node != NULL; node = node->next) {
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
    Stack* top = nullptr;
    bool exit = 0;

    do {
        std::cout << "Press q to exit, 1 to push element to stack, 2 to view stack, 3 to swap max and min in stack\n";
        switch (_getch()) {
        case 'q': exit = 1; break;
        case '1': {
            int pushed = 0;
            std::cout << "Input new value:\n";
            std::cin >> pushed;
            top = pushOntoStack(top, pushed);
            break;
        }
        case '2': {
            viewStack(top);
            break;
        }
        case '3': {
            swapMaxAndMin(top);
            break;
        }
        }
    } while (!exit);

    deleteAll(top);
    return 0;
}

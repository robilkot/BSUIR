#include <iostream>
#include <conio.h>
#include <string>

struct Stack
{
	char info = 0;
	Stack* next = nullptr;
};

Stack* pushToStack(Stack* top, char in)
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

Stack* popFromStack(Stack* top)
{
	Stack* t = nullptr;
	if (top != nullptr) t = top->next;
	delete top;

	return t;
}

void deleteAll(Stack* top)
{
	while (top != NULL) {
		Stack* t = top;
		top = (top)->next;
		delete t;
	}
}

std::string toIpn(std::string normalExpression)
{
	Stack* top = nullptr;
	std::string ipnExpression;

	for (const char& c : normalExpression)
	{
		if (isdigit(c)) ipnExpression += c;
		else if (c == ')') {
			while (top->info != '(') {
				ipnExpression += top->info;
				top = popFromStack(top);
			}
			top = popFromStack(top);
		}
		else {
			if (c == '+' || c == '-') { // Достаем из стека операции большего или равного приоритета
				while (top != nullptr && (
					top->info == '*' ||
					top->info == '/' ||
					top->info == '%' ||
					top->info == '-' ||
					top->info == '+'))
				{
					ipnExpression += top->info;
					top = popFromStack(top);
				}
			}
			else if (c == '*' || c == '/' || c == '%') {
				while (top != nullptr && (
					top->info == '*' ||
					top->info == '/' ||
					top->info == '%'))
				{
					ipnExpression += top->info;
					top = popFromStack(top);
				}
			}

			top = pushToStack(top, c); // Операцию кидаем в стек
		}
	}
	for (Stack* t = top; t != nullptr; t = t->next)
		ipnExpression += t->info;

	deleteAll(top);
	return ipnExpression;
}

int calculateIpn(std::string ipnExpression)
{
	Stack* top = nullptr;

	for (const char& c : ipnExpression)
	{
		if (isdigit(c)) top = pushToStack(top, c - '0'); // Кидаем операнд в стек. - '0' т.к. чар
		else {
			int operand1, operand2;
			operand1 = top->info;
			operand2 = top->next->info;
			top = popFromStack(top);
			top = popFromStack(top);

			switch (c) { // Результат операции кидаем в стек вместо двух операндов
			case '*': top = pushToStack(top, operand1 * operand2); break;
			case '/': top = pushToStack(top, operand1 / operand2); break;
			case '%': top = pushToStack(top, operand1 % operand2); break;
			case '+': top = pushToStack(top, operand1 + operand2); break;
			case '-': top = pushToStack(top, operand1 - operand2); break;
			}
		}
	}
	int answer = top->info;

	deleteAll(top);
	return answer;
}

int main()
{
	bool exit = 0;
	do {
		std::cout << "Press q to exit, or any other key to convert normal expression to inversed polish notation and count it\n";
		if (_getch() == 'q') exit = 1;
		else {
			std::string normalExpression, ipnExpression;

			std::cout << "Input expression:\n";
			std::cin >> normalExpression;

			ipnExpression = toIpn(normalExpression);
			std::cout << "Inverse polish notation: " << ipnExpression << '\n'
				<< "Result of calculations: " << calculateIpn(ipnExpression) << '\n';

			break;
		}
	} while (!exit);

	return 0;
}
//5. Найти значение функции Аккермана A(m, n), которое определяется для
//всех неотрицательных целых аргументов m и n следующим образом :
//A(0, n) = n + 1;
//A(m, 0) = A(m – 1, 1) при m > 0;
//A(m, n) = A(m – 1, A(m, n – 1)) при m > 0 и n > 0

#include <iostream>
#include <conio.h>

unsigned long long  AckermannRecursive(unsigned long long m, unsigned long long n) {
	if (m == 0)
		return n + 1;
	else
		if (n == 0) return AckermannRecursive(m - 1, 1);
			else return AckermannRecursive(m - 1, AckermannRecursive(m, n - 1));
}

int main()
{
	do {
		unsigned long long  m = 2, n = 1;
		std::cout << "Input non-negative m and n:\n";
		std::cin >> m >> n;

		std::cout << "The result is " << AckermannRecursive(m, n) << ". Press q to exit or other key to retry\n";

		switch (_getch()) {
		case 'й':
		case 'q': exit(0);
		}
	} while (true);
}

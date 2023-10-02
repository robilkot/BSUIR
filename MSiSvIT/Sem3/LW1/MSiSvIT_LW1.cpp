#include <iostream>

using std::cout;
using std::cin;

long long fact(int n) {
	if (n == 0 || n == 1) {
		return 1;
	}
	else {
		return n * fact(n - 1);
	}
}

int main()
{
	int M = 0;

	do {
		cout << "Input number (1,13):\n";
		cin >> M;
	} while (M == 0 || M > 13);

	cout << fact(M);
	return 0;
}

// Вариант 20
// Временная сложность O(M)
// Пространственная O(M)
// Время работы 2M;
// Используемая память M + 1
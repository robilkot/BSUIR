#include <iostream>
#include <math.h>

using namespace std;

float func3(float x) {
	return (1 + 2 * x * x) * pow(2.7182818284590, x * x);
}

long double fact3(int N)
{
	if (N > 0) return N * fact3(N - 1);
	if (N == 0) return 1;
	if (N < 0) return 0;
}

float findsumm(int n, float x) {
	float summ = 0;
	for (int k = 0; k <= n; k++) {
		summ += (2 * k + 1) * pow(x, 2 * k) / fact3(k);
	}
	return summ;
}

int main3() {
	float a, b, h, eps;
	int i = 1;
	cout << "Pls input a,b,h,epsilon \n";
	cin >> a >> b >> h >> eps;
	cout << "\n";

	if (!cin) //numeric check
	{
		cin.clear();
		cin.ignore();
		cout << "Non-numeric!" << "\n";
		return 0;
	}

	cout << "i\t Y\t S\t |Y-S|\t n sum\n";

	for (a; a <= b; a += h, i++) {
		int n = 1;
		while (abs(findsumm(n, a) - func3(a)) > eps) { n++; }
		cout << i << "\t" << func3(a) << "\t" << findsumm(n, a) << "\t" << abs(func3(a) - findsumm(n,a)) << "\t" << n <<"\n";
	}
	cout << "\n";
}

//params for test:
//0.1
//1
//0.1
//0.001
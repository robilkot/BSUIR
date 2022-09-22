#include <iostream>
#include <math.h>

using namespace std;

float func2(float x) {
	return (1+2*x*x) * pow(2.7182818284590, x * x);
}

long double fact2(int N)
{
	if (N > 0) return N * fact2(N - 1);
	if (N == 0) return 1;
	if (N < 0) return 0;
}

int main2() {
	float a, b, h, summ;
	int i = 1, n = 0;
	cout << "Pls input a,b,h,n \n";
	cin >> a >> b >> h >> n; 
	cout << "\n";

	if (!cin) //numeric check
	{
		cin.clear();
		cin.ignore();
		cout << "Non-numeric!" << "\n";
		return 0;
	}

	cout << "i" << " -> " << "   Y   " << "  ->  " << "    S    " << " -> " << "  |Y-S| \n";

	for (a; a <= b; a += h, i++) {
		summ = 0;
		for (int k=0; k <= n; k++) {
			summ += (2 * k + 1) * pow(a, 2 * k) / fact2(k);
		}
		cout << i << " -> " << func2(a) << "  ->  " << summ <<"  ->  " << abs(func2(a)-summ)  << "\n";
	}
	cout << "\n";
}

//params for test:
//0.1
//1
//0.1
//6
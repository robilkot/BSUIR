#include <iostream>
#include <math.h>

using namespace std;

float func(float x) {
	return (x * x / 4 + x / 2 - 3) * pow(2.7182818284590, x / 2);
}

int main1() {
	float a, b, h, max, min;
	int i=1;
	cout << "Pls input a,b,h \n";
	cin >> a >> b >> h;


	if (!cin) //numeric check
	{
		cin.clear();
		cin.ignore();
		cout << "Non-numeric!" << "\n";
		return 0;
	}

	max = func(a);
	min = func(a);

	cout << "n\t x\t y\n";
	for (a; a <= b; a += h, i++) {
		if (max < func(a)) max = func(a);
		if (min > func(a)) min = func(a);
		cout << i << "\t" << a << "\t" << func(a) << "\n";
	}
	cout << "max value is " << max << "; min value is " << min << "\n";
}
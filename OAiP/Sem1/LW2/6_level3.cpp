#include <math.h>
#include <iostream>

using namespace std;

double max(double arg1, double arg2) {
	if (arg1 > arg2) return arg1; else return arg2;
}

double min(double arg1, double arg2) {
	if (arg1 < arg2) return arg1; else return arg2;
}

int main3() {
	double x, y, z, m;

	cout << "Pls input x,y,z \n";
	cin >> x >> y >> z;

	if (!cin) //numeric check
	{
		cin.clear();
		cin.ignore();
		cout << "Non-numeric!" << "\n";
		return 0;
	}

	if (y * z != 0 && x + y + z != 0) {
		if (max(x + y + z, x / (y * z)) != 0) {
			m = min(y,z)/max(min(x,y),min(y,z));
			cout << "m equals " << m << "\n";
			return 0;
		}
	}
	cout << "Arguments out of bounds! \n";
}
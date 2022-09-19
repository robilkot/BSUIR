#include <math.h>
#include <iostream>

using namespace std;

int main2() {
	double a, b, x, y, z, fi;
	int func;

	cout << "Pls input a,b,z \n";
	cin >> a >> b >> z;

	if (!cin) //numeric check
	{
		cin.clear();
		cin.ignore();
		cout << "Non-numeric!" << "\n";
		return 0;
	}

	if (z < 0) x = z, cout << "z<0, calculating x=z \n"; else x = sin(z), cout << "z>=0, calculating x=sin(z) \n";

	cout << "Pls choose function (1 - 2x, 2 - x^2, 3 - x/3) \n";
	cin >> func;
	switch (func)
	{
	case 1:fi = 2 * x, cout << "2x chosen \n"; break;
	case 2:fi = x*x, cout << "x^2 chosen \n"; break;
	case 3:fi = 3 - x/3, cout << "3-x/3 chosen \n"; break;
	default: cout << "Incorrect number given"; return 0;
	}

	y = 2. / 3 * a * sin(x) * sin(x) - 3. / 4 *b * cos(fi) * cos(fi);
	cout << "y equals " << y << "\n";
}
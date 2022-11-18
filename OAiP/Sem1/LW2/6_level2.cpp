#include <math.h>
#include <iostream>

using namespace std;

float input_num() { // Проверка на числовой ввод
	bool ping = true;
	int done = 0;
	float output = 0;
	do {
		char check[256];
		cout << "Enter number (double or integer)\n";
		cin.getline(check, 256);
		bool point = false;
		for (int i = 0; i < strlen(check); i++) {
			if (isdigit(check[i])) done++;
			else if (i != 0 && i != (strlen(check) - 1) && check[i] == '.' && point == false) {
				done++;
				point = true;
			}
			else if (i == 0 && check[i] == '-' && i != (strlen(check) - 1)) {
				done++;
			}
			else {
				cout << "Error\n";
				ping = false;
				break;
			}
			if (done == strlen(check)) {
				ping = true;
				break;
			}
		}
		output = atof(check);
		done = 0;
	} while (ping == false);
	return output;
}

int main2() {
	double a, b, x, y, z, fi;
	int func;

	cout << "Pls input a,b,z \n";
	a = input_num();
	b = input_num();
	z = input_num();

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
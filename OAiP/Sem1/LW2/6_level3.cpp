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

double max(double arg1, double arg2) {
	return arg1 > arg2 ? arg1 : arg2;
}

double min(double arg1, double arg2) {
	return arg1 < arg2 ? arg1 : arg2;
}

int main3() {
	double x, y, z, m;

	cout << "Pls input x,y,z \n";
	x = input_num();
	y = input_num();
	z = input_num();

	if (y * z != 0 && x + y + z != 0) {
		if (max(x + y + z, x / (y * z)) != 0) {
			m = min(y,z)/max(min(x,y),min(y,z));
			cout << "m equals " << m << "\n";
			return 0;
		}
	}
	cout << "Arguments out of bounds! \n";
}
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

int main1() {
	double x,y,z;
	cout << "pls input z \n";
	z = input_num();

	if (z < 0) x = z, cout << "z<0, calculating x=z \n"; else x = sin(z), cout << "z>=0, calculating x=sin(z) \n";

	y = 2./3*sin(x)*sin(x)-3./4*cos(x)*cos(x);
	cout << "y equals " << y << "\n";
}
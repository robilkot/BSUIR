#include <iostream>
#include <cmath>
#include <conio.h>

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

double f(double x) {
    return 7 * pow(sin(x),2);
}

double findmin_rec(double a, double b, double eps) {
        double m = (a + b) / 2;
        if (b - a < eps) return m;
        double x1 = findmin_rec(a, m, eps), x2 = findmin_rec(m, b, eps);
        return f(x1) < f(x2) ? x1 : x2;
}

double findmin_lin(double a, double b, double eps) {
    double min_f = f(a), min = a, val;
    for (; a < b; a += eps) {
        val = f(a);
        if (val < min_f) {
            min = a;
            min_f = val;
        }
    }
    return min;
}

int main() {
    cout << "\nLW8 level 3\n";
    cout << "\nPls input epsilon\n";
    double eps = input_num();
    cout << "\nPress 1 for recursive or any other button for linear algorithm\n";
    _getch() == '1' ? cout << "\n\n[Using recursion] Function minimum is " << findmin_rec(2, 6, eps) : cout << "\n\n[Using linear] Function minimum is " << findmin_lin(2, 6, eps);
    return 0;
}
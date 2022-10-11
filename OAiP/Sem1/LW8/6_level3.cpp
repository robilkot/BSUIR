#include <iostream>
#include <cmath>
#include <conio.h>
#include <regex>

using namespace std;

float input_num() {
    regex reg_num("^[\\+-]?([0-9]+\\.?[0-9]*|\\.?[0-9]+)$");
    string inp;
    cin >> inp;
    while (!regex_match(inp, reg_num)) {
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        cout << "\nNon-numeric, pls re-input:\n";
        cin >> inp;
    }
    return stof(inp);
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
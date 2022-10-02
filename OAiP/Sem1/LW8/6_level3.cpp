#include <iostream>
#include <cmath>
#include <conio.h>

using namespace std;

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

int main3() {
    double eps;
    cout << "\nPls input epsilon\n";
    cin >> eps;
    cout << "\nPls press 1 for recursive or any other button for linear algorithm\n";
    _getch() == '1' ? cout << "\n\n[Using recursion] Function minimum is " << findmin_rec(2, 6, eps) : cout << "\n\n[Using linear] Function minimum is " << findmin_lin(2, 6, eps);
    return 0;
}
#include <iostream>
#include <math.h>

using namespace std;

int main1()
{
    double alpha, z1, z2;
    cout << "Pls enter alpha" << "\n";
    cin >> alpha;
    z1 = cos(alpha) + cos(2 * alpha) + cos(6 * alpha) + cos(7 * alpha);
    z2 = 4 * cos(alpha / 2) * cos(alpha * 5 / 2) * cos(4 * alpha);
    cout << "z1 equals " << z1 << "\n";
    cout << "z2 equals " << z2 << "\n";
    return 0;
}
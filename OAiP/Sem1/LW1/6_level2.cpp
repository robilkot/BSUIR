#include <iostream>
#include <math.h>

using namespace std;


int main2()
{
    double alpha, z1, z2;
    cout << "Pls enter alpha" << "\n";
    cin >> alpha;

    if (!cin) //numeric check
    {
        cin.clear();
        cin.ignore();
        cout << "Non-numeric!" << "\n";
        return 0;
    }

    if (alpha < 0) {
        cout << "omg danila what are doing (<0)";
        return 0;
    }

    if (alpha != 0) {
        z1 = sqrt(pow((3*alpha+2),2)-24*alpha) / (3 * sqrt(alpha) - 2 / sqrt(alpha));
        z2 = -sqrt(alpha);
        cout << "z1 equals " << z1 << "\n";
        cout << "z2 equals " << z2 << "\n";
    }
    else {
        cout << "omg danila what are doing (=0)";
        return 0;
    }
    return 0;
}
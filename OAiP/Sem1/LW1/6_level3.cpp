#include <iostream>
#include <math.h>

#define PI 3.14159265358979323846

using namespace std;

int main3()
{
    double x, y, z, b1, b2, b3;
    cout <<"Pls enter x, y ,z" << "\n";
    cin >> x >> y >> z;

    if (!cin) //numeric check
    {
        cin.clear();
        cin.ignore();
        cout << "Non-numeric!" << "\n";
        return 0;
    }

    b1 = pow(x, 1 / 3) + pow(x, y + 2);
    b2 = pow(asin(z), 2)-abs(x-y);

    if (z>= -PI/2 and z <= PI/2 and b1 >= 0) {
        b3 = sqrt(10*b1)*b2;
        cout << "beta equals " <<  b3 << "\n";
    }
    else {
        cout << "Arguments out of bounds!";
        return 0;
    }

    return 0;
}
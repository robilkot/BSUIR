#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    double x, y, z, b1;
    cout <<"Pls enter x, y ,z" << "\n";
    cin >> x >> y >> z;

    if (!cin) //numeric check
    {
        cin.clear();
        cin.ignore();
        cout << "Non-numeric!" << "\n";
        return 0;
    }

    b1 = pow(x, 1./ 3) + pow(x, y + 2);

    if (z>= -1 and z <= 1 and b1 >= 0) {
        cout << "beta equals " << sqrt(10 * (pow(x, 1. / 3) + pow(x, y + 2))) * (asin(z) * asin(z) - fabs(x - y)) << "\n";
    }
    else {
        cout << "Arguments out of bounds!";
        return 0;
    }

    return 0;
}
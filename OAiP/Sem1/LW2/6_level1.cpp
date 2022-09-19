#include <math.h>
#include <iostream>

using namespace std;

int main1() {
	double x,y,z;
	cout << "pls input z \n";
	cin >> z;

	if (!cin) //numeric check
	{
		cin.clear();
		cin.ignore();
		cout << "Non-numeric!" << "\n";
		return 0;
	}

	if (z < 0) x = z, cout << "z<0, calculating x=z \n"; else x = sin(z), cout << "z>=0, calculating x=sin(z) \n";

	y = 2./3*sin(x)*sin(x)-3./4*cos(x)*cos(x);
	cout << "y equals " << y << "\n";
}
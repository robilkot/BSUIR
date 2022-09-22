#include <iostream>
#include <math.h>

using namespace std;

int main1() {
	const int length = 20;
	float arr[length];
	float summ=0;

	cout << "Pls input array elements \n\n";
	for (int i = 0; i < length; i++) {
		cin >> arr[i];
	}

	cout << "\n";

	if (!cin) //numeric check
	{
		cin.clear();
		cin.ignore();
		cout << "Non-numeric!" << "\n";
		return 0;
	}

	for (int i = 0; i < length; i++) {
		summ += arr[i]- (int) arr[i];
	}
	cout << "The summ is " << summ; //сумма дробных

	cout << "\n";
}
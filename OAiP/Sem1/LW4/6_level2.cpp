#include <iostream>
#include <math.h>
#include <conio.h>

using namespace std;

int main2() {
	const int length = 20;
	int n_n1, n_n2; //number_negative1, 2
	n_n1 = -1;
	n_n2 = -1;
	float arr[length];
	float summ = 0;

	cout << "Pls type 1 to input elements manually (otherwise will be randomly generated) \n\n";
	if (_getch() == '1') {
		cout << "Pls input elements for array \n\n";
		for (int i = 0; i < length; i++) {
			cin >> arr[i];
		}
	}
	else {
		cout << "Generating random numbers \n\n";
		for (int i = 0; i < length; i++) {
			arr[i] = ((rand() % 100) - 50) / 5.; //generate number in [-9.8; 10]
			cout << arr[i] << "\n";
		}
	}

	if (!cin) //numeric check
	{
		cin.clear();
		cin.ignore();
		cout << "Non-numeric!" << "\n";
		return 0;
	}

	for (int i = 0; i < length; i++) { //check for the 1st negative element
		if (arr[i] < 0) {
			n_n1 = i;
			break;
		}
	}
	if (n_n1 != -1) { //and for the 2nd
		for (int j = n_n1+1; j < length; j++) {
			if (arr[j] < 0) {
				n_n2 = j;
				break;
			}
		}
	}
	if (n_n1 == -1 && n_n2 == -1) { 
		cout << "\n No negative numbers in array! \n";
		return 0;
	}
	
	for (int k = n_n1 + 1; k < n_n2; k++) {
		summ += arr[k] - (int) arr[k];
	}
	cout << "\n The summ is " << summ; //сумма дробных
	cout << "\n";
}
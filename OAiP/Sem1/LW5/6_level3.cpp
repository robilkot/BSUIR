#include <iostream>
#include <math.h>
#include <conio.h>

using namespace std;

float scalarproduct(float** arr, int n) {
	float min = arr[0][0], max = arr[0][0];
	int min_n = 0, max_m = 0;
	float scalarproduct = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (arr[i][j] > max) max = arr[i][j], max_m = i;
			if (arr[i][j] < min) min = arr[i][j], min_n = j;
		}
	}
	cout << "\nMin: " << min_n << "\t" << min;
	cout << "\nMax: " << max_m << "\t" << max << "\n\n";
	for (int i = 0; i < n; i++) {
		scalarproduct += arr[i][max_m]*arr[min_n][i];
	}
	return scalarproduct;
}

int main3() {
	int n;

	cout << "Pls unput size for array" << "\n\n";
	cin >> n;

	if (!cin) //numeric check
	{
		cin.clear();
		cin.ignore();
		cout << "\nNon-numeric!\n";
		return 0;
	}

	float** arr = new float* [n];
	for (int i = 0; i < n; i++) {
		arr[i] = new float [n] ;
	}

	cout << "Pls type 1 to input elements manually (otherwise will be randomly generated) \n\n";
	if (_getch() == '1') {
		cout << "Pls input elements for array \n\n";
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cin >> arr[i][j];
			}
		}
	}
	else {
		cout << "Generating random numbers \n\n";
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				arr[i][j] = ((rand() % 100) - 50) / 5.; //generate number in [-9.8; 10]
			}
		}
	}

	cout << "\nGiven array:\n\n";
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cout << arr[i][j] << "\t";
		}
		cout << "\n";
	}

	cout << "The product is " << scalarproduct(arr, n) << "\n";

	for (int i = 0; i < n; i++) {
		delete[] arr[i];
	}
	delete[] arr;
}
#include <iostream>
#include <math.h>
#include <conio.h>
#include <algorithm>

using namespace std;

int main2() {
	int m, n;
	int counter = 0;

	cout << "Pls unput n, m for array" << "\n\n";
	cin >> m >> n;

	float* arr_flat= new float[m*n];

	if (!cin) //numeric check
	{
		cin.clear();
		cin.ignore();
		cout << "\nNon-numeric!\n";
		return 0;
	}

	float** arr = new float* [m];
	for (int i = 0; i < m; i++) {
		arr[i] = new float[n];
	}

	cout << "\nPls type 1 to input elements manually (otherwise will be randomly generated) \n\n";
	if (_getch() == '1') {
		cout << "Pls input elements for array \n\n";
		cin.clear();
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				cin >> arr[i][j];
			}
		}
	}
	else {
		cout << "Generating random numbers \n\n";
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				arr[i][j] = rand() % 100; //generate number
			}
		}
	}

	cout << "\nGiven array:\n\n";
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			cout << arr[i][j] << "\t";
		}
		cout << "\n";
	}

	int arr_flat_cnt = 0;
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			arr_flat[arr_flat_cnt] = arr[i][j];
			arr_flat_cnt++;
		}
	}
	sort(arr_flat, arr_flat+m*n);

	for (int i = 1; i < m*n; i++) {
			if (arr_flat[i-1] == arr_flat[i]) {
				counter++;
			}
	}

	cout << "\nTotal unique numbers: " << m*n-counter << "\n";

	for (int i = 0; i < m; i++) {
		delete[] arr[i];
	}
	delete[] arr;
}
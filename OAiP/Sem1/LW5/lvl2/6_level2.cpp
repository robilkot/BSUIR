#include <iostream>
#include <math.h>
#include <conio.h>
#include <algorithm>
#include <regex>

using namespace std;

float input_num() {
	regex reg_num("^[\\+-]?([0-9]+\\.?[0-9]*|\\.?[0-9]+)$");
	string inp;
	cin >> inp;
	while (!regex_match(inp, reg_num)) {
		cin.clear();
		cin.ignore(numeric_limits<streamsize>::max(), '\n');
		cout << "\nNon-numeric, pls re-input:\n";
		cin >> inp;
	}
	return stof(inp);
}

int main() {
	cout << "\nLW5 level 2\n";
	int counter = 0;

	cout << "Pls unput n, m for array" << "\n\n";
	int m = input_num(), n = input_num();

	float* arr_flat = new float[m * n];

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
				arr[i][j] = input_num();
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
	sort(arr_flat, arr_flat + m * n);

	for (int i = 1; i < m * n; i++) {
		if (arr_flat[i - 1] == arr_flat[i]) {
			counter++;
		}
	}

	cout << "\nTotal unique numbers: " << m * n - counter << "\n";

	for (int i = 0; i < m; i++) {
		delete[] arr[i];
	}
	delete[] arr;
}
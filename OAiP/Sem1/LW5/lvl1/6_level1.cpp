#include <iostream>
#include <math.h>
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

int rowsum(int** arr, int row, int length) {
	int sum = 0;
	for (int i = 0; i < length; i++) {
		sum += arr[row][i];
	}
	return sum;
}

int main() {
	cout << "\nLW5 level 1\n";
	int sum = 0;

	cout << "\nPls unput n, m for array\n\n";
	int m = input_num(), n = input_num();

	int** arr = new int* [m];
	for (int i = 0; i < m; i++) {
		arr[i] = new int[n];
	}

	cout << "\nPls input array elements\n\n";

	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			arr[i][j] = input_num();
		}
	}
	cout << "\nGiven array:\n\n";
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			cout << arr[i][j] << "\t";
		}
		cout << "\n";
	}


	for (int i = 0; i < m; i++) {
		for (int k = 0; k < n; k++) {
			if (arr[i][k] < 0) {
				sum += rowsum(arr, i, n);
				cout << "\nAdding to the sum row " << i + 1;
				break;
			}
		}
		cout << "\n";
	}
	if (sum != 0) cout << "\nThe sum is " << sum << "\n"; else  cout << "\nNo rows with negative numbers found!\n";

	for (int i = 0; i < m; i++) {
		delete[] arr[i];
	}
	delete[] arr;
}
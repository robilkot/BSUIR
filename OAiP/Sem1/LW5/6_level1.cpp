#include <iostream>
#include <math.h>

using namespace std;

int rowsum(int** arr ,int row, int length) {
	int sum = 0;
	for (int i = 0; i < length; i++) {
		sum += arr[row][i];
	}
	return sum;
}

int main1() {
	int m,n;
	int sum = 0;

	cout << "Pls unput n, m for array" << "\n\n";
	cin >> m >> n;

	if (!cin) //numeric check
	{
		cin.clear();
		cin.ignore();
		cout << "\nNon-numeric!\n";
		return 0;
	}

	int** arr = new int *[m];
	for (int i = 0; i < m; i++) {
		arr[i] = new int[n];
	}

	cout << "\nPls input array elements\n\n";

	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			cin >> arr[i][j];
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
				cout << "\nAdding to the sum row " << i+1;
				break;
			}
		}
		cout << "\n";
	}
	if (sum != 0) cout << "The sum is " << sum << "\n"; else  cout << "No such rows found!\n";

	delete[] arr;
}
#include <iostream>
#include <math.h>
#include <algorithm>

using namespace std;

void uniteArrays(int *a1, int size1, int *a2, int size2, int *a3)
{
	int i = 0;
	for (; i < size1; i++) {
		a3[i] = a1[i];
	}
	for (int k=0; k < size2; i++, k++) {
		a3[i] = a2[k];
	}
	sort(a3, a3 + size1 + size2);

	cout << "\nUnited array elements:\n\n";
	for (int k = 0; k < size1 + size2; k++) {
		cout << a3[k] << "\n";
	}
	cout << "\n";
}

void fillArray(int* a1, int size)
{
	for (int i = 0; i < size; i++) {
		a1[i] = rand();
	}
	sort(a1, a1 + size);

	cout << "\nFilled array elements:\n\n";
	for (int i = 0; i < size; i++) {
		cout << a1[i] << "\n";
	}
	cout << "\n";
}

int main3() {
	int arr1s, arr2s;

	cout << "Pls unput X and Y size" << "\n\n";
	cin >> arr1s >> arr2s;

	if (!cin) //numeric check
	{
		cin.clear();
		cin.ignore();
		cout << "\nNon-numeric!\n";
		return 0;
	}

	int* arr1 = new int[arr1s];
	int* arr2 = new int[arr2s];
	int* arr3 = new int[arr1s + arr2s];

	fillArray(arr1, arr1s);
	fillArray(arr2, arr2s);
	uniteArrays(arr1, arr1s, arr2, arr2s, arr3);

	delete[] arr1, arr2, arr3;
}
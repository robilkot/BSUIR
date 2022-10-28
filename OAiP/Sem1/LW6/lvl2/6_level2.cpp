#include <iostream>
#include <conio.h>

using namespace std;

int main() {
	cout << "\nLW6 level 2\n";
	do {
		char inp[256];
		cout << "Pls input string\n\n";
		cin.getline(inp, 256);
		int i = 0, max = strlen(inp);
		for (; i < max; i++) {
			if (isdigit(inp[i]) == 0) {
				for (int k = i; k < max - 1; k++) inp[k] = inp[k + 1];
				i--;
				max--;
			}
		}
		inp[i] = '\0';
		inp[0] == '\0' ? cout << "\nNo number found\n" : cout << "\nThe number is " << inp << "\n";
		cout << "Press q to exit\n";
	} while (_getch() != 'q');
	return 0;
}
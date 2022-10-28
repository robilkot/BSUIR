#include <iostream>
#include <conio.h>

using namespace std;

int main() {
	cout << "\nLW6 level 1\n";
	do {
		char inp[256];
		cout << "Pls input string\n\n";
		cin.getline(inp, 256);
		if (strlen(inp) % 2 == 0 && strlen(inp) > 3) {
			cout << "Deleting first and last 2 symbols\n";
			for (int i = 2; i < strlen(inp); i++) inp[i - 2] = inp[i];
			inp[strlen(inp) - 4] = '\0';
			cout << inp << "\n";
		}
		else {
			cout << "Less than 4 symbols or not even number\n";
		}
		cout << "Press q to exit\n";
	} while (_getch() != 'q');
	return 0;
}
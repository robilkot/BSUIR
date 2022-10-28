#include <iostream>
#include <conio.h>

using namespace std;

int main() {
	cout << "\nLW6 level 3\n";
	do {
		char inp[256];
		cout << "Pls input string\n\n";
		cin.getline(inp, 256);
		char cut[256] = "";
		int spacenum = -1;


		if (strlen(inp) > 15) {
			for (int i = 0; i < 10; i++) {
				cut[i] = inp[i + 4];
			}
			//cout << "Cut string is " << cut << "\n";

			for (int i = strlen(inp); i > 0; i -= 1) {
				if (inp[i] == ' ') {
					spacenum = i;
					break;
				}
			}
			if (spacenum != -1) {
				for (int i = spacenum; i < strlen(inp) - 1; i++) inp[i - spacenum] = inp[i + 1];
				inp[strlen(inp) - spacenum - 1] = '\0';
				cout << "\nThe string is: " << cut << inp << "\n";
			}
			else {
				cout << "\nNo spaces found!\n";
			}
		}
		else {
			cout << "\nLess than 15 symbols!\n";
		}
		cout << "Press q to exit\n";
	} while (_getch() != 'q');
	return 0;
}
#include <iostream>
#include <string>

using namespace std;

int main() {
	cout << "\nLW6 level 3\n";
	string inp;
	char cut[200] = "";
	int spacenum = -1;

	cout << "Pls input string\n";
	getline(cin, inp);

	if (size(inp) > 15) {
		for (int i = 0; i < 10; i++) {
			cut[i] = inp[i + 4];
		}
		//cout << "Cut string is " << cut << "\n";

		for (int i = size(inp); i > 0; i -= 1) {
			if (inp[i] == ' ') {
				spacenum = i;
				break;
			}
		}
		if (spacenum != -1) {
			inp.erase(0, spacenum);
		}
		else {
			cout << "\nNo spaces found!\n";
			return 0;
		}
		cout << "\nThe string is: " << cut + inp << "\n";
	}
	else {
		cout << "\nLess than 15 symbols!\n";
		return 0;
	}
	return 0;
}
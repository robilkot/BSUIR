#include <iostream>
#include <string>

using namespace std;

int main() {
	cout << "\nLW6 level 2\n";
	string inp;
	cout << "Pls input string\n\n";
	cin >> inp;
	for (int i = 0; i < size(inp); ) {
		if (isdigit(inp[i])) {
			i++;
		}
		else {
			inp.erase(i, 1);
		}
	}
	cout << "\nThe number is " << inp << "\n";
	return 0;
}
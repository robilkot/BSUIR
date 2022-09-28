#include <iostream>
#include <string>

using namespace std;

int main1() {
	string inp;
	cout << "Pls input string\n\n";
	cin >> inp;
	if (size(inp) % 2 == 0 && size(inp)>4) {
		cout << "Deleting first and last 2 symbols\n";
		inp.erase(0, 2);
		inp.erase(size(inp)-2, 2);
		cout << inp;
	}
	else {
		cout << "Less than 4 symbols or not even number";
	}
	return 0;
}
#include <iostream>
#include <conio.h>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

void writetofile(string str, string filename) {
	ofstream fout(filename);
	if (fout.is_open()) {
		fout << str;
		fout.close();
		cout << "\nFile " << filename << " succesfully saved.\n";
	}
	else {
		cout << "\nError saving file, pls try again.\n";
	}
}

string readfromfile(string filename) {
	ifstream fin(filename);
	if (fin.is_open()) {
		string output;
		getline(fin, output);
		return output;
	}
	else {
		return "Error opening file, pls try again.\n";
	}
}

string cyfer(string str) {
	vector<char> cyfred;
	if (str.length() == 1) {
		return str;
	}
	for (int i = 0; i < str.size() - 1; i++) {
			if (str[i + 1] == 'i' && (str[i] == 's' || str[i] == 'l' || str[i] == 't')) {
				cyfred.push_back('i');
				cyfred.push_back('i');
				switch (str[i]){
				case 's': cyfred.push_back('s'); break;
				case 'l': cyfred.push_back('l'); break;
				case 't': cyfred.push_back('t'); break;
				}
				i++;
			}
			else {
				cyfred.push_back(str[i]);
			}
	}
	if (!(str[str.length()-2] == 's' || str[str.length() - 2] == 'l' || str[str.length() - 2] == 't') && str[str.length()-1] != 'i') {
		cyfred.push_back(str[str.length()-1]);
	}
	return string(cyfred.begin(), cyfred.end());
}

string decyfer(string str) {
	vector<char> decyfred;

	return string(decyfred.begin(), decyfred.end());
}

int main() {
	string inp;
	do {
		cout << "\nPls type 1 to cyfer smth or other key to decyfer from file.\n";
		if (_getch() == '1') {
			cout << "\nWhat do you want to cyfer today? Pls input string.\n";
			cin >> inp;
			writetofile(cyfer(inp), "cyfer.txt");
		}
		else {
			cout << "\nHere is decyfer from file 'cyfer.txt':\n";
			cout << decyfer(readfromfile("cyfer.txt")) << "\n";
		}
		cout << "\n--- Pls type Q to exit the program ---\n";
	} while (_getch()!='Q');
	return 0;
}
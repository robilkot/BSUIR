#include <iostream>
#include <conio.h>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

void writetofile(string str, const char* filename) {
	ofstream fout(filename);
	if (fout.is_open()) {
		fout << str;
		fout.close();
		cout << "\nFile " << filename << " succesfully saved in project folder.\n";
	}
	else {
		cout << "\nError saving file, try again.\n";
	}
}

string readfromfile(const char* filename) {
	ifstream fin(filename);
	if (fin.is_open()) {
		string output;
		getline(fin, output);
		return output;
	}
	else {
		return "Error opening file, try again.\n";
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
	if (str.length() < 3) {
		return str;
	}
	int i = 0;
	for (; i < str.size(); i++) {
		if (str[i] == 'i' && str[i + 1] == 'i' && (str[i + 2] == 's' || str[i + 2] == 'l' || str[i + 2] == 't')) {
			switch (str[i + 2]) {
			case 's': decyfred.push_back('s'); break;
			case 'l': decyfred.push_back('l'); break;
			case 't': decyfred.push_back('t'); break;
			}
			decyfred.push_back('i');
			//cout << "\nReplaced cyfred symbols at i = " << i << "\n";
			i += 2;
		}
		else {
			//cout << "\nPush last symbol at i = " << i << "\n";
			decyfred.push_back(str[i]);
		}
	}
	return string(decyfred.begin(), decyfred.end());
}

int main() {
	do {
		cout << "\n\nLW7 LVL3 === Type 1 to cyfer string === Type any other key to decyfer from file === FOR EXIT PRESS Q ===\n";
		switch (_getch()) {
		case '1': {
			cout << "\nWhat do you want to cyfer today? Pls input string.\n";
			string inp;
			getline(cin, inp);
			writetofile(cyfer(inp), "cyfer.txt");
			break;
		}
		case 'q':
		case 'Q': return 0;
		default: {
			cout << "\nHere is decyfer from file 'cyfer.txt':\n";
			cout << decyfer(readfromfile("cyfer.txt")) << "\n";
			break;
		}
		}
	} while (true);
}
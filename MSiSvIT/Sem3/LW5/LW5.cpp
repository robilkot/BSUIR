#include <cmath>
#include <iostream>
#include <Windows.h>
using namespace std;

int main() {
    setlocale(LC_ALL, "Russian"); //Локализация
    SetConsoleCP(1251); // ф-ия кодировки на странице(для ввода кирилицы)
    SetConsoleOutputCP(1251);

    int n1, n2, both, i, j;
    int* arr1;
    int* arr2;
    both = 0;

    cout << "введите размеры двух массивов" << '\n';
    cin >> n1 >> n2;

    arr1 = new int[n1]; // Выделение памяти под элементы массива
    arr2 = new int[n2];

    cout << "введите элементы 1ого массива" << '\n';

    for (i = 0; i < n1; i++) {
        cin >> arr1[i];
    }

    cout << "введите элементы 2ого массива" << '\n';

    for (i = 0; i < n2; i++) {
        cin >> arr2[i];
    }

    for (i = 0; i < n1; i++) {
        for (j = 0; j < n2; j++) {
            if (arr1[i] == arr2[j]) {

                switch (i) {
                case 1: {
                    cout << "Eins\n";
                    break;
                }
                case 2: {
                    cout << "Zwei\n";
                    break;
                }
                case 3: {
                    cout << "Drei\n";
                    break;
                }
                default:
                    cout << "Default\n";
                }

                both = both + 1;
            }
        }
    }

    cout << "массив 1: ";

    for (i = 0; i < n1; i++) {
        cout << arr1[i] << " ";
    }

    cout << endl;
    cout << "число одинаковых элементов = " << both << "\n";

    cout << "массив 2: ";

    for (i = 0; i < n2; i++) {
        cout << arr2[i] << " ";
    }

    delete[] arr1;
    delete[] arr2;
}

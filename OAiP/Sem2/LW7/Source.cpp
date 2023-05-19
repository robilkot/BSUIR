#include <iostream>

using namespace std;

long random(long min, long max)
{
	static bool first = true;
	if (first)
	{
		srand(time(NULL));
		first = false;
	}
	return min + rand() % ((max + 1) - min);
}

struct hashTable1 {
	int	capacity = 50,
			size = 0;
	
	int* array = nullptr;

	hashTable1(int capacity) {
		this->capacity = capacity;

		array = new int[this->capacity];

		for (int i = 0; i < this->capacity; i++)
			array[i] = NULL;
	}
	~hashTable1() {
		delete array;
	}

	void show() {
		cout << "Index\t-\tvalue\n";

		for (int i = 0; i < capacity; i++)
			cout << i << "\t-\t" << array[i] << '\n';
	}

	int hashFunction(int key) {
		double A = 0.618033;

		return capacity * fmod(key * A, 1);
	}

	void insert(int key) {
		int index = hashFunction(key);

		bool foundFreeCell = true;

		foundFreeCell = false;

		// Попытка поиска в следующих ячейках
		for (int shift = 0; shift < capacity - index + 1; shift++) {
			if (array[index + shift] == NULL || array[index + shift] == key) {
				index += shift;
				foundFreeCell = true;
				break;
			}
		}	
		// Попытка поиска в предыдущих ячейках
		if (!foundFreeCell) {
			for (int i = 0; i < index - 1; i++) {
				if (array[i] == NULL || array[i] == key) {
					index = i;
					foundFreeCell = true;
					break;
				}
			}
		}

		// Если элемент вставить не удалось
		if (!foundFreeCell) {
			cout << "Failed to insert element (not enough capacity!)\n";
			return;
		}

		if (key == array[index])
			cout << "Rewriting element " << key << " at index " << index << '\n';
		else {
			cout << "Inserting element " << key << " at index " << index << '\n';
			size++;
		}

		array[index] = key;
		return;
	}

	int get(int key) {
		int index = hashFunction(key);

		bool foundElement = true;

		if (array[index] != key) {
			foundElement = false;

			for (int shift = 1; shift < capacity - index + 1; shift++) {
				if (array[index + shift] == key) {
					index += shift;
					foundElement = true;
					break;
				}
			}
			for (int i = 0; i < index - 1; i++) {
				if (array[i] == key) {
					index = i;
					foundElement = true;
					break;
				}
			}
		}

		if (foundElement) {
			cout << "Element with key " << key << " found on index " << index << ".\n";
			return array[index];
		}
		else {
			cout << "Element with key " << key << " not found!\n";
			return 0;
		}
	}
};

const string destinations[5] = { "Minsk", "Moscow", "Barnaul", "Berlin", "France" };

struct Flight {
	string destination = destinations[random(0,4)];
	int number = 0;
	float departure = random(0, 23) + (float)random(0, 60) / 100;

	void show() {
		cout << "Flight number " << number << " departs to " << destination << " at " << departure << "\n";
	}
};

struct hashTable2 {
	const static int capacity = 50;
	int size = 0;

	Flight* array[capacity];

	hashTable2() {
		for (int i = 0; i < capacity; i++) {
			array[i] = nullptr;
		}
	}

	void show() {
		cout << "Index\t-\tfields\n";

		for (int i = 0; i < capacity; i++)
			if (array[i] != nullptr)
				cout << i << "\t-\t" << array[i]->number << "\t-\t" << array[i]->destination << "\t-\t" << array[i]->departure << '\n';
			else
				cout << "--- empty slot ---\n";
	}

	int hashFunction(int key) {
		double A = 0.618033;

		return capacity * fmod(key * A, 1);
	}

	size_t hashFunction2(int key) {
		return hash<int>{}(key);
	}

	void insert(Flight* flight) {
		int key = flight->number;

		size_t index = hashFunction(key);

		bool foundFreeCell = false;

		// Попытка поиска в следующих ячейках
		for (int i = 0; i < capacity; i++) {
			int testIndex = (index + i * hashFunction2(key)) % capacity;

			if (array[testIndex] == nullptr) {
				foundFreeCell = true;
				index = testIndex;
				break;
			}
			else if (array[testIndex]->number == NULL ||
				key == array[testIndex]->number) {
				foundFreeCell = true;
				index = testIndex;
				break;
			}
		}

		// Если элемент вставить не удалось
		if (!foundFreeCell) {
			cout << "Failed to insert element with key " << key << " (not enough capacity!)\n";
			return;
		}

		if (array[index] != nullptr) {
			if (key == array[index]->number)
				cout << "Rewriting element " << key << " at index " << index << '\n';
		}
			else {
				//cout << "Inserting element " << key << " at index " << index << '\n';
				size++;
			}

		array[index] = flight;
		return;
	}

	Flight* get(int key) {
		size_t index = hashFunction(key);

		for (int i = 0; i < capacity; i++) {
			int testIndex = (index + i * hashFunction2(key)) % capacity;

			if (array[testIndex] != nullptr) {
				if (key == array[testIndex]->number) {
					return array[testIndex];
				}
			}
		}

		cout << "Could not find element with key " << key << '\n';
		return nullptr;
	}
};


int main()
{
	//Часть А
	{
		const int keysNumber = 50;

		hashTable1 table(keysNumber);

		int keys[keysNumber];
		for (int i = 0; i < keysNumber; i++) {
			keys[i] = random(32000, 68000);
			table.insert(keys[i]);
		}

		table.show();

		for (int i = 0; i < keysNumber; i++) {
			table.get(keys[i]);
		}
	}
	
	// Часть В
	 {
		 const int keysNumber = 50;

		 hashTable2 table;

		 Flight flights[keysNumber];

		 cout << "Given array of flights:\n";

		 for (int i = 0; i < keysNumber; i++) {
			 flights[i].number = random(10000, 50000);
			 flights[i].show();
			 table.insert(&flights[i]);
		 }

		 cout << "\nHash table of flights:\n";
		 table.show();

		 cout << "\nFinding flights by number:\n";
		 for (int i = 0; i < keysNumber; i++) {
			 Flight* foundFlight = table.get(flights[i].number);
			 if (foundFlight) foundFlight->show();
		 }
	 }
}
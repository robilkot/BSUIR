# Компилятор языка MathLang

# Отчет по лабораторной работе

## Спецификация языка

Язык, описывающий математические вычисления
Встроенные типы: int, float
Операции: +, -, *, \, %, ^, ==, !=, <, >, <=, >=
Встроенные функции log, ln, sin, cos, tan, asin, acos, atan

Объявление переменных явное

Преобразование типов явное, например, a = (int) b

Оператор присваивания многоцелевой, например, a, b = c, d

Структуры, ограничивающие область видимости - подпрограммы

Маркер блочного оператора явный, например, { } или begin end

Условные операторы - двух вариантный оператор if-then-else

Перегрузка подпрограмм присутствует

Передача параметров в подпрограмму по ссылке

Допустимое место объявления подпрограмм в начале программы

Целевой код WAT, текстовое представление WASM

## Синтаксис объявления переменных и подпрограмм

Допускается объявление нескольких переменных за раз. Обязательно указание типа каждой переменной.

Допускается инициализация всех переменных одинаковым значением (если тип всех переменных совпадает),
либо иницилизация каждой переменной собственным значением.

Допускается инициализация любым выражением (в том числе константным).

Объявление переменных без инициализации не допускается.

Тип значения при инициализации должен соответствовать типу переменных. Неявные преобразования не допускаются.

```
float a = 0.0
float b, float c = 5.0 // Все две переменные инициализированы значением 5.0
float d, float e, float f = a  // Все три переменные инициализированы значением переменной a
float g, int h, bool e = 0.0, 2, true  // g = 0.0, h = 2, e = true
```

Объявление подпрограмм допускается в начале файла (обеспечено грамматикой).

Допускается перегрузка подпрограмм (одинаковое имя, разные параметры).

Все параметры в подпрограммы передаются по ссылке.

Синтаксис объявления подпрограммы и примеры: 
```
sub [имя] [ :([Список шаблонных аргументов]) ]? ([Список параметров]) { [Тело подпрограммы] }
```
```
sub computeWave(float x, float result) {
    result = sin(x) + 0.5 * sin(2. * x + 1.0)
}
sub computeWave(float x, float amplitude, float result) {
    result = amplitude * sin(x)
}
```
Возвращаемый тип пользовательских подпрограмм - void.

Стандартные подпрограммы могут возвращать другие типы. Математические подпрограммы (sin, cos, другие) возвращают float. Подпрограмма чтения (read) возвращает тип, указанный в шаблонном аргументе. Подпрограмма преобразования (cast) возвращает тип, указанный во втором шаблонном аргументе.

Допускается использование шаблонных аргументов (1 и более).

Не допускается использование выражений в качестве шаблонных аргументов.

В случае использования шаблонных подпрограмм семантическая проверка внутренних выражений производится по факту вызова при подстановке типов, не при определении подпрограмм.

Допускается явная реализация шаблонной подпрограммы, если присутствует шаблонное определение. При этом обязательно указание типов для всех шаблонных аргументов.

Допускается вызов шаблонных подпрограмм как с явным указанием шаблонных аргументов, так и с неявным (типы определяются автоматически из предоставленных аргументов).

Вызов стандартных подпрограмм преобразования и ввода требуют явного указания всех шаблонных аргументов (2 и 1 соответственно).

```
// Один шаблонный аргумент
sub pretty_write:(T)(T a)
{
    write("Something pretty\n")
    write(a)
    write("\n")
}

// Более одного шаблонного аргумента
sub double_template:(K, V)(K key, V value)
{
    V key_casted = cast:(K, V)(key) // Явное указание шаблонных аргументов при вызове
}


sub inner_initialization:(T)(T result)
{
    T intermediate_result = read:(T)() // Инициализация переменной шаблонного типа
    result = intermediate_result * cast:(float, T)(2.0)
}


// When defining templated subprogram, it is possible to manually provide custom implementation for specific types ...
sub explicit_implementation:(T)(T val)
{
    write("Arbitrary type")
    write(val)
    write("\n")
}

 // Явное определение шаблонной подпрограммы для конкретного типа
sub explicit_implementation:(int)(int val)
{
    write("Specifically for int!")
    write(val)
    write("\n")
}
```


## Синтаксис операций над данными

Значения переменных возможно изменять операцией присвоения выражения.

Выражением может выступать константа, ссылка на переменную, составное выражение, вызов подпрограммы.

Примеры операций над данными:
```
sub isRightTriangle(float a, float b, float c, bool result) {
	result = (a^2. + b^2. == c^2.) or (a^2. + c^2. == b^2.) or (b^2. + c^2. == a^2.) // Сложное математическое выражение со скобками
}

float cathetusA = read:(float)() // Вызов стандартной шаблонной подпрограммы
float cathetusB = read:(float)()

float area, float hypotenuse = 0.0 // Присвоение константы
area = cathetusA * cathetusB / 2.0 // Сложное математическое выражение

int roundedHypotenuse = cast:(float, int)(hypotenuse) // Преобразование
sub recursion:(T, K)(T val1, K val2)
{
    write(val1)
    write("\n")
    write(val2)
    write("\n")

    if (val2 > cast:(int, K)(5)) // Вызов подпрограмм с аргументами-литералами
    {
        return
    }

    val2 = val2 + cast:(int, K)(1)

    recursion(val2, val1) // Операции над шаблонными типами. Валидируются при подстановке типов (при вызове подпрограммы)
}

recursion(1.5, 2) 
```

## Синтаксис всех управляющих конструкций

### Оператор ветвления if-else

Требует выражения типа bool в условии

```
sub test(float c) {
    c = c * 2.0

    if(c > 100.0)
    {
        write("exiting recursion after c > 100\n")
        write(100500)
        write("\n")
    }
    else
    {
        test(c)
    }
}
```

### Оператор цикла for

Требует выражения типа bool в условии. Допускает не более одной операции в шаге.

```
for (float angle = 0.0; angle <= 6.28318; angle = angle + 0.1) {
    float result = 0.
	  computeWave(angle, result)

    write("sin(")
    write(angle)
    write(") = ")
    write(result)
    write("\n")
}
```


### Оператор цикла while

Требует выражения типа bool в условии

```
while(abs(sin(x) - target) > precision) {
    x = x + 0.01
    if (x > 10.0) { // Infinite loop guard
        break
    }
}
```

### Оператор цикла until

Требует выражения типа bool в условии

```
int x = 0
until(x == 10) {
  x = x + 1
	write(x)
}
```

Все циклы допускают применение в теле break, continue.

Допускается return в подпрограммах. Return в глобальной области видимости не допускается.

## Файл грамматики

Файл грамматики доступен по адресу grammar/MathLang.g4

## Перечень дополнительных классов

## Перечень генерируемых ошибок

Все семантические ошибки в удобном для чтения виде описаны в файле src/models/error_formatter.py

Список семантических ошибок:

- Нельзя присвоить значение типа {from_type} переменной типа {to_type}'
- Количество выражений (при присвоении) должно совпадать с количеством переменных или быть равным 1
- Символ {symbol} уже определен в этой области видимости
- Символ {symbol_id} не определен
- Символ {symbol_id} не определен в глобальной области видимости
- Подпрограмма {subprogram_id} не определена
- Глобальная переменная {symbol_id} вне подпрограммы не инициализирована
- Не найдено перегрузки {sub_name} с параметрами {params_string}
- Бинарный оператор '{operator}' применим только к {type_description}. Получены типы {left_type}, {right_type}"
- Унарный оператор '{operator}' применим только к {type_description}. Получен тип {actual_type}
- Оператор return может использоваться только внутри подпрограмм
- Операторы continue и break могут использоваться только внутри циклов
- Ожидался булев тип в условии. Получен {actual_type}
- Невозможно преобразовать {from_type} в {to_type}"
- Неиспользованный шаблонный аргумент {arg}"
- Требуется аргументов: {expected}. Получено аргументов: {actual}.
- Ожидался тип {expected}. Получен {actual}.
- Шаблонный аргумент {template_arg_type} не определен
- Тип {type} не определен
- Тип шаблонного аргумента {typ} не указан при явной реализации
- Явная реализация {sub_name} не допускается до шаблонного объявления подпрограммы
- Аргумент подпрограммы не соответствует типу шаблонного аргумента. Ожидался {expected}, получен {actual}
- Использование строк в качестве операндов не поддерживается языком

## Примеры работы компилятора

В папке samples представлены примеры исходного кода и полученных исполняемых файлов, а также промежуточного кода на WAT. 

Описания примеров:

- sample1: запрашивает у пользователя катеты прямоугольного треугольника, рассчитывает гипотенузу и другие характеристики треугольника
```
// Declaration above other stuff:
sub calculateHypotenuse(float a, float b, float result) {
	result = (a^2. + b^2.)^0.5
}

sub isRightTriangle(float a, float b, float c, bool result) {
	result = (a^2. + b^2. == c^2.) or (a^2. + c^2. == b^2.) or (b^2. + c^2. == a^2.)
}

sub usingGlobalStuff() {
	global float global_var1, float global_var2, int global_var3 = 2.0, 2.0, 2
	global_var1 = 3.0

	global_var2 = 3.0
	
	write(global_var3) // 2.0
    write("\n")
}

// Start of program
int counter = 0
float cathetusA, float cathetusB = 0.0

write("Enter the first cathetus:\n")
cathetusA = read:(float)()
write("Enter the second cathetus:\n")
cathetusB = read:(float)()

// Compound assignment
float area, float hypotenuse = 0.0
area = cathetusA * cathetusB / 2.0
calculateHypotenuse(cathetusA, cathetusB, hypotenuse)

// Branching operator
if (hypotenuse > 10.0) {
	write("Large triangle.\n")
} else {
	write("Small triangle.\n")
}

write("Area: ")
write(area)
write(", Hypotenuse: ")
write(hypotenuse)
write("\n")

// Type conversion
int roundedHypotenuse = cast:(float, int)(hypotenuse)
write("Rounded hypotenuse: ")
write(roundedHypotenuse)
write("\n")

bool isRight = false
isRightTriangle(cathetusA, cathetusB, hypotenuse, isRight)
write("Is right triangle? ")
write(isRight)
write("\n")
```

<img width="361" height="253" alt="image" src="https://github.com/user-attachments/assets/2fb0e94e-9186-4067-ab80-b38c88f68b3b" />

- sample2: рассчитывает значения составного тригонометрического выражения, аппроксимирует значение аргумента по значению функции с заданной точностью. Проверяет аксиому (sin^2(x) + cos^2(x) = 1)

```
// Function overloading
sub computeWave(float x, float result) {
    result = sin(x) + 0.5 * sin(2. * x + 1.0)
}

// Function overloading example
sub computeWave(float x, float amplitude, float result) {
    result = amplitude * sin(x)
}

// Start of program
write("Calculating sine wave values from 0 to 2*PI:\n")

// For loop
for (float angle = 0.0; angle <= 6.28318; angle = angle + 0.1) {
    float result = 0.
	computeWave(angle, result)

    write("sin(")
    write(angle)
    write(") = ")
    write(result)
    write("\n")
}

// While loop
float x = 0.0
float precision = 0.001
float target = 0.5

write("\nFinding solution for sin(x) = 0.5\n")

while(abs(sin(x) - target) > precision) {
    x = x + 0.01
    if (x > 10.0) { // Infinite loop guard
        break
    }
}

write("Solution found: x = ")
write(x)
write(", sin(x) = ")
write(sin(x))
write("\n")

float result = (cos(x) ^ 2.) + (sin(x) ^ 2.) // Should be ≈1
write("sin^2(x) + cos^2(x) = ")
write(result)
write("\n")
```


<img width="419" height="711" alt="image" src="https://github.com/user-attachments/assets/f62d7289-af78-4096-a0e8-ede9e0bc80e1" />

- sample4: решает квадратное уравнение с заданными коэффициентами методом дискриминанта. Проверяет вычисленные решения.

```
sub solveQuadratic(float a, float b, float c, float root1, float root2, bool result) {
    float discriminant = b^2. - 4.*a*c
    
    if (discriminant < 0.) {
        result = false // No roots found
    }
    
    root1 = (-b + discriminant^0.5) / (2.*a)
    root2 = (-b - discriminant^0.5) / (2.*a)
    
	result = true
}

float a, float b, float c = 1.0, -5.0, 6.0
float root1, float root2 = 0.0
float test, float test2 = 0.5


bool result = false
solveQuadratic(a, b, c, root1, root2, result)
if (result) {
    write("Roots of equation ")
    write(a)
    write("x^2 + ")
    write(b)
    write("x + ")
    write(c)
    write(" = 0 are:")
    write("Root 1: ")
    write(root1)
    write(", Root 2: ")
    write(root2)
    write("\n")
    
    float check1 = a*(root1^2.) + b*root1 + c
    float check2 = a*(root2^2.) + b*root2 + c
    write("Verification (should be close to 0): ")
    write(check1)
    write(" and ")
    write(check2)
    write("\n")
} else {
    write("No real roots found\n")
}

bool isPositive = (root1 > 0.) and (root2 > 0.)
write("Both roots are positive: ")
write(isPositive)
write("\n")

```

<img width="789" height="77" alt="image" src="https://github.com/user-attachments/assets/062e6708-9a5a-4e8c-a7a0-c287a6f90d44" />

- sample6: рекурсивно возводит число в степень до достижения порога. Выводит сообщения при каждом вызове.

```
sub test(float c) {
    c = c * 2.0

    write(c)
    write("\n")
    if(c > 100.0)
    {
        write("exiting recursion after c > 100\n")
        write(100500)
        write("\n")
    }
    else
    {
        test(c)
    }
}

for(int i = 0; i < 10; i = i + 1)
{
    write(sin(cast:(int, float)(i)))
    write("\n")
}

write("recursive sub:\n")
test(5.0)

```

<img width="789" height="185" alt="image" src="https://github.com/user-attachments/assets/6b9b380a-6336-4573-9ab3-696fcb39d95d" />

- sample7: шаблонная рекурсивная подпрограмма, с каждым вызовом инкрементирующая аргументы, переданные по ссылке. Порядок аргументов с каждым вызовом меняется для проверки корректности разрешения шаблонов.

```
sub recursion:(T, K)(T val1, K val2)
{
    write(val1)
    write("\n")
    write(val2)
    write("\n")

    if (val2 > cast:(int, K)(5))
    {
        return
    }

    val2 = val2 + cast:(int, K)(1)

    recursion(val2, val1)
}

recursion(1.5, 2)
```

<img width="140" height="405" alt="image" src="https://github.com/user-attachments/assets/ae8b532c-31e1-4393-bd2d-19ef099bb495" />

- sample8: песочница, повторяет другие примеры
- samples_templates: песочница для шаблонных подпрограмм, содержит все виды ошибок и примеры использования шаблонов
- samples_templates_correct.ml: аналогично предыдущему, но без ошибок

```
// CORRECT SAMPLES


// Using one template argument
sub pretty_write:(T)(T a)
{
    write("Something pretty\n")
    write(a)
    write("\n")
}

// Using two or more template arguments
sub double_template:(K, V)(K key, V value)
{
    V key_casted = cast:(K, V)(key)
}

// Variables of templated types may be created in subprogram
sub inner_initialization:(T)(T result)
{
    T intermediate_result = read:(T)()
    result = intermediate_result * cast:(float, T)(2.0)
}

sub call_to_templated_sub:(T)(T val)
{
    pretty_write(val)

    // Providing template argument explicitly is allowed in call statement
    int i_val = cast:(T, int)(val)
    pretty_write:(int)(i_val)
}

// When defining templated subprogram, it is possible to manually provide custom implementation for specific types ...
sub explicit_implementation:(T)(T val)
{
    write("Arbitrary type")
    write(val)
    write("\n")
}

// ... This requires definition of templated subprogram before
sub explicit_implementation:(int)(int val)
{
    write("Specifically for int!")
    write(val)
    write("\n")
}

sub recursion:(T)(T val, int result)
{
    int res = cast:(T, int)(val)

    if(result > 10)
    {
        return
    }

    result = result + 1

    recursion(val, result)
}

// Sample calling code
inner_initialization(2)
inner_initialization(2.0)

explicit_implementation(2)
explicit_implementation(2.0)

call_to_templated_sub(2)
call_to_templated_sub(2.0)
// call_to_templated_sub("dsd")

float input_float = 0.0
int a = cast:(float, int)(read:(float)())
inner_initialization(2)
inner_initialization(2.0)
//inner_initialization("dsd")
inner_initialization(2)

int res = 0
write("result before recursion: ")
write(res)
write("\n")
recursion(2, res)
write("result after recursion: ")
write(res)
write("\n")

double_template(2, 4.0)
double_template(2, true)
double_template(false, true)
```

<img width="291" height="407" alt="image" src="https://github.com/user-attachments/assets/ca6517c6-3c48-47de-a645-799a6baacf83" />



## Установка и запуск

В репозиторий залита зависимость wabt-1.0.39 для компиляции WAT в WASM. Для запуска на ОС кроме Linux необходимо вручную скачать нужную версию из репозитория разработчиков: https://github.com/WebAssembly/wabt/releases 

Установите зависимости для Python.
```
./setup.sh
```
Запустите toolchain на файле с кодом MathLang.
```
source .venv/bin/activate
python toolchain.py samples/sample1.ml
```
Toolchain сгенерирует исполняемые файлы на WASM + JS, а также промежуточный код на WAT.
В случае ошибок компиляция остановится, будут выведены сообщения об ошибках.

Для запуска исполняемых файлов рекомендуется использовать node.js. Для корректной работы ввода через терминал требуются зависимости.

Установите зависимости для JS.
```
npm install
```
Запустите сгенерированный исполняемый файл.
```
node samples/sample1.js
```

Готово!

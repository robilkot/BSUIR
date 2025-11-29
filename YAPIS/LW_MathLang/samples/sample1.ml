// Declaration above other stuff:
sub calculateHypotenuse(float a, float b, float result) {
	result = (a^2 + b^2)^0.5
}

sub isRightTriangle(float a, float b, float c, bool result) {
	result = (a^2 + b^2 == c^2) or (a^2 + c^2 == b^2) or (b^2 + c^2 == a^2)
}

sub usingGlobalStuff() {
	global float global_var1, float global_var2, int global_var3 = 2.0
	global_var1 = 3.0

	global_var2 = 3.0
	
	write(global_var3) // 2.0
}

// Start of program
int counter = 0
float cathetusA, float cathetusB = 0.0

write("Enter the first cathetus: ")
cathetusA = read()
write("Enter the second cathetus: ")
cathetusB = read()

// Compound assignment
float area, float hypotenuse = 0.0
area = cathetusA * cathetusB / 2.0
calculateHypotenuse(cathetusA, cathetusB, hypotenuse)

// Branching operator
if (hypotenuse > 10.0) {
	write("Large triangle. ")
} else {
	write("Small triangle. ")
}

write("Area: ")
write(area)
write(", Hypotenuse: ")
write(hypotenuse)

// Type conversion
int roundedHypotenuse = cast(hypotenuse)
write("Rounded hypotenuse: ")
write(roundedHypotenuse)

bool isRight = false
isRightTriangle(cathetusA, cathetusB, hypotenuse, isRight)
write("Is right triangle? ")
write(isRight)

// until loop
int x = 0
until(x == 10) {
	write(x + 1)
}

float global_var1 = 2.0
float global_var2 = 2.0
float global_var3 = 2.0

write(global_var1) // 3.0
write(global_var2) // 2.0


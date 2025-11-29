// Pass parameters by reference
sub findMinMax(float a, float b, float min, float max) {
    if (a < b) {
        min, max = a, b
    } else {
        min, max = b, a
    }
}

sub swap(float x, float y) {
    float temp = x
    x = y
    y = temp
}

sub solveQuadratic(float a, float b, float c, float root1, float root2, bool result) {
    float discriminant = b^2 - 4*a*c
    
    if (discriminant < 0) {
        result = false // No roots found
    }
    
    root1 = (-b + discriminant^0.5) / (2*a)
    root2 = (-b - discriminant^0.5) / (2*a)
    
	result = true
}

// Start of program
float num1 = 15.7
float num2 = 8.3
float minimum, float maximum = 0.0

{{{{
    findMinMax(num1, num2, minimum, maximum)
    
    {
        findMinMax(num1, num2, minimum, maximum)
    }
}}}}

write("Min: ")
write(minimum)
write(", Max: ")
write(maximum)

write("Before swap: num1 = ")
write(num1)
write(", num2 = ")
write(num2)

num1, num2 = num2, num1

write("After swap: num1 = ")
write(num1)
write(", num2 = ")
write(num2)

float a = 1.0, float b = -5.0, float c = 6.0
float root1, float root2 = 0.0, 0.0
float test, float test2 = 0.5, 0.5
test, test2 = 0.2, 0.7


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
    
    float check1 = a*(root1^2) + b*root1 + c
    float check2 = a*(root2^2) + b*root2 + c
    write("Verification (should be close to 0): ")
    write(check1)
    write(" and ")
    write(check2)
} else {
    write("No real roots found")
}

bool isPositive = (root1 > 0) and (root2 > 0)
write("Both roots are positive: ")
write(isPositive)

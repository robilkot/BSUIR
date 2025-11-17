// Function overloading
sub computeWave(float x, float result) {
    result = sin(x) + 0.5 * sin(2*x + 1.0)
}

// Function overloading example
sub computeWave(float x, float amplitude, float result) {
    result = amplitude * sin(x)
}

// Start of program
write("Calculating sine wave values from 0 to 2*PI:\n")

// For loop
for (float angle = 0.0; angle <= 6.28318; angle = angle + 0.1) {
    float result = 0
	computeWave(angle, result)

    write("sin(", angle, ") = ", result)
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

write("Solution found: x ≈ ", x, ", sin(x) ≈ ", sin(x))

float result = (cos(x) ^ 2) + (sin(x) ^ 2) // Should be ≈1
write("sin^2(x) + cos^2(x) = ", result)


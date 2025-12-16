sub solveQuadratic(float a, float b, float c, float root1, float root2, bool result) {
    float discriminant = b^2. - 4.*a*c

    if (discriminant < 0.) {
        result = false // No roots found
    }

    root1 = (-b + discriminant^0.5) / (2.*a)
    root2 = (-b - discriminant^0.5) / (2.*a)

	result = true
}

float b = 0.0
bool result = false
solveQuadratic(b, b, b, b, b, result)
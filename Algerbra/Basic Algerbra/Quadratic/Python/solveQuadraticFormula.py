from cmath import sqrt
# Solve with quadratic equation
def solveQuadratic(a, b, c):
    discr = b**2 - 4*a*c # discriminant
    root1 = (-b + sqrt(discr)) / (2*a)
    root2 = (-b - sqrt(discr)) / (2*a)
    return root1, root2

# Coefficients of the quadratic equation
a, b, c = 1, -3, 2

roots = solveQuadratic(a, b, c)
print("Quadratic Formula Roots:", roots)

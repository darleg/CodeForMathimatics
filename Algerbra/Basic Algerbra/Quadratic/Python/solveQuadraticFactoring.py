# Sove quadratic by factoring
def solveQuadraticFactoring(a, b, c):
    discr = b**2 - 4*a*c
    if discr < 0:
        return "No real roots"
    if discr == 0:
        root = -b / (2 * a)
        return (root, root)
    if discr > 0:
        root1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
        root2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
        return (root1, root2)

# Coefficients
a, b, c = 1, -3, 2

roots = solveQuadraticFactoring(a, b, c)
print("Factoring Method Roots:", roots)

from sympy import symbols, Eq, solve

def solveQuadraticSympy(a, b, c):
    x = symbols('x')
    equation = Eq(a*x**2 + b*x + c, 0)
    roots = solve(equation, x)
    return roots

# Coefficients
a, b, c = 1, -3, 2

roots = solveQuadraticSympy(a, b, c)
print("SymPy Roots:", roots)

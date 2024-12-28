import numpy as np

def solveQuadraticNumpy(a, b, c):
    coef = [a, b, c]
    roots = np.roots(coef)
    return roots

# Coefficients
a, b, c = 1, -3, 2

roots = solveQuadraticNumpy(a, b, c)
print("NumPy Roots:", roots)

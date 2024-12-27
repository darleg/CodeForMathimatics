from numpy import poly1d, polyint

# Define the polynomial coefficients (2x^2 - 4x + 3)
coef = [2, -4, 3]
# Create a polynomial object
p = poly1d(coef)
# Integrate the polynomial
intPoly = polyint(p)
print("Integral of the Polynomial:")
print(intPoly)

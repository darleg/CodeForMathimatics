from numpy import poly1d, polyder

# Define the polynomial coefficients (2x^2 - 4x + 3)
coef = [2, -4, 3]
# Create a polynomial object
p = poly1d(coef)
# Differentiate the polynomial
derPoly = polyder(p)
print("Derivative of the Polynomial:")
print(derPoly)

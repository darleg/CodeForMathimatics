from numpy import poly1d, roots

# Define the polynomial coefficients (2x^2 - 4x + 3)
coef = [2, -4, 3]
# Create a polynomial object
p = poly1d(coef)
# Find the roots of the polynomial
r = roots(p)
print("Roots of the Polynomial:")
print(r)

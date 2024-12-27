from numpy import poly1d

# Define the polynomial coefficients (2x^3 - 4x^2 + 3x - 5)
coef = [2, -4, 3, -5]
# Create a polynomial object
p = poly1d(coef)
# Print the polynomial
print("Polynomial:")
print(p)
# Evaluate the polynomial at a specific value (x = 2)
value = 2
print(f"\nValue of the polynomial at x = {value}:")
print(p(value))

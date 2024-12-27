from numpy import poly1d, polymul

# Define the coefficients of two polynomials
p1 = poly1d([2, -4, 3])  # 2x^2 - 4x + 3
p2 = poly1d([1, 0, -1])  # x^2 - 1
# Multiply the polynomials
prodPoly = polymul(p1, p2)
print("Product of the polynomials p1 and p2:")
print(poly1d(prodPoly))

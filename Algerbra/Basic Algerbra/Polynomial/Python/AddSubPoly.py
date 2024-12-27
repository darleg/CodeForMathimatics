from numpy import poly1d, polyadd, polysub

# Define the coefficients of two polynomials
p1 = poly1d([2, -4, 3])  # 2x^2 - 4x + 3
p2 = poly1d([1, 2, -1])  # x^2 + 2x - 1
# Add the polynomials
sumPoly = polyadd(p1, p2)
print("Sum of the polynomials p1 and p2:")
print(poly1d(sumPoly))
# Subtract the polynomials
diffPoly = polysub(p1, p2)
print("\nDifference of the polynomials p1 and p2:")
print(poly1d(diffPoly))

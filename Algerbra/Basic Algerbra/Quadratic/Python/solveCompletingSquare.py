# Solve qudratic by completing the square
def completingSquare(a, b, c):
    if a != 1:  # Make the coefficient of x^2 to be 1
        a, b, c = 1, b / a, c / a
    xVertex = -b / 2
    yVertex = c - (b ** 2 / 4)
    r1 = xVertex + (-yVertex) ** 0.5
    r2 = xVertex - (-yVertex) ** 0.5
    return (r1, r2)

# Coefficients
a, b, c = 1, -3, 2

roots = completingSquare(a, b, c)
print("Completing the Square Roots:", roots)

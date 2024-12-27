from numpy import poly1d, linspace, roots
from pylab import plot, xlabel, ylabel, title, axhline, axvline, grid, legend, show

# Define the polynomial coefficients
# For example, 3x^2 + 2x - 5
coefficients = [3, 2, -5]
# Create a polynomial object
p = poly1d(coefficients)
# Print the polynomial
print("Polynomial:")
print(p)
# Evaluate the polynomial at a specific value (e.g., x = 2)
value = 2
print(f"\nValue of the polynomial at x = {value}:")
print(p(value))

# Find the roots of the polynomial
r = roots(p)
print("\nRoots of the polynomial:")
print(r)

# Plot the polynomial
xrange = linspace(-4, 4, 400)
yrange = p(xrange)

plot(xrange, yrange, label=str(p))
xlabel('x')
ylabel('y')
title('Polynomial Plot')
axhline(0, color='black', linewidth=0.5)
axvline(0, color='black', linewidth=0.5)
grid(True, linestyle='--', alpha=0.7)
legend()
show()

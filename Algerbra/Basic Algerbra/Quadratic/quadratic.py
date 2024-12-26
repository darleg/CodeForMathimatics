from numpy import sqrt, linspace
from pylab import plot, axhline, axvline, scatter, grid, xlabel, ylabel, title, legend, show

# Coefficients of the quadratic equation ax^2 + bx + c = 0
a = 1
b = -3
c = 2
# Calculate the roots using the quadratic formula
discriminant = b**2 - 4*a*c
r1 = (-b + sqrt(discriminant)) / (2*a)
r2 = (-b - sqrt(discriminant)) / (2*a)
print("Roots:", r1, r2)
# Define the quadratic function
def quadratic_function(x):
    return a*x**2 + b*x + c
# Create an array of x values
xrange = linspace(0, 3, 400)
yrange = quadratic_function(xrange)
# Plot the quadratic function
plot(xrange, yrange, label=f'{a}x^2 + {b}x + {c}')
axhline(0, color='black', linewidth=0.5)
axvline(0, color='black', linewidth=0.5)
scatter([r1, r2], [0, 0], color='red')  # Plot the roots
grid(True, linestyle='--', alpha=0.7)
xlabel('x')
ylabel('y')
title('Graph of the Quadratic Equation')
legend()
show()

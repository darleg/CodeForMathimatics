from numpy import linspace, exp, tanh, sinh, cosh
from pylab import plot, xlabel, ylabel, title, legend, grid, show

# Generate data points
x = linspace(-2, 2, 100)
# Plot the function
y = sinh(x)
plot(x, y, label='Sinh Function')
y = cosh(x)
plot(x, y, label='Cosh Function')
y = tanh(x)
plot(x, y, label='Tanh Function')
xlabel('x')
ylabel('f(x)')
title('Hyperbolic Functions')
legend()
grid(True)
show()

from numpy import linspace, sin, cos, tan, pi
from pylab import figure, plot, ylim, xlabel, ylabel, title, legend, grid, axhline, axvline, show


# Define the range of x values
x = linspace(-2 * pi, 2 * pi, 200)
# Limit the y-axes
ylim(-3, 3)
# Plotting the sine function
y = sin(x)
plot(x, y, label='sin(x)', color='red')
y = cos(x)
plot(x, y, label='cos(x)', color='blue')
y = tan(x)
plot(x, y, label='tan(x)', color='green')
# Adding labels and title
xlabel('x')
ylabel('trigonometric functions')
title('Plotting of trigonometric functions')
legend()

# Show the plot
grid(True)
axhline(0, color='black', linewidth=0.5)
axvline(0, color='black', linewidth=0.5)
show()

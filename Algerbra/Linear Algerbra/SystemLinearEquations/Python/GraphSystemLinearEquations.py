from numpy import linspace
from pylab import plot, xlabel, ylabel, title, axhline, axvline, grid, legend, show

# Define the equations
def eq1(x):
    return (6 - 2*x) / 3

def eq2(x):
    return (x + 3) / 4

# Create an array of x values
xrange = linspace(-5, 5, 400)

# Calculate y values for each equation
yeq1 = eq1(xrange)
yeq2 = eq2(xrange)

# Plot the equations
plot(xrange, yeq1, label='2x + 3y = 6')
plot(xrange, yeq2, label='x - 4y = -3')

# Add labels and title
xlabel('x')
ylabel('y')
title('Solving a System of Linear Equations by Graphing')
axhline(0, color='black', linewidth=0.5)
axvline(0, color='black', linewidth=0.5)
grid(True, linestyle='--', alpha=0.7)
legend()

# Show the plot
show()

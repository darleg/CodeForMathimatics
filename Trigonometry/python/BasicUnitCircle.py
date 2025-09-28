from numpy import linspace, sin, cos, pi
from pylab import figure, plot, ylim, xlabel, ylabel, title, legend, grid, axhline, axvline, gca, show

# Generate points for the unit circle
theta = linspace(0, 2 * pi, 500)  # Angle from 0 to 2π
x = cos(theta)  # x = cos(θ)
y = sin(theta)  # y = sin(θ)

# Plot the circ
figure(figsize=(6, 6))
plot(x, y, label='Unit Circle')

axhline(0, color='green')  # x-axis
axvline(0, color='green')  # y-axis
gca().set_aspect('equal', adjustable='box')  # Equal aspect ratio
title("Basic Unit Circle")
xlabel("x")
ylabel("y")
legend()
grid()
show()

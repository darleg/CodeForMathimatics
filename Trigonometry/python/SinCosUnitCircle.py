from numpy import linspace, sin, cos, pi
from pylab import figure, plot, ylim, xlabel, ylabel, title, text, legend, grid, axhline, axvline, gca, show

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
title("Sine and Cosine Ratios within the Unit Circle")
xlabel("x")
ylabel("y")
grid()

# theta = pi/3
theta = pi/4
# theta = pi/6

px1 = cos(theta)
py1 = sin(theta)

rx = [0, cos(theta)]
ry = [0, sin(theta)]

plot(rx, ry, label = 'r', color = 'orange')
plot(px1, py1, marker = 'o', color = 'orange')
text(.2,.4,'r = 1')

sinx = [cos(theta), cos(theta)]
siny = [sin(theta), 0]
plot(sinx, siny, label = 'sine', color = 'red')
text(.77, .25,'sin')

cosx = [0, cos(theta)]
cosy = [sin(theta), sin(theta)]
plot(cosx, cosy, label = 'cosine', color = 'yellow')
text(.26, .6,'cos')


legend(loc = 'upper left')
show()

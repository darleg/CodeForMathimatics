from numpy import linspace, sin, cos, pi
from pylab import figure, plot, ylim, xlabel, ylabel, title, text, xlim, ylim, legend, grid, axhline, axvline, gca, show

# Generate points for the unit circle
theta = linspace(0, 2 * pi, 500)  # Angle from 0 to 2π
x = cos(theta)  # x = cos(θ)
y = sin(theta)  # y = sin(θ)

# Plot the circ
figure(figsize=(6, 6))
title('Trigonometric Functions Ratios')
plot(x, y, label= 'Unit Cirle')

axhline(0, color='black')  # x-axis
axvline(0, color='black')  # y-axis
gca().set_aspect('equal', adjustable='box')  # Equal aspect ratio
xlabel("x")
ylabel("y")
xlim(-2, 2)
ylim(-2, 2)

# theta = pi/3
# theta = pi/4
theta = pi/6

px1 = cos(theta)
py1 = sin(theta)

rx = [0, cos(theta)]
ry = [0, sin(theta)]

plot(rx, ry, label = 'r', color = 'orange')
plot(px1, py1, marker = 'o', color = 'orange')

sinx = [cos(theta), cos(theta)]
siny = [sin(theta), 0]
plot(sinx, siny, label = 'sine', color = 'red')

cosx = [0, cos(theta)]
cosy = [sin(theta), sin(theta)]
plot(cosx, cosy, label = 'cosine', color = 'yellow')

x1 = 1/cos(theta)
y1 = 0
secx = [0, 1/cos(theta)]
secy = [0, 0]
p3 = [x1, y1] 
plot(secx, secy, label = 'secant', color = 'green')
plot(x1, y1, marker = 'o', color = 'green')

x2 = 0
y2 = 1/sin(theta)
cscx = [0, 0]
cscy = [0, 1/sin(theta)]
p4 = [x2, y2]
plot(cscx, cscy, label = 'cosecant', color = 'blue')
plot(x2, y2, marker = 'o', color = 'blue')

tanx = [cos(theta), 1/cos(theta)]
tany = [sin(theta), 0]
plot(tanx, tany, label = 'tangent', color = 'pink')

cotx = [cos(theta), 0]
coty = [sin(theta), 1/sin(theta)]
plot(cotx, coty, label = 'cotangent', color = 'purple')

legend(loc = 'upper left')
show()

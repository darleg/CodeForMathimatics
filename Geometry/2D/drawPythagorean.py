from pylab import figure, plot, xlabel, ylabel, title, legend, grid, text, axhline, axvline, gca, show
import numpy as np

# Coordinates of the vertices of the right triangle
A = (0, 0)
B = (3, 0)
C = (3, 4)
# Plotting the right triangle
figure(figsize=(6, 8))
plot([A[0], B[0]], [A[1], B[1]], 'bo-', label='Opposit a (3 units)')
plot([B[0], C[0]], [B[1], C[1]], 'bo-', label='Adjacent b (4 units)')
plot([C[0], A[0]], [C[1], A[1]], 'bo-', label='Hypotenuse c (5 units)')
# Adding labels and title
text(A[0], A[1], 'A (0,0)', fontsize=12, ha='right')
text(B[0], B[1], 'B (3,0)', fontsize=12, ha='left')
text(C[0], C[1], 'C (3,4)', fontsize=12, ha='right')
xlabel('x')
ylabel('y')
title('Right Triangle and Pythagorean Theorem')
# Showing the Pythagorean Theorem properties and equations
text(0.2, 3, '$a^2 + b^2 = c^2$', fontsize=14, color='red')
text(0.2, 2.5, '$3^2 + 4^2 = 5^2$', fontsize=14, color='red')
text(1.7, 2, '$a = Opposit$', fontsize=14, color='green')
text(1.7, 1.5, '$b = Adjacent$', fontsize=14, color='green')
text(1.7, 1, '$c = Hypotenuse$', fontsize=14, color='green')
# Displaying the grid and axes
grid(True)
axhline(0, color='black', linewidth=0.5)
axvline(0, color='black', linewidth=0.5)
# Aspect ratio to make sure the plot is not skewed
gca().set_aspect('equal', adjustable='box')
legend()
# Show the plot
show()

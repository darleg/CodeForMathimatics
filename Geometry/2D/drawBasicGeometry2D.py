from pylab import figure, subplots, Rectangle, Polygon, Circle, plot, xlabel, ylabel, title, grid, text, axhline, axvline, show
import numpy as np

# Create a new figure
fig, ax = subplots()
# Square
square = Rectangle((0.1, 0.7), 0.2, 0.2, color='green', fill=False)
ax.add_patch(square)
# Triangle
triangle = Polygon([[0.1, 0.4], [0.3, 0.4], [0.2, 0.6]], color='red', fill=False)
ax.add_patch(triangle)
# Circle
circle = Circle((0.2, 0.2), 0.1, color='blue', fill=False)
ax.add_patch(circle)
# Adding labels and title
title('Basic Geometry Shapes 2D')
text(0.5, 0.8, 'Square', fontsize=14, color='green')
text(0.5, 0.5, 'Triangle', fontsize=14, color='red')
text(0.5, 0.2, 'Circle', fontsize=14, color='blue')
# Set the limits of the plot
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
# Set aspect ratio to be equal
ax.set_aspect('equal')
# Hide the axes
ax.axis('off')
# Show plot
show()

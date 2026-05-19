import numpy as np
import matplotlib.pyplot as plt
from math import comb

def bezier_curve(t, points):
    # points: List of control points (e.g., [[x0,y0], [x1,y1], ...])
    n = len(points) - 1
    curve = np.zeros((len(t), 2))
    for i, _t in enumerate(t):
        for j in range(len(points)):
            curve[i] += comb(n, j) * ((1 - _t) ** (n - j)) * (_t ** j) * np.array(points[j])
    return curve

# Define control points (cubic Bézier)
control_points = np.array([[0, 0], [1, 2], [3, 3], [4, 0]])

# Generate curve
t = np.linspace(0, 1, 100)
curve = bezier_curve(t, control_points)

# Plot
plt.plot(control_points[:, 0], control_points[:, 1], 'ro--', label='Control Points')
plt.plot(curve[:, 0], curve[:, 1], 'b-', label='Bézier Curve')
plt.legend()
plt.title("Cubic Bézier Curve")
plt.show()

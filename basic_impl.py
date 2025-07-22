import numpy as np

# Point positions (relative to center)
x = 1  # e.g., 10 cm
y = 1

points = np.array([
    [ x,  0, 100],  # A
    [ 0,  y, 110],  # B
    [-x,  0, 114],  # C
    [ 0, -y, 104]   # D
])

# Fit plane Z = p*x + q*y + r
X = np.c_[points[:,0], points[:,1], np.ones(4)]
Z = points[:,2]

coeffs, _, _, _ = np.linalg.lstsq(X, Z, rcond=None)
p, q, r = coeffs

# Plane equation: Z = p*x + q*y + r
print(f"Plane: Z = {p:.2f}*x + {q:.2f}*y + {r:.2f}")

# Compute how much to raise/lower each screw to reach Z=r (flat)
adjustments = []
for pt in points:
    x_i, y_i, z_measured = pt
    z_target = r
    z_current = p*x_i + q*y_i + r
    delta = z_target - z_current
    adjustments.append(delta)

print("Adjustment needed at A, B, C, D (in mm):")
print(adjustments)

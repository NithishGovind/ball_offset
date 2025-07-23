import numpy as np
##center
x = 1  
y = 1
A=100
B=110
C=114
D=104

points = np.array([
    [ x,  0, A], 
    [ 0,  y, B], 
    [-x,  0, C], 
    [ 0, -y, D]   
])


X = np.c_[points[:,0], points[:,1], np.ones(4)]
Z = points[:,2]

coeffs, _, _, _ = np.linalg.lstsq(X, Z, rcond=None)
p, q, r = coeffs

print(coeffs)
print(f"Plane: Z = {p:.2f}*x + {q:.2f}*y + {r:.2f}")

adjustments = []
for pt in points:
    x_i, y_i, z_measured = pt
    z_target = r
    z_current = p*x_i + q*y_i + r
    delta = z_target - z_current
    adjustments.append(delta)

print("Adjustment needed at A, B, C, D (in mm):")
print(adjustments)

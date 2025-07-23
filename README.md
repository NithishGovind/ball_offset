# 🛠️ Planarity Correction for Machine Mounting using Least Squares

This repository demonstrates how to **measure and correct the tilt** (planarity error) of a machine platform (e.g., Maxio) using four probe measurements and a least squares fit to a plane. The adjustment helps align the machine surface to be perfectly flat (zero slope) with respect to a reference.

---

## 📌 Problem Statement

A robot with a flat base is mounted onto a surface via a plate. Due to installation and surface imperfections, the robot is not perfectly level. To calibrate this:

- A **needle** mounted on the robot end-effector probes four equidistant points (A, B, C, D) around the center.
- The **Z-height** values (a, b, c, d) at each probe point indicate the deviation from a flat reference.
- The goal is to calculate how much to **adjust the support screws** at each point to correct the surface and make it level.

## 📥 Input Parameters

| Parameter | Type            | Description                                                                 |
|-----------|-----------------|-----------------------------------------------------------------------------|
| `points`  | List of tuples or `np.ndarray` | Coordinates and Z-values of 4 probe points. Format: `[(x1, y1, z1), ..., (x4, y4, z4)]` |
| `x`       | `float`         | X-offset distance from center to A/C (symmetric setup)                      |
| `y`       | `float`         | Y-offset distance from center to B/D (symmetric setup)                      |

### 🧾 Input
```yaml
probe_points:
  A: {x:  1.0, y:  0.0, z: 100.0}
  B: {x:  0.0, y:  1.0, z: 110.0}
  C: {x: -1.0, y:  0.0, z: 114.0}
  D: {x:  0.0, y: -1.0, z: 104.0}
  method: least_squares
  plane: z = p*x + q*y + r

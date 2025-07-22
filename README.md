# 🛠️ Planarity Correction for Machine Mounting using Least Squares

This repository demonstrates how to **measure and correct the tilt** (planarity error) of a machine platform (e.g., Maxio) using four probe measurements and a least squares fit to a plane. The adjustment helps align the machine surface to be perfectly flat (zero slope) with respect to a reference.

---

## 📌 Problem Statement

A robot with a flat base is mounted onto a surface via a plate. Due to installation and surface imperfections, the robot is not perfectly level. To calibrate this:

- A **needle** mounted on the robot end-effector probes four equidistant points (A, B, C, D) around the center.
- The **Z-height** values (a, b, c, d) at each probe point indicate the deviation from a flat reference.
- The goal is to calculate how much to **adjust the support screws** at each point to correct the surface and make it level.


## 📄 Sample YAML Configuration

```yaml
robot:
  name: Maxio
  probe_points:
    A: {x: 1, y: 0, z: 100}
    B: {x: 0, y: 1, z: 110}
    C: {x: -1, y: 0, z: 114}
    D: {x: 0, y: -1, z: 104}
correction:
  method: least_squares
  plane: z = p*x + q*y + r

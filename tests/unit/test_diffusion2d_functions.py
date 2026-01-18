import pytest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from diffusion2d import SolveDiffusion2D


def test_initialize_domain():
    solver = SolveDiffusion2D()
    w, h, dx, dy = 20.0, 15.0, 0.5, 0.3  # Non-default, w != h to catch bugs
    expected_nx = int(w / dx)  # 40
    expected_ny = int(h / dy)  # 50

    solver.initialize_domain(w, h, dx, dy)

    assert solver.nx == expected_nx
    assert solver.ny == expected_ny
    assert solver.w == w
    assert solver.h == h
    assert solver.dx == dx
    assert solver.dy == dy


def test_initialize_physical_parameters():
    solver = SolveDiffusion2D()
    solver.initialize_domain()  # Only for dx,dy (minimal dep, but isolated check)
    d, T_cold, T_hot = 5.0, 250.0, 800.0
    dx2, dy2 = solver.dx**2, solver.dy**2
    expected_dt = dx2 * dy2 / (2 * d * (dx2 + dy2))  # ~6.25e-4

    solver.initialize_physical_parameters(d, T_cold, T_hot)

    assert solver.D == d
    assert solver.T_cold == T_cold
    assert solver.T_hot == T_hot
    assert abs(solver.dt - expected_dt) < 1e-10  # Floating-point tolerance


def test_set_initial_condition():
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=10.0, h=10.0, dx=0.1, dy=0.1)
    solver.initialize_physical_parameters()

    u = solver.set_initial_condition()

    print("u shape:", u.shape)  # Should be (100,100)
    print("T_cold:", solver.T_cold, type(solver.T_cold))
    print("T_hot:", solver.T_hot, type(solver.T_hot))
    center_i = int(5.0 / solver.dx)
    center_j = int(5.0 / solver.dy)
    print("center_i,j:", center_i, center_j)
    print("u[center]:", u[center_i, center_j])
    print("Hot count:", np.sum(u == solver.T_hot))
    print("Sample u[49:51,49:51]:\n", u[49:51, 49:51])

    # Keep existing asserts for now

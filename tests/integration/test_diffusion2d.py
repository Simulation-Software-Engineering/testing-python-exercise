"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import numpy as np


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    w = 12.0
    h = 12.0
    dx = 0.4
    dy = 0.4
    d = 5.0
    T_cold = 300.0
    T_hot = 700.0

    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d, T_cold, T_hot)

    dx2 = dx * dx
    dy2 = dy * dy
    expected_dt = dx2 * dy2 / (2 * d * (dx2 + dy2))

    assert solver.dt == expected_dt


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    w = 12.0
    h = 12.0
    dx = 1.0
    dy = 1.0
    d = 5.0
    T_cold = 300.0
    T_hot = 700.0

    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d, T_cold, T_hot)

    u = solver.set_initial_condition()

    expected_u = T_cold * np.ones((solver.nx, solver.ny))
    r, cx, cy = 2, 5, 5
    r2 = r ** 2

    for i in range(solver.nx):
        for j in range(solver.ny):
            p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
            if p2 < r2:
                expected_u[i, j] = T_hot
    
    assert np.allclose(u, expected_u)

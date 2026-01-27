"""
Tests for functionality checks in class SolveDiffusion2D
"""

import numpy as np

from diffusion2d import SolveDiffusion2D


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_physical_parameters
    """
    solver = SolveDiffusion2D()

    w, h, dx, dy = 12.0, 9.0, 0.6, 0.4
    d, T_cold, T_hot = 3.5, 290.0, 600.0
    solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)

    dx2, dy2 = dx * dx, dy * dy
    expected_dt = dx2 * dy2 / (2 * d * (dx2 + dy2))

    solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)

    assert np.isclose(solver.dt, expected_dt)


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.set_initial_condition
    """
    solver = SolveDiffusion2D()

    solver.initialize_domain(w=10.0, h=10.0, dx=1.0, dy=1.0)
    solver.initialize_physical_parameters(d=4.0, T_cold=250.0, T_hot=400.0)

    expected = solver.T_cold * np.ones((solver.nx, solver.ny))
    r, cx, cy = 2, 5, 5
    r2 = r ** 2
    for i in range(solver.nx):
        for j in range(solver.ny):
            p2 = (i * solver.dx - cx) ** 2 + (j * solver.dy - cy) ** 2
            if p2 < r2:
                expected[i, j] = solver.T_hot

    actual = solver.set_initial_condition()

    assert np.array_equal(actual, expected)

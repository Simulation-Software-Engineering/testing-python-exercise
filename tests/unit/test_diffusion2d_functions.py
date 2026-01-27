"""
Tests for functions in class SolveDiffusion2D
"""

import numpy as np

from diffusion2d import SolveDiffusion2D


def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()

    w, h, dx, dy = 12.5, 7.5, 0.5, 0.25
    expected_nx = int(w / dx)
    expected_ny = int(h / dy)

    solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)

    assert solver.nx == expected_nx
    assert solver.ny == expected_ny


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_physical_parameters
    """
    solver = SolveDiffusion2D()

    solver.dx = 0.2
    solver.dy = 0.4
    d, T_cold, T_hot = 2.0, 273.15, 313.15

    dx2, dy2 = solver.dx * solver.dx, solver.dy * solver.dy
    expected_dt = dx2 * dy2 / (2 * d * (dx2 + dy2))

    solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)

    assert solver.D == d
    assert solver.T_cold == T_cold
    assert solver.T_hot == T_hot
    assert np.isclose(solver.dt, expected_dt)


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.set_initial_condition
    """
    solver = SolveDiffusion2D()

    solver.nx = 6
    solver.ny = 6
    solver.dx = 1.0
    solver.dy = 1.0
    solver.T_cold = 10.0
    solver.T_hot = 100.0

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

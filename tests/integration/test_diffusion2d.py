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
    solver.initialize_domain()
    solver.initialize_physical_parameters()

    # Expected result
    expected_dt = 0.000625

    # Actual result
    actual_dt = solver.dt

    #Test
    assert abs(expected_dt - actual_dt) < 1e-5


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()

    # Expected result
    w = 20.
    h = 30.
    dx = 0.5
    dy = 0.2
    nx = 40
    ny = 150
    T_cold = 250.
    T_hot = 900.
    d = 6.
    expected_u0 = T_cold * np.ones((nx, ny))
    r, cx, cy = 2, 5, 5
    r2 = r ** 2
    for i in range(nx):
        for j in range(ny):
            p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
            if p2 < r2:
                expected_u0[i, j] = T_hot

    # Actual result
    solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
    solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)
    actual_u0 = solver.set_initial_condition()

    # Test
    for i in range(nx):
        for j in range(ny):
            assert expected_u0[i,j] == actual_u0[i,j]

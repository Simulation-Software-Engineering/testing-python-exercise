"""
Tests for functionality checks in class SolveDiffusion2D
"""
import numpy as np
import pytest
from diffusion2d import SolveDiffusion2D


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    w = 12.
    h = 20.
    dx = 0.4
    dy = 0.2
    d=5.

    expected_dt = pytest.approx(0.0032, abs=0.000001)

    solver.initialize_domain(w,h,dx,dy)
    solver.initialize_physical_parameters(d)

    assert solver.dt == expected_dt

def test_get_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    w = 12.
    h = 20.
    dx = 0.4
    dy = 0.2
    d=5.
    T_cold = 200.
    T_hot = 600.
    nx = 30
    ny = 100

    expected_u = T_cold * np.ones((nx, ny))
    # Initial conditions - circle of radius r centred at (cx,cy) (mm)
    r, cx, cy = 2, 5, 5
    r2 = r ** 2
    for i in range(nx):
        for j in range(ny):
            p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
            if p2 < r2:
                expected_u[i, j] = T_hot

    solver.initialize_domain(w,h,dx,dy)
    solver.initialize_physical_parameters(d,T_cold,T_hot)
    actual_u = solver.get_initial_condition()

    assert np.all(actual_u == expected_u)

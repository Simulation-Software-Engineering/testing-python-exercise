"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import pytest
import numpy as np

def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_physical_parameters
    """
    solver = SolveDiffusion2D()

    w, h, dx, dy = 10.0, 10.0, 0.1, 0.1
    d = 4.0
    expected_dt = 0.000625
    
    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d=d)

    assert solver.dt == pytest.approx(expected_dt)


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.set_initial_condition
    """
    solver = SolveDiffusion2D()

    w, h, dx, dy = 10.0, 10.0, 0.1, 0.1
    T_cold = 300.0
    T_hot = 700.0
    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(T_cold=T_cold, T_hot=T_hot)
    
    nx, ny = 100, 100
    expected_u = T_cold * np.ones((nx, ny))
    r, cx, cy = 2, 5, 5
    r2 = r ** 2
    for i in range(nx):
        for j in range(ny):
            p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
            if p2 < r2:
                expected_u[i, j] = T_hot
    
    actual_u = solver.set_initial_condition()
    assert np.allclose(actual_u, expected_u)
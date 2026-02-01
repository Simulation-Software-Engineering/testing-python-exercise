"""
Tests for functionality checks in class SolveDiffusion2D
"""

import pytest
import numpy as np
from diffusion2d import SolveDiffusion2D


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_physical_parameters
    """
    solver = SolveDiffusion2D()
    
    # Selection of values
    w, h, dx, dy = 10.0, 10.0, 0.5, 0.5
    d = 2.0
    
    # Manual computation of expected dt
    # dx2 = 0.25, dy2 = 0.25
    # expected_dt = (0.25 * 0.25) / (2 * 2.0 * (0.25 + 0.25))
    # expected_dt = 0.0625 / (4.0 * 0.5) = 0.0625 / 2.0 = 0.03125
    expected_dt = 0.03125
    
    # Call functions in order
    solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
    solver.initialize_physical_parameters(d=d)
    
    assert solver.dt == pytest.approx(expected_dt)


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.set_initial_condition
    """
    solver = SolveDiffusion2D()
    
    # Selection of values
    w, h, dx, dy = 10.0, 10.0, 0.5, 0.5
    T_cold = 300.0
    T_hot = 700.0
    
    solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
    solver.initialize_physical_parameters(T_cold=T_cold, T_hot=T_hot)
    
    # Manually compute the expected u array
    nx, ny = 20, 20
    expected_u = np.full((nx, ny), T_cold)
    r, cx, cy = 2, 5, 5
    r2 = r ** 2
    for i in range(nx):
        for j in range(ny):
            p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
            if p2 < r2:
                expected_u[i, j] = T_hot
                
    u = solver.set_initial_condition()
    
    assert np.array_equal(u, expected_u)

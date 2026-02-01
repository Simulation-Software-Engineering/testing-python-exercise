"""
Tests for functions in class SolveDiffusion2D
"""

import pytest
import numpy as np
from diffusion2d import SolveDiffusion2D


def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    w = 20.0
    h = 10.0
    dx = 0.5
    dy = 0.2

    expected_nx = 40
    expected_ny = 50

    solver.initialize_domain(w, h, dx, dy)

    assert solver.nx == expected_nx
    assert solver.ny == expected_ny


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_physical_parameters
    """
    solver = SolveDiffusion2D()
    solver.dx = 0.2
    solver.dy = 0.1
    d = 4.0
    # expected_dt = (0.2^2 * 0.1^2) / (2 * 4.0 * (0.2^2 + 0.1^2))
    # expected_dt = (0.04 * 0.01) / (8.0 * (0.04 + 0.01))
    # expected_dt = 0.0004 / (8.0 * 0.05) = 0.0004 / 0.4 = 0.001
    expected_dt = 0.001

    solver.initialize_physical_parameters(d=d)

    assert solver.dt == pytest.approx(expected_dt)


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.set_initial_condition
    """
    solver = SolveDiffusion2D()
    solver.nx = 10
    solver.ny = 10
    solver.dx = 0.1
    solver.dy = 0.1
    solver.T_cold = 300.0
    solver.T_hot = 700.0
    
    # cx=5, cy=5, r=2. r^2 = 4
    # For nx=10, ny=10, dx=0.1, dy=0.1, max i*dx = 0.9.
    # (i*dx - 5)^2 + (j*dy - 5)^2 will always be >= (0.9-5)^2 + (0.9-5)^2 = 16.81 + 16.81 = 33.62
    # 33.62 > 4, so all values should be T_cold
    
    expected_u = 300.0 * np.ones((10, 10))
    
    u = solver.set_initial_condition()
    
    assert np.array_equal(u, expected_u)

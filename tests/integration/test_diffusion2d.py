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

    w = 10.
    h = 10.
    dx = 0.5
    dy = 0.5
    solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)

    d = 2.
    T_cold = 150.
    T_hot = 350.
    solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)
    expected_result = 0.03125

    assert solver.dt == expected_result


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    # compute a similar `u` array for defined parameters
    w = 12.
    h = 18.
    dx = 2.
    dy = 6.
    T_cold = 6.
    nx = int(w / dx)
    ny = int(h / dy)
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
    solver.initialize_physical_parameters(T_cold=T_cold)
    solver.cx = 4
    solver.cy = 2
    expected_u = solver.T_cold * np.ones((nx, ny)).copy()
    
    computed_u = solver.set_initial_condition()
    assert computed_u.all() == expected_u.all()

"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import numpy as np


def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    w = 100.
    h = 120.
    dx = 0.5
    dy = 0.5
    expected_nx = 200.
    expected_ny = 240.
    solver = SolveDiffusion2D()

    solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
    assert solver.nx == expected_nx
    assert solver.ny == expected_ny

def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    d = 2.
    T_cold = 150.
    T_hot = 350.
    solver = SolveDiffusion2D()
    solver.dx = 0.5
    solver.dy = 0.5
    expected_dt = 0.03125

    solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)
    assert solver.dt == expected_dt

def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.T_cold = 6
    solver.nx = 6
    solver.ny = 3
    solver.dx = 9
    solver.dy = 3
    solver.cx = 4
    solver.cy = 2
    expected_result = solver.T_cold * np.ones((solver.nx, solver.ny)).copy()
    
    actual_result = solver.set_initial_condition()
    assert actual_result.all() == expected_result.all()

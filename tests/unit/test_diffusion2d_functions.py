"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import pytest
import numpy as np


def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    # fixture
    w = 1.
    h = 2.
    dx = 0.2
    dy = 0.5
    # expected result
    expected_nx = 5
    expected_ny = 4
    # actual result
    solver = SolveDiffusion2D()
    solver.initialize_domain(w, h, dx, dy)
    # test
    assert expected_nx == solver.nx
    assert expected_ny == solver.ny


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    # fixture
    solver = SolveDiffusion2D()
    d = 2.
    T_cold = 350.
    T_hot = 420.
    solver.dx = 1.
    solver.dy = 1.
    # expected result
    expected_dt = 0.125
    # actual result
    solver.initialize_physical_parameters(d, T_cold, T_hot)
    # test
    assert expected_dt == solver.dt
    assert T_cold == solver.T_cold
    assert T_hot == solver.T_hot
    
    


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    # fixture
    solver = SolveDiffusion2D()
    solver.nx = 2
    solver.ny = 2
    solver.dx = 4.5
    solver.dy = 5.5
    solver.T_cold = 200.
    solver.T_hot = 420.
    
    # expected result
    expected_u = np.array([[200., 200.], [200., 420.]])
    # actual result
    actual_u = solver.set_initial_condition()
    expected_u_approx = pytest.approx(expected_u, abs=0.01)
    # test
    assert expected_u_approx == actual_u

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
    # fixture
    w = 1.
    h = 2.
    d = 2.
    T_cold = 350.
    T_hot = 420.
    dx = 1.
    dy = 1.
    # expected result
    expected_dt = 0.125
    # actual result
    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d, T_cold, T_hot)
    # test
    assert expected_dt == solver.dt

def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    # fixture
    w = 9.
    h = 11.
    dx = 4.5
    dy = 5.5
    d = 2.
    T_cold = 200.
    T_hot = 420.
    
    # expected result
    nx = int(w/dx)
    ny = int(h/dy)
    expected_u = T_cold * np.ones((nx,ny))
    expected_u[1,1] = T_hot
    # actual result
    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d, T_cold, T_hot)
    actual_u = solver.set_initial_condition()
    # expected_u_approx = pytest.approx(expected_u, abs=0.01)
    # test
    # self.assertAlmostEqual(expected_u_approx, actual_u)
    for idx_x in range(solver.nx):
        for idx_y in range(solver.ny):
            assert expected_u[idx_x, idx_y] == actual_u[idx_x, idx_y]

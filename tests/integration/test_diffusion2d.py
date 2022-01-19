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
    w = 25.
    h = 4.
    dx = 0.5
    dy = 0.1
    d = 5.
    T_cold = 250.
    T_hot = 850.
    expected_dt = 9.6153846e-04
    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d, T_cold, T_hot)
    np.testing.assert_almost_equal(solver.dt, expected_dt)

# I think, we should test GET_initial_condition() instead of SET_initial_condition since there exists no such function and we expect a return value.
# def test_set_initial_condition():
def test_get_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    w = 10.
    h = 6.6668
    solver.T_cold = 250.
    solver.T_hot = 850.
    solver.nx = 3
    solver.ny = 4
    solver.dx = 2.5
    solver.dy = 1.6667

    u_expected = np.array([[250., 250., 250., 250.], [250., 250., 250., 250.], [250., 250., 850., 850.]])
    u_return = solver.get_initial_condition()
    np.testing.assert_almost_equal(u_return, u_expected)

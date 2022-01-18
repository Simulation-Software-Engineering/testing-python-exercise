"""
Tests for functionality checks in class SolveDiffusion2D
"""
import numpy as np
from diffusion2d import SolveDiffusion2D
from pytest import approx


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()

    w = 30.0
    h = 12.0
    dx = 0.3
    dy = 0.6
    d = 20.0
    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d)

    expected_dt = approx(0.0018, abs=0.000001)

    actual_dt = solver.dt

    assert actual_dt == expected_dt


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()

    w = 6.0
    h = 8.0
    dx = 0.3
    dy = 0.5
    d = 20.0
    T_cold = 300.0
    T_hot = 400.0

    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d, T_cold, T_hot)

    expected_u = T_cold * np.ones((20, 16))
    expected_u[11:20, 7:14] = 400.0
    expected_u[11:13, 7] = 300.0
    expected_u[11:13, 13] = 300.0

    actual_u = solver.set_initial_condition()

    np.testing.assert_allclose(actual_u, expected_u)

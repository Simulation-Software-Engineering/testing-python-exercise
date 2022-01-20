"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import pytest
import numpy as np


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """

    solver = SolveDiffusion2D()
    w, h, dx, dy = 20.0, 40.0, 0.1, 0.1
    d, T_cold, T_hot = 2.5, 200.0, 500.0

    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)

    expected_dt = pytest.approx(0.001, abs=0.0001)

    assert solver.dt == expected_dt

def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    w, h, dx, dy = 10.0, 12.0, 5.0, 6.0
    d, T_cold, T_hot = 2.5, 200.0, 500.0

    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)

    expected_u = solver.T_cold * np.ones((solver.nx, solver.ny))
    expected_u[1,1] = solver.T_hot

    assert (solver.set_initial_condition() == expected_u).all()
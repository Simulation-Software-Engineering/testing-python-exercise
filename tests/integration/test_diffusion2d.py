"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D

import pytest
import numpy as np

@pytest.fixture
def input_values():
    # w, h, dx, dy, d, T_cold, T_hot
    return [40., 50., 0.1, 0.1, 5., 200., 800.]

def test_initialize_physical_parameters(input_values):
    """
    Checks function SolveDiffusion2D.initialize_physical_parameters
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(*input_values[:4])
    solver.initialize_physical_parameters(*input_values[4:])
    assert solver.dt == pytest.approx(0.0005)


def test_set_initial_condition(input_values):
    """
    Checks function SolveDiffusion2D.set_initial_condition
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(*input_values[:4])
    solver.initialize_physical_parameters(*input_values[4:])
    u = solver.set_initial_condition()
    np.testing.assert_array_almost_equal(u, np.genfromtxt("tests/u_ref.csv", delimiter=","))

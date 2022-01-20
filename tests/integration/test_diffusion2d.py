"""
Tests for functionality checks in class SolveDiffusion2D
"""
import os, sys

import numpy as np
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.append(parentdir)

from diffusion2d import SolveDiffusion2D

def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()

    w = 22.
    h = 3.
    dx = 0.5
    dy = 0.86

    solver.initialize_domain(w, h, dx, dy)

    d = 7.0
    solver.initialize_physical_parameters(d)

    actual_dt_rounded = round(solver.dt, 3)

    assert 0.013 == actual_dt_rounded


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()

    w = 9.
    h = 9.
    dx = 3.
    dy = 3.

    T_cold = 200.
    T_hot = 900.

    solver.initialize_domain(w, h, dx, dy)

    d = 7.0
    solver.initialize_physical_parameters(d, T_cold, T_hot)

    u = solver.set_initial_condition()

    expected_u = np.array([[200., 200., 200.],
                            [200., 200., 200.],
                            [200., 200., 900.]])
    
    assert np.testing.assert_array_equal(u, expected_u) is None


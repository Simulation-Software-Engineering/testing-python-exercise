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
    solver = SolveDiffusion2D()

    solver.initialize_domain(1.5, 2.0, 0.2, 0.2)

    assert solver.nx == 7
    assert solver.ny == 10

    with pytest.raises(AssertionError):
        solver.initialize_domain(1, 2, 0.2, 0.2)


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()

    solver.dx = 0.1
    solver.dy = 0.1
    solver.nx = 100
    solver.ny = 100

    solver.initialize_physical_parameters(5.0, 300.0, 700.0)
    assert solver.dt == pytest.approx(0.0005, rel=1e-4)

    solver.initialize_physical_parameters(5.0, 500.0, 800.0)
    assert solver.dt == pytest.approx(0.0005, rel=1e-4)

    with pytest.raises(AssertionError):
        solver.initialize_physical_parameters(5, 500, 800)


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()

    solver.T_cold = 0.0
    solver.T_hot = 1.0
    solver.dx = 1.0
    solver.dy = 1.0
    solver.nx = 8
    solver.ny = 8

    # 8x8 domain with circle at (5,5)
    expected_field = np.array(
        [[0., 0., 0., 0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 1., 1., 1., 0.],
         [0., 0., 0., 0., 1., 1., 1., 0.],
         [0., 0., 0., 0., 1., 1., 1., 0.],
         [0., 0., 0., 0., 0., 0., 0., 0.]]
    )

    actual_field = solver.set_initial_condition()

    error_norm = np.linalg.norm(expected_field - actual_field)
    assert 0 == pytest.approx(error_norm, abs=1e-14)

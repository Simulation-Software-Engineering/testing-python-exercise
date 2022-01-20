"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import numpy as np
import math


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    # Fixture
    square_domain = {'w': 1., 'h': 1., 'dx': 0.2, 'dy': 0.2}
    easy_physical = {'d': 2., 'T_cold': 300.,'T_hot': 450.}
        
    # Expected result
    solution = {'dt': 0.005}

    # Actual Result
    solver = SolveDiffusion2D()
    solver.initialize_domain(**square_domain)
    solver.initialize_physical_parameters(**easy_physical)

    # Test
    assert math.isclose(solver.dt, solution['dt']), "dt for case 1"

def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    # Fixture
    square_domain = {'w': 1., 'h': 1., 'dx': 0.2, 'dy': 0.2}
    easy_physical = {'d': 2., 'T_cold': 300.,'T_hot': 450.}

    # Expected Result
    solution = np.array([[300., 300., 300., 300., 300.],
                        [300., 300., 300., 300., 300.],
                        [300., 300., 300., 300., 300.],
                        [300., 300., 300., 300., 300.],
                        [300., 300., 300., 300., 300.]])

    # Set-up
    solver = SolveDiffusion2D()
    solver.initialize_domain(**square_domain)
    solver.initialize_physical_parameters(**easy_physical)

    # Test
    result = solver.set_initial_condition()
    assert (np.allclose(result, solution)) and result.shape == solution.shape

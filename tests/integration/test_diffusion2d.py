"""
Tests for functionality checks in class SolveDiffusion2D
"""
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.append(parentdir)
import math
import numpy as np
from diffusion2d import SolveDiffusion2D


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(20.,40.,1.,10.)
    solver.initialize_physical_parameters(5.,200.,800.)
    expected_dt = 0.09900990099009900
    assert math.isclose(solver.dt, expected_dt)


def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(20.,40.,10.,40.)
        solver.initialize_physical_parameters(5.,200.,800.)

        # Expected result
        expected = np.array([[200.],[200.]])
        result = solver.set_initial_condition()
        np.testing.assert_array_equal(result, expected)


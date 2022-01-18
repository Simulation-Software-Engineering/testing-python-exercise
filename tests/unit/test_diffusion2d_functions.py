"""
Tests for functions in class SolveDiffusion2D
"""

from unittest import TestCase

import numpy as np
from diffusion2d import SolveDiffusion2D
from pytest import approx


class TestOperations(TestCase):
    def setUp(self):
        self.solver = SolveDiffusion2D()
    
    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        w = 20.0
        h = 40.0
        dx = 0.2
        dy = 0.2
        self.solver.initialize_domain(w, h, dx, dy)

        expected_nx = 100
        expected_ny = 200

        actual_nx = self.solver.nx
        actual_ny = self.solver.ny

        self.assertEqual(actual_nx, expected_nx)
        self.assertEqual(actual_ny, expected_ny)


    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        d = 5.0
        T_cold = 200.0
        T_hot = 800.0
        self.solver.dx = 0.2
        self.solver.dy = 0.4
        self.solver.initialize_physical_parameters(d, T_cold, T_hot)

        expected_dt = 0.0032

        actual_dt = self.solver.dt

        self.assertAlmostEqual(actual_dt,expected_dt)


    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        self.solver.T_cold = 200.0
        self.solver.T_hot = 800.0
        self.solver.nx = 5
        self.solver.ny = 10
        self.solver.dx = 1.0
        self.solver.dy = 2.0

        expected_u = np.ones((5,10))*200.
        expected_u[4,2:4]=800.

        actual_u = self.solver.set_initial_condition()

        np.testing.assert_allclose(actual_u,expected_u)



# old tests
'''def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    w = 20.0
    h = 40.0
    dx = 0.2
    dy = 0.2
    solver.initialize_domain(w, h, dx, dy)

    expected_nx = 100
    expected_ny = 200

    actual_nx = solver.nx
    actual_ny = solver.ny

    assert actual_nx == expected_nx
    assert actual_ny == expected_ny


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    d = 5.0
    T_cold = 200.0
    T_hot = 800.0
    solver.dx = 0.2
    solver.dy = 0.4
    solver.initialize_physical_parameters(d, T_cold, T_hot)

    expected_dt = approx(0.0032, abs=0.0001)

    actual_dt = solver.dt

    assert actual_dt == expected_dt


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.T_cold = 200.0
    solver.T_hot = 800.0
    solver.nx = 5
    solver.ny = 10
    solver.dx = 1.0
    solver.dy = 2.0

    expected_u = np.ones((5,10))*200.
    expected_u[4,2:4]=800.

    actual_u = solver.set_initial_condition()

    np.testing.assert_allclose(actual_u,expected_u)'''



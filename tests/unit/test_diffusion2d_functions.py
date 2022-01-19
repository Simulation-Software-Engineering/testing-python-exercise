"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import numpy as np
from unittest import TestCase

class TestDiffusion2DFunctions(TestCase):
    def setUp(self):
        self.solver = SolveDiffusion2D()

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        w = 25.
        h = 4.
        dx = 0.5
        dy = 0.1
        expected_nx = 50
        expected_ny = 40
        self.solver.initialize_domain(w, h, dx, dy)
        np.testing.assert_equal(self.solver.nx, expected_nx)
        np.testing.assert_equal(self.solver.ny, expected_ny)


    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        d = 5.
        T_cold = 250.
        T_hot = 850.
        self.solver.dx = 0.5
        self.solver.dy = 0.1
        expected_dt = 9.6153846e-04
        self.solver.initialize_physical_parameters(d, T_cold, T_hot)
        np.testing.assert_almost_equal(self.solver.dt, expected_dt, decimal=6)


    def test_get_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        self.solver.T_cold = 250.
        self.solver.T_hot = 850.
        self.solver.nx = 3
        self.solver.ny = 4
        self.solver.dx = 2.5
        self.solver.dy = 1.6667

        u_expected = np.array([[250., 250., 250., 250.], [250., 250., 250., 250.], [250., 250., 850., 850.]])
        u_return = self.solver.get_initial_condition()
        np.testing.assert_almost_equal(u_return, u_expected)

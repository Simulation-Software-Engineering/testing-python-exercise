"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import pytest
import numpy as np
from unittest import TestCase

class TestDiffusion2D(TestCase):
    def setUp(self):
        # fixture
        self.solver = SolveDiffusion2D()

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        w = 1.
        h = 2.
        dx = 0.2
        dy = 0.5
        # expected result
        expected_nx = 5
        expected_ny = 4
        # actual result
        self.solver.initialize_domain(w, h, dx, dy)
        # test
        self.assertEqual(self.solver.nx, expected_nx)
        self.assertEqual(self.solver.ny, expected_ny)
        
    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        # fixture
        d = 2.
        T_cold = 350.
        T_hot = 420.
        self.solver.dx = 1.
        self.solver.dy = 1.
        # expected result
        expected_dt = 0.125
        # actual result
        self.solver.initialize_physical_parameters(d, T_cold, T_hot)
        # test
        self.assertAlmostEqual(expected_dt, self.solver.dt)
        self.assertAlmostEqual(T_cold, self.solver.T_cold)
        self.assertAlmostEqual(T_hot, self.solver.T_hot)

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        # fixture
        self.solver.nx = 2
        self.solver.ny = 2
        self.solver.dx = 4.5
        self.solver.dy = 5.5
        self.solver.T_cold = 200.
        self.solver.T_hot = 420.
    
        # expected result
        # expected_u = np.array([[200., 200.], [200., 420.]])
        expected_u = self.solver.T_cold * np.ones((self.solver.nx,self.solver.ny))
        expected_u[1,1] = self.solver.T_hot
        # actual result
        actual_u = self.solver.set_initial_condition()
        # expected_u_approx = pytest.approx(expected_u, abs=0.01)
        # test
        # self.assertAlmostEqual(expected_u_approx, actual_u)
        for idx_x in range(self.solver.nx):
            for idx_y in range(self.solver.ny):
                self.assertEqual(expected_u[idx_x, idx_y], actual_u[idx_x, idx_y])

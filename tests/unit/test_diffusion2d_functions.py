"""
Tests for functions in class SolveDiffusion2D
"""
from unittest import TestCase
from diffusion2d import SolveDiffusion2D
import numpy as np

class TestOperations(TestCase):
    """
    Test suite for mathematical operations functions.
    """
    def setUp(self):
        # Fixture
        self.solver = SolveDiffusion2D()

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        

        # Expected result
        expected_nx = 250
        expected_ny = 400

        # Actual result
        self.solver.initialize_domain(w=5., h=20., dx=0.02, dy=0.05)
        actual_nx = self.solver.nx
        actual_ny = self.solver.ny

        # Test
        self.assertEqual(expected_nx, actual_nx)
        self.assertEqual(expected_ny, actual_ny)


    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """

        # Expected result
        expected_T_cold = 200.
        expected_T_hot = 600.
        expected_dt = 1/32

        # Actual result
        self.solver.dx = 1
        self.solver.dy = 1
        self.solver.initialize_physical_parameters(d=8., T_cold=expected_T_cold, T_hot=expected_T_hot)
        actual_T_cold = self.solver.T_cold
        actual_T_hot = self.solver.T_hot
        actual_dt = self.solver.dt

        # Test
        self.assertEqual(expected_T_cold, actual_T_cold)
        self.assertEqual(expected_T_hot, actual_T_hot)
        self.assertEqual(expected_dt, actual_dt)


    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """

        # Expected result
        dx = 0.2
        dy = 0.3
        nx = 100
        ny = 150
        T_cold = 200.
        T_hot = 600.
        expected_u = T_cold * np.ones((nx, ny))
        r, cx, cy = 2, 5, 5
        r2 = r ** 2
        for i in range(nx):
            for j in range(ny):
                p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
                if p2 < r2:
                    expected_u[i, j] = T_hot

        # Actual result
        self.solver.dx = dx
        self.solver.dy = dy
        self.solver.nx = nx
        self.solver.ny = ny
        self.solver.T_cold = T_cold
        self.solver.T_hot = T_hot
        actual_u = self.solver.set_initial_condition()

        # Test
        for i in range(nx):
            for j in range(ny):
                self.assertEqual(expected_u[i,j], actual_u[i,j])

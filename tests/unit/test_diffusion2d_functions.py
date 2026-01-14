"""
Tests for functions in class SolveDiffusion2D
"""
import unittest
import numpy as np
import sys
import os

# Fix import path: Add the root directory to sys.path so we can import diffusion2d
# This assumes you run the test from the root of the repository
sys.path.append(os.getcwd())

from diffusion2d import SolveDiffusion2D


class TestDiffusion2D(unittest.TestCase):
    
    def setUp(self):
        """
        Fixture that runs before every test.
        """
        self.solver = SolveDiffusion2D()

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        # 1. Define input parameters different from defaults
        w = 20.0
        h = 40.0
        dx = 2.0
        dy = 4.0
        
        # 2. Expected values (manually calculated)
        # nx = 20 / 2 = 10
        # ny = 40 / 4 = 10
        expected_nx = 10
        expected_ny = 10

        # 3. Call the function
        self.solver.initialize_domain(w, h, dx, dy)

        # 4. Assertions
        self.assertEqual(self.solver.nx, expected_nx)
        self.assertEqual(self.solver.ny, expected_ny)

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_physical_parameters
        """
        # 1. Manually define the required internal variables (dx, dy)
        # We must do this because we cannot call initialize_domain here.
        self.solver.dx = 1.0
        self.solver.dy = 1.0
        
        # 2. Define inputs
        d = 5.0
        T_cold = 200.0
        T_hot = 600.0

        # 3. Calculate expected dt manually
        # dt = dx^2 * dy^2 / (2 * D * (dx^2 + dy^2))
        # dt = 1*1 / (2*5 * (1+1)) = 1 / 20 = 0.05
        expected_dt = 0.05

        # 4. Call the function
        self.solver.initialize_physical_parameters(d, T_cold, T_hot)

        # 5. Assertions
        self.assertAlmostEqual(self.solver.dt, expected_dt, places=5)
        self.assertEqual(self.solver.T_cold, T_cold)
        self.assertEqual(self.solver.T_hot, T_hot)

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.set_initial_condition
        """
        # 1. Manually set all member variables required for calculation
        self.solver.nx = 3
        self.solver.ny = 3
        self.solver.dx = 1.0
        self.solver.dy = 1.0
        self.solver.T_cold = 300.0
        self.solver.T_hot = 700.0
        
        # 2. Call the function
        actual_u = self.solver.set_initial_condition()

        # 3. Manually compute the expected array
        # We replicate the logic for a small 3x3 grid
        expected_u = 300.0 * np.ones((3, 3))
        
        # Circle parameters from the code: r=2, cx=5, cy=5
        r, cx, cy = 2, 5, 5
        r2 = r ** 2
        
        for i in range(3):
            for j in range(3):
                p2 = (i * 1.0 - cx) ** 2 + (j * 1.0 - cy) ** 2
                if p2 < r2:
                    expected_u[i, j] = 700.0
        
        # 4. Assertions
        # Use numpy.testing to compare arrays
        np.testing.assert_array_equal(actual_u, expected_u)
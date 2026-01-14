"""
Tests for functionality checks in class SolveDiffusion2D
"""
import unittest
import numpy as np
import sys
import os

# Fix import path to allow importing diffusion2d from the root directory
sys.path.append(os.getcwd())

from diffusion2d import SolveDiffusion2D


class TestDiffusion2D(unittest.TestCase):
    
    def setUp(self):
        """
        Fixture that runs before every test.
        """
        self.solver = SolveDiffusion2D()

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_physical_parameters 
        running AFTER initialize_domain.
        """
        # 1. Define inputs
        w = 10.0
        h = 10.0
        dx = 1.0
        dy = 1.0
        d = 4.0
        T_cold = 300.0
        T_hot = 700.0
        
        # 2. Call the functions in sequence (Integration)
        self.solver.initialize_domain(w, h, dx, dy)
        self.solver.initialize_physical_parameters(d, T_cold, T_hot)

        # 3. Calculate expected dt manually
        # dt = dx^2 * dy^2 / (2 * D * (dx^2 + dy^2))
        # dt = (1*1) / (2 * 4 * (1+1)) = 1 / 16 = 0.0625
        expected_dt = 0.0625

        # 4. Assertion
        self.assertAlmostEqual(self.solver.dt, expected_dt, places=4)

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.set_initial_condition
        running AFTER domain and physical parameters are set.
        """
        # 1. Define inputs for the whole chain
        w = 10.0
        h = 10.0
        dx = 1.0
        dy = 1.0
        d = 4.0
        T_cold = 300.0
        T_hot = 700.0

        # 2. Call the functions in sequence
        self.solver.initialize_domain(w, h, dx, dy)
        self.solver.initialize_physical_parameters(d, T_cold, T_hot)
        actual_u = self.solver.set_initial_condition()

        # 3. Manually compute expected_u
        # We know initialize_domain with these params creates a 10x10 grid (w/dx, h/dy)
        nx = 10
        ny = 10
        expected_u = T_cold * np.ones((nx, ny))

        # Circle logic from the problem statement: r=2, cx=5, cy=5
        r, cx, cy = 2, 5, 5
        r2 = r ** 2
        
        for i in range(nx):
            for j in range(ny):
                p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
                if p2 < r2:
                    expected_u[i, j] = T_hot
        
        # 4. Assertion
        np.testing.assert_array_equal(actual_u, expected_u)
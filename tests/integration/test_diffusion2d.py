"""
Tests for functionality checks in class SolveDiffusion2D
"""

import unittest
import numpy as np
from diffusion2d import SolveDiffusion2D

class TestDiffusion2D(unittest.TestCase):

    def setUp(self):
        self.solver = SolveDiffusion2D()

    def test_initialize_physical_parameters(self):
        """
        Checks function initialize_physical_parameters.
        """
        w = 10.0
        h = 10.0
        dx = 1.0
        dy = 1.0
        
        self.solver.initialize_domain(w, h, dx, dy)

        d = 1.0
        T_cold = 300.0
        T_hot = 700.0

        # Expected result
        # dt = dx*dy / ( 2*d * (dx^2 + dy^2) )
        # dt = 1 / (2 * 2) = 0.25
        expected_dt = 0.25

        self.solver.initialize_physical_parameters(d, T_cold, T_hot)

        self.assertAlmostEqual(self.solver.dt, expected_dt)

    def test_set_initial_condition(self):
        """
        Checks function set_initial_condition.
        """
        w = 10.0
        h = 10.0
        dx = 1.0
        dy = 1.0
        d = 4.0
        T_cold = 300.0
        T_hot = 700.0

        self.solver.initialize_domain(w, h, dx, dy)
        self.solver.initialize_physical_parameters(d, T_cold, T_hot)
        u = self.solver.set_initial_condition()

        self.assertEqual(u.shape, (10, 10))
        
        self.assertEqual(u[0, 0], 300.0)
"""
Tests for functions in class SolveDiffusion2D
"""
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.append(parentdir)

import math
from cv2 import solve
from diffusion2d import SolveDiffusion2D
import numpy as np
import unittest


class TestDiffusion2D(unittest.TestCase):
    def setUp(self):
        self.solver = SolveDiffusion2D()

    # Unit tests
    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        self.solver.initialize_domain(20.,30.,0.01,0.01)
        expected_nx = 2000
        expected_ny = 3000
        self.assertEqual(expected_nx,self.solver.nx)
        self.assertEqual(expected_ny,self.solver.ny)



    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        self.solver.dx = 0.1
        self.solver.dy = 0.2
        self.solver.initialize_physical_parameters(5.,200.,800.)
        expected_dt = 0.0008000000000000001
        self.assertAlmostEqual(self.solver.dt, expected_dt)

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        self.solver.w = 0.1
        self.solver.h = 0.1
        self.solver.T_cold = 200.
        self.solver.T_hot = 800.
        self.solver.dx = 0.1
        self.solver.dy = 0.2
        self.solver.nx = 1
        self.solver.ny = 1

        # Expected result
        expected = np.array([[200.]])

        result = self.solver.set_initial_condition()
        self.assertIsNone(np.testing.assert_array_equal(result, expected))

if __name__ == '__main__':
    unittest.main()

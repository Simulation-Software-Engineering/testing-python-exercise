"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import numpy as np

from unittest import TestCase
import pytest


class TestDiffusion2D(TestCase):
    def setUp(self):
        self.solver = SolveDiffusion2D()


    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        # set values
        w  = 2.
        h  = 3.
        dx = 0.5
        dy = 0.5

        nx_expected = 4
        ny_expected = 6

        self.solver.initialize_domain(w, h, dx, dy)
        
        #assert nx_expected == solver.nx
        #assert ny_expected == solver.ny
        self.assertEqual(self.solver.nx, nx_expected)
        self.assertEqual(self.solver.ny, ny_expected)


    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        #solver = SolveDiffusion2D()

        T_cold = 100.
        T_hot  = 1000.

        d      = 2. 
        dx     = 1.
        dy     = 1.
        
        dt_expected = 0.125

        self.solver.dx = dx 
        self.solver.dy = dy

        self.solver.initialize_physical_parameters(d, T_cold, T_hot)

        # check for correct calculations and setting of params
        self.assertEqual(self.solver.dt, dt_expected)
        self.assertEqual(self.solver.T_cold, T_cold)
        self.assertEqual(self.solver.T_hot, T_hot)
        

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """

        self.solver.T_hot  = 333. 
        self.solver.T_cold = -17.
        self.solver.nx     = 2
        self.solver.ny     = 2
        self.solver.dx     = 4.5
        self.solver.dy     = 5.5

        u_expected = np.array([[-17., -17.], [-17., 333.]])
        u_expected_approx = pytest.approx(u_expected, abs=0.0001)

        u_returned  = self.solver.set_initial_condition()
        
        #assert all([a == b for a, b in zip(u_expected, u_returned)])
        self.assertAlmostEqual(u_returned, u_expected_approx)

        
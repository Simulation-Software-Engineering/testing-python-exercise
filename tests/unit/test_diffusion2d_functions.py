"""
Tests for functions in class SolveDiffusion2D
"""
import os, sys
import unittest

import numpy as np
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.append(parentdir)

from diffusion2d import SolveDiffusion2D

class TestDiffusion2D(unittest.TestCase):

    def setUp(self):
        self.solver = SolveDiffusion2D()

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        w = 22.
        h = 3.
        dx = 0.67
        dy = 0.12

        self.solver.initialize_domain(w, h, dx, dy)

        self.assertEqual(32, self.solver.nx) 
        self.assertEqual(25, self.solver.ny)


    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """

        self.solver.dx = 0.5
        self.solver.dy = 0.86

        d = 7.0
        self.solver.initialize_physical_parameters(d)

        actual_dt_rounded = round(self.solver.dt, 3)

        self.assertEqual(0.013, actual_dt_rounded)


    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """

        self.solver.T_cold = 200
        self.solver.T_hot = 900

        self.solver.nx = 3
        self.solver.ny = 3
        self.solver.dx = 0.4
        self.solver.dy = 0.5

        u = self.solver.set_initial_condition()

        expected_u = np.array([[200., 200., 200.],
                               [200., 200., 200.],
                               [200., 200., 200.]])

        self.assertIsNone(np.testing.assert_array_equal(expected_u, u))



# pytest code

#"""
#Tests for functions in class SolveDiffusion2D
#"""
#import os, sys

#import numpy as np
#currentdir = os.path.dirname(os.path.realpath(__file__))
#parentdir = os.path.dirname(os.path.dirname(currentdir))
#sys.path.append(parentdir)

#from diffusion2d import SolveDiffusion2D


#def test_initialize_domain():
#    """
#    Check function SolveDiffusion2D.initialize_domain
#   """
#   solver = SolveDiffusion2D()

#    w = 22.
#    h = 3.
#    dx = 0.67
#    dy = 0.12

#    solver.initialize_domain(w, h, dx, dy)

#   assert 32 == solver.nx
#    assert 25 == solver.ny


#def test_initialize_physical_parameters():
#    """
#    Checks function SolveDiffusion2D.initialize_domain
#    """
#    solver = SolveDiffusion2D()

#    solver.dx = 0.5
#    solver.dy = 0.86

#    d = 7.0
#    solver.initialize_physical_parameters(d)

#    actual_dt_rounded = round(solver.dt, 3)

#    assert 0.013 == actual_dt_rounded


#def test_set_initial_condition():
#   """
#    Checks function SolveDiffusion2D.get_initial_function
#    """
#    solver = SolveDiffusion2D()

#    solver.T_cold = 200
#    solver.T_hot = 900

#    solver.nx = 3
#    solver.ny = 3
#    solver.dx = 0.4
#    solver.dy = 0.5

    # the returned ndarray should have everywhere a value of 200., according to the function
#    u = solver.set_initial_condition()

#    expected_u = np.array([[200., 200., 200.],
#                          [200., 200., 200.],
#                          [200., 200., 200.]])

#    assert np.testing.assert_array_equal(u, expected_u) is None
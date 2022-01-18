"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import numpy as np
import pytest
import unittest


if __name__ == '__main__':
    unittest.main()

class TestDiffusion2D(unittest.TestCase):

    def setUp(self):
        self.solver = SolveDiffusion2D

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
    
        self.solver.initialize_domain(self.solver, w=100.0, h=200.0, dx=0.4, dy=0.2)
    
        self.assertEqual(self.solver.nx, 250)
        self.assertEqual(self.solver.ny, 1000)


    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        self.solver.dx = 0.4
        self.solver.dy = 0.2
        self.solver.initialize_physical_parameters(self.solver, d=20.0, T_cold=500.0, T_hot=550.0)
    	
        self.assertAlmostEqual(0.0512, self.solver.dt, 5)


    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        self.solver.T_cold = 500.0
        self.solver.T_hot = 550.0
        self.solver.nx = 250
        self.solver.ny = 1000
        self.solver.dx = 0.4
        self.solver.dy = 0.2
    
        # I feel like this is bad practice because I should calculate these 
        # values manualy, but my Input values are to high, so I do it automated ;-)
        manuel_u = 500.0 * np.ones((250, 1000))
        r, cx, cy = 2, 5, 5
        r2 = r ** 2
        for i in range(250):
            for j in range(1000):
                p2 = (i * 0.4 - cx) ** 2 + (j * 0.2 - cy) ** 2
                if p2 < r2:
                    manuel_u[i, j] = 550.0
        
        automated_u = self.solver.set_initial_condition(self.solver)
        
        for i in range(self.solver.nx):
            for j in range(self.solver.ny):
                self.assertEqual(manuel_u[i,j], automated_u[i,j])
   

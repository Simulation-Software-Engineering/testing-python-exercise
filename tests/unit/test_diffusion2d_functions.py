"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
from unittest import TestCase
import numpy as np

class TestDiffusion2D(TestCase):

    """
    Test suite for mathematical operations functions.
    """
    def setUp(self):
        self.solver = SolveDiffusion2D()

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        # input param.
        w=20.0
        h=40.0
        dx=0.1
        dy=0.5
        
        # exact result
        exact_nx=200
        exact_ny=80
        
        # actual
        self.solver.initialize_domain(w,h,dx,dy)
    
        # test
        self.assertEqual(exact_nx,self.solver.nx)
        self.assertEqual(exact_ny,self.solver.ny)
    
    
    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_physical_parameters_domain
        """
        # input param.
        dx=0.1
        dy=0.5
        d=5.
        T_cold=100.
        T_hot=500.
    
        # expect result
        expect_dt=9.61538*10**(-4)
        
        # actual
        self.solver.dx=dx
        self.solver.dy=dy
        self.solver.initialize_physical_parameters(d,T_cold,T_hot)
    
        # test
        self.assertAlmostEqual(expect_dt,self.solver.dt,5)
        self.assertEqual(T_cold,self.solver.T_cold)
        self.assertEqual(T_hot,self.solver.T_hot)
    
    
    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.set_initial_function
        """
        # input param.
        dx=0.1
        dy=0.5
        nx=40
        ny=80
        T_cold=100.
        T_hot=500.
        
        # exact result
        exact_u = T_cold * np.ones((nx, ny))
        r, cx, cy = 2, 5, 5
        r2 = r ** 2
        for i in range(nx):
            for j in range(ny):
                p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
                if p2 < r2:
                    exact_u[i, j] = T_hot
    
        # actual
        self.solver.dx=dx
        self.solver.dy=dy
        self.solver.nx=nx
        self.solver.ny=ny
        self.solver.T_cold=T_cold
        self.solver.T_hot=T_hot            
        actual_u = self.solver.set_initial_condition()
        
        # test
        for i in range(nx):
            for j in range(ny):
                self.assertEqual(exact_u[i,j], actual_u[i,j])

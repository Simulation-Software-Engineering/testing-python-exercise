import unittest
import numpy as np
from diffusion2d import SolveDiffusion2D

class TestDiffusion2D(unittest.TestCase):
    
    def setUp(self):
        self.solver = SolveDiffusion2D()

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        w = 20.
        h = 10.
        dx = 0.2
        dy = 0.5
        
        self.solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
        
        self.assertEqual(self.solver.nx, int(w / dx))
        self.assertEqual(self.solver.ny, int(h / dy))

    def test_initialize_physical_parameters(self):
        """
        Check function SolveDiffusion2D.initialize_physical_parameters
        """
        d = 5.
        T_cold = 200.
        T_hot = 600.
        
        self.solver.dx = 0.2
        self.solver.dy = 0.5
        
        self.solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)
        
        dx2 = self.solver.dx * self.solver.dx
        dy2 = self.solver.dy * self.solver.dy
        expected_dt = dx2 * dy2 / (2 * d * (dx2 + dy2))
        
        self.assertAlmostEqual(self.solver.dt, expected_dt)

    def test_set_initial_condition(self):
        """
        Check function SolveDiffusion2D.set_initial_condition
        """
        self.solver.nx = 10
        self.solver.ny = 10
        self.solver.dx = 1.0
        self.solver.dy = 1.0
        self.solver.T_cold = 300.
        self.solver.T_hot = 700.
        
        u = self.solver.set_initial_condition()
        
        expected_u = self.solver.T_cold * np.ones((self.solver.nx, self.solver.ny))
        r, cx, cy = 2, 5, 5
        r2 = r ** 2
        for i in range(self.solver.nx):
            for j in range(self.solver.ny):
                p2 = (i * self.solver.dx - cx) ** 2 + (j * self.solver.dy - cy) ** 2
                if p2 < r2:
                    expected_u[i, j] = self.solver.T_hot
                    
        self.assertTrue(np.array_equal(u, expected_u))

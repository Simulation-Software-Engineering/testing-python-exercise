"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import unittest
import numpy as np

class TestDiffusion2d(unittest.TestCase):

    def setUp(self):
        self.dx = 0.1
        self.w = 20.
        self.h = 20.
        self.dy = 0.2
        self.nx = int(self.w / self.dx)
        self.ny = int(self.h / self.dy)
        self.solver = SolveDiffusion2D()
        self.D = 3.
        self.T_cold = 300.
        self.T_hot = 900.
        self.solver = SolveDiffusion2D()
    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """




        self.solver.initialize_domain(self.w,self.h,self.dx,self.dy)

        self.assertEqual(self.solver.nx,self.nx)
        self.assertEqual(self.solver.ny, self.ny)

    def test_initialize_physical_parameters(self):

        """self.dx = 0.1
        self.dy = 0.2
        self.solver = SolveDiffusion2D()"""

        # Computing reference values
        calc_dx2 = self.dx * self.dx
        calc_dy2 = self.dy * self.dy
        calc_dt = calc_dx2 * calc_dy2 / (2 * self.D * (calc_dx2 + calc_dy2))

        self.solver.initialize_physical_parameters()

        #self.assertEqual(self.solver.dt,calc_dt)


    def test_set_initial_condition(self):



        u = self.T_cold * np.ones((self.nx, self.ny))

        # Initial conditions - circle of radius r centred at (cx,cy) (mm)
        r, cx, cy = 2, 5, 5
        r2 = r ** 2
        for i in range(self.nx):
            for j in range(self.ny):
                p2 = (i * self.dx - cx) ** 2 + (j * self.dy - cy) ** 2
                if p2 < r2:
                    u[i, j] = self.T_hot

        u_diff = self.solver.set_initial_condition()

        self.assertEqual(u_diff.tolist(), u.tolist())



"""
Tests for functions in class SolveDiffusion2D
"""
import unittest
from diffusion2d import SolveDiffusion2D

class TestDiffusion2D(unittest.TestCase):

    def setUp(self):
        self.solver = SolveDiffusion2D()

    def test_initialize_domain(self):
        """
        Check if nx and ny are calculated correctly.
        """
        w = 20.0
        h = 10.0
        dx = 2.0
        dy = 5.0

        expected_nx = 10
        expected_ny = 2

        self.solver.initialize_domain(w, h, dx, dy)

        self.assertEqual(self.solver.nx, expected_nx)
        self.assertEqual(self.solver.ny, expected_ny)

    def test_initialize_physical_parameters(self):
        """
        Check if dt is calculated correctly.
        """
        d = 5.0
        T_cold = 200.0
        T_hot = 500.0
        
        self.solver.dx = 2.0
        self.solver.dy = 2.0

        # 2. Expected output 
        # dt = (dx^2 * dy^2) / (2 * d * (dx^2 + dy^2))
        # dt = (4 * 4) / (2 * 5 * (4 + 4))
        # dt = 16 / (10 * 8) = 16 / 80 = 0.2
        expected_dt = 0.2

        self.solver.initialize_physical_parameters(d, T_cold, T_hot)

        self.assertAlmostEqual(self.solver.dt, expected_dt, places=5)

    def test_set_initial_condition(self):
        """
        Check if u matrix is initialized correctly.
        """
        self.solver.nx = 3
        self.solver.ny = 3
        self.solver.dx = 1.0
        self.solver.dy = 1.0
        self.solver.T_cold = 100.0
        self.solver.T_hot = 200.0

        u = self.solver.set_initial_condition()

        self.assertEqual(u[0, 0], 100.0)
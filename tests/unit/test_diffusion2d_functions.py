"""
Tests for functions in class SolveDiffusion2D
"""
import numpy as np
#import pytest
from diffusion2d import SolveDiffusion2D

from unittest import TestCase


class TestOperations(TestCase):
    """
    Test suite for mathematical operations functions.
    """
    def setUp(self):
        # Fixture
        self.w = 12.
        self.h = 20.
        self.dx = 0.4
        self.dy = 0.2
        self.D = 0.5
        self.T_cold = 300.
        self.T_hot = 700.

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()

        expected_nx = 30 #int(self.w / self.dx)
        expected_ny = 100 #int(self.h / self.dy)

        solver.initialize_domain(self.w,self.h,self.dx,self.dy)

        self.assertEqual(solver.nx, expected_nx)
        self.assertEqual(solver.ny, expected_ny)

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.dx = self.dx
        solver.dy = self.dy

        #dx**2 * dy**2 / (2 * d * (dx**2 + dy**2))
        expected_dt = 0.032

        solver.initialize_physical_parameters(self.D)

        self.assertAlmostEqual(solver.dt, expected_dt, 6)

    def test_get_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.T_cold = self.T_cold
        solver.T_hot = self.T_hot
        solver.initialize_domain(self.w,self.h,self.dx,self.dy)

        expected_u = self.T_cold * np.ones((solver.nx, solver.ny))

        # Initial conditions - circle of radius r centred at (cx,cy) (mm)
        r, cx, cy = 2, 5, 5
        r2 = r ** 2
        for i in range(solver.nx):
            for j in range(solver.ny):
                p2 = (i * solver.dx - cx) ** 2 + (j * solver.dy - cy) ** 2
                if p2 < r2:
                    expected_u[i, j] = self.T_hot

        actual_u = solver.get_initial_condition()

        for i in range(solver.nx):
            for j in range(solver.ny):
                self.assertEqual(actual_u[i,j], expected_u[i,j])

# def test_initialize_domain():
#     """
#     Check function SolveDiffusion2D.initialize_domain
#     """
#     solver = SolveDiffusion2D()
#
#     w = 12.
#     h = 20.
#     dx = 0.4
#     dy = 0.2
#     expected_nx = 30 #int(w / dx)
#     expected_ny = 100 #int(h / dy)
#
#     solver.initialize_domain(w,h,dx,dy)
#
#     assert solver.nx == expected_nx
#     assert solver.ny == expected_ny
#
# def test_initialize_physical_parameters():
#     """
#     Checks function SolveDiffusion2D.initialize_domain
#     """
#     solver = SolveDiffusion2D()
#     solver.dx = 0.2
#     solver.dy = 0.4
#     d=5.
#
#     #dx**2 * dy**2 / (2 * d * (dx**2 + dy**2))
#     expected_dt = pytest.approx(0.0032, abs=0.000001)
#
#     solver.initialize_physical_parameters(d)
#
#     assert solver.dt == expected_dt
#
# def test_get_initial_condition():
#     """
#     Checks function SolveDiffusion2D.get_initial_function
#     """
#     solver = SolveDiffusion2D()
#     solver.T_cold = 300.
#     solver.T_hot = 700.
#     solver.dx = 0.1
#     solver.dy = 0.2
#     solver.nx = 100
#     solver.ny = 50
#
#     expected_u = solver.T_cold * np.ones((solver.nx, solver.ny))
#
#     # Initial conditions - circle of radius r centred at (cx,cy) (mm)
#     r, cx, cy = 2, 5, 5
#     r2 = r ** 2
#     for i in range(solver.nx):
#         for j in range(solver.ny):
#             p2 = (i * solver.dx - cx) ** 2 + (j * solver.dy - cy) ** 2
#             if p2 < r2:
#                 expected_u[i, j] = solver.T_hot
#
#     actual_u = solver.get_initial_condition()
#
#     assert np.all(actual_u == expected_u)

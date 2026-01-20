"""
Tests for functions in class SolveDiffusion2D
"""
import unittest
from diffusion2d import SolveDiffusion2D

class TestDiffusion2D(unittest.TestCase):
    def test_initialize_domain(self):
            """
            Check function SolveDiffusion2D.initialize_domain
            """
            # Fixture (Input data)
            w = 20.0
            h = 10.0
            dx = 2.0
            dy = 2.0

            # Expected Result (Manual calculation)
            expected_nx = 10  # 20 / 2
            expected_ny = 5   # 10 / 2

            # Action (Call the function)
            solver = SolveDiffusion2D()
            solver.initialize_domain(w, h, dx, dy)

            # Assertion (Check if code matches expectation)
            self.assertEqual(solver.nx, expected_nx)
            self.assertEqual(solver.ny, expected_ny)


    def test_initialize_physical_parameters(self):
        """
        Check function SolveDiffusion2D.initialize_physical_parameters
        """
        solver = SolveDiffusion2D()

        # Manually set the state (mocking domain initialization)
        solver.dx = 2.0
        solver.dy = 2.0
        d = 4.0

        # Expected dt calculation: 
        # dt = (dx*dx * dy*dy) / (2 * d * (dx*dx + dy*dy))
        # dt = (4 * 4) / (2 * 4 * (4 + 4)) = 16 / 64 = 0.25
        expected_dt = 0.25

        solver.initialize_physical_parameters(d=d)

        self.assertAlmostEqual(solver.dt, expected_dt)

    def test_set_initial_conditions(self):
        """
        Check function SolveDiffusion2D.set_initial_conditions
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=10., h=10., dx=1., dy=1.)
        solver.initialize_physical_parameters(T_cold=100., T_hot=500.)
        
        # Action
        u = solver.set_initial_condition()
        
        # Assertion: Check a known hot spot (center) and cold spot (corner)
        # Center should be 500.0 (Hot)
        self.assertEqual(u[5, 5], 500.0)
        
        # Corner (0,0) should be 100.0 (Cold)
        self.assertEqual(u[0, 0], 100.0)

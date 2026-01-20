import unittest
import numpy as np
from diffusion2d import SolveDiffusion2D

class TestDiffusion2D(unittest.TestCase):
    
    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_physical_parameters 
        working with initialize_domain
        """
        solver = SolveDiffusion2D()
        w = 10.0
        h = 10.0
        dx = 1.0
        dy = 1.0
        d = 4.0
        
        # Expected dt calculation (Integration test: we rely on initialize_domain working too)
        # dt = (dx*dx * dy*dy) / (2 * d * (dx*dx + dy*dy))
        # dt = (1 / (2 * 4 * 2)) = 1 / 16 = 0.0625
        expected_dt = 0.0625

        solver.initialize_domain(w, h, dx, dy)
        solver.initialize_physical_parameters(d=d)

        self.assertAlmostEqual(solver.dt, expected_dt)

    def test_get_initial_function(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        working with initialize_domain and initialize_physical_parameters
        """
        solver = SolveDiffusion2D()
        
        # 1. Initialize the solver fully
        solver.initialize_domain(w=10., h=10., dx=1., dy=1.)
        solver.initialize_physical_parameters(T_cold=100., T_hot=500.)
        
        # 2. Call the function
        u_actual = solver.set_initial_condition()
        
        # 3. Manually calculate Expected Result
        expected_u = 100.0 * np.ones((10, 10))
        
        # Loop to create the hot circle
        for i in range(10):
            for j in range(10):
                # Calculate distance from center (5.0, 5.0)
                # Note: The code uses coordinates based on dx, dy, so:
                x = i * 1.0
                y = j * 1.0
                p2 = (x - 5.0)**2 + (y - 5.0)**2
                
                # Radius is squared in the comparison (radius=2, r^2=4)
                if p2 < 4.0:
                    expected_u[i, j] = 500.0
        
        # 4. Compare the full arrays
        np.testing.assert_array_equal(u_actual, expected_u)
"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import numpy as np

def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(dx=0.2, dy=0.6)

    d = 2.
    T_cold = 150.
    T_hot = 350.
    dx2, dy2 = solver.dx * solver.dx, solver.dy * solver.dy
    dt = dx2 * dy2 / (2 * d * (dx2 + dy2))
    solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)
    assert dt == solver.dt, "wrong value of dt"

def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(dx=0.2, dy=0.6)
    solver.initialize_physical_parameters(d=2., T_cold=150., T_hot=350.)
    u = solver.T_cold * np.ones((solver.nx, solver.ny))

    r, cx, cy = 2, 5, 5
    r2 = r ** 2
    for i in range(solver.nx):
        for j in range(solver.ny):
            p2 = (i * solver.dx - cx) ** 2 + (j * solver.dy - cy) ** 2
            if p2 < r2:
                u[i, j] = solver.T_hot

    ground_truth = u.copy()

    assert np.array_equal(ground_truth, solver.set_initial_condition()), "initial condition not set correctly"
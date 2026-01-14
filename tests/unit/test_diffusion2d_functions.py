"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import numpy as np

def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    w = 5.
    h = 20.
    dx = 0.2
    dy = 0.6
    nx = int(w / dx)
    ny = int(h / dy)

    solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
    assert nx == solver.nx, "wrong value of nx"
    assert ny == solver.ny, "wrong value of ny"


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    
    solver.dx = 0.2
    solver.dy = 0.6

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
    solver.w = 5.
    solver.h = 20.
    solver.dx = 0.2
    solver.dy = 0.6
    solver.nx = int(solver.w / solver.dx)
    solver.ny = int(solver.h / solver.dy)
    solver.dx = 0.2
    solver.dy = 0.6

    solver.d = 2.
    solver.T_cold = 150.
    solver.T_hot = 350.

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


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
    w= 10.0
    h= 5.0
    dx = 0.1
    dy = 0.1

    correct_nx = int(w/ dx)
    correct_ny = int(h/ 0.1)

    solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)

    assert solver.w == w
    assert solver.h == h
    assert solver.dx == dx
    assert solver.dy == dy
    assert solver.nx == correct_nx
    assert solver.ny == correct_ny


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.dx = 0.1
    solver.dy = 0.1
    D = 2.0
    T_cold = 200.0
    T_hot = 1000.0

    dx2 = solver.dx * solver.dx
    dy2 = solver.dy * solver.dy
    dt = dx2 * dy2 / (2.0 * D * (dx2 + dy2))

    solver.initialize_physical_parameters(d=D, T_cold=T_cold, T_hot=T_hot)

    assert solver.D == D
    assert solver.T_cold == T_cold
    assert solver.T_hot == T_hot
    assert solver.dt == dt


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.dx = 1.0
    solver.dy = 1.0
    solver.nx = 11
    solver.ny = 11

    solver.T_cold = 300.0
    solver.T_hot = 700.0

    u = solver.set_initial_condition()

    u_expected = solver.T_cold * np.ones((solver.nx, solver.ny))

    r, cx, cy = 2, 5, 5
    r2 = r ** 2

    for i in range(solver.nx):
        for j in range(solver.ny):
            p2 = (i * solver.dx - cx) ** 2 + (j * solver.dy - cy) ** 2
            if p2 < r2:
                u_expected[i, j] = solver.T_hot

    assert np.array_equal(u, u_expected)

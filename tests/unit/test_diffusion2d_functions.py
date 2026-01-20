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

    w = 12.0
    h = 8.0
    dx = 0.2
    dy = 0.2

    nx = int(w / dx)
    ny = int(h / dy)

    solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)

    assert solver.w == w
    assert solver.h == h
    assert solver.dx == dx
    assert solver.dy == dy
    assert solver.nx == nx
    assert solver.ny == ny


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()

    dx = 0.2
    dy = 0.2
    d = 5.
    T_cold = 290.0
    T_hot = 750.0

    dx2, dy2 = dx * dx, dy * dy
    dt = dx2 * dy2 / (2 * d * (dx2 + dy2))

    solver.dx = dx
    solver.dy = dy
    solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)

    assert solver.D == d
    assert solver.T_cold == T_cold
    assert solver.T_hot == T_hot
    assert solver.dt == dt

def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()

    dx = 0.2
    dy = 0.2
    T_cold = 290.0
    T_hot = 750.0
    nx = int(12.0 / dx)
    ny = int(8.0 / dy)

    u = T_cold * np.ones((nx, ny))
    r, cx, cy = 2, 5, 5
    r2 = r ** 2
    for i in range(nx):
        for j in range(ny):
            p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
            if p2 < r2:
                u[i, j] = T_hot

    solver.nx = nx
    solver.ny = ny
    solver.dx = dx
    solver.dy = dy
    solver.T_cold = T_cold
    solver.T_hot = T_hot
    u_return = solver.set_initial_condition()

    assert np.array_equal(u, u_return)
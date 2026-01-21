"""
Tests for functions in class SolveDiffusion2D
"""
import numpy as np
import pytest

from diffusion2d import SolveDiffusion2D


def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()

    w, h = 3.0, 2.0
    dx, dy = 0.5, 0.25

    solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)

    assert solver.w == w
    assert solver.h == h
    assert solver.dx == dx
    assert solver.dy == dy

    assert solver.nx == int(w / dx)
    assert solver.ny == int(h / dy)


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_physical_parameters
    """
    solver = SolveDiffusion2D()

    solver.dx = 0.5
    solver.dy = 0.25

    d = 4.0
    T_cold = 300.0
    T_hot = 700.0

    solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)

    assert solver.D == d
    assert solver.T_cold == T_cold
    assert solver.T_hot == T_hot

    dx2, dy2 = solver.dx * solver.dx, solver.dy * solver.dy
    expected_dt = dx2 * dy2 / (2 * solver.D * (dx2 + dy2))
    assert np.isclose(solver.dt, expected_dt)


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.set_initial_condition
    """
    solver = SolveDiffusion2D()

    solver.nx = 30
    solver.ny = 20
    solver.dx = 0.5
    solver.dy = 0.25
    solver.T_cold = 300.0
    solver.T_hot = 700.0

    u0 = solver.set_initial_condition()

    assert isinstance(u0, np.ndarray)
    assert u0.shape == (solver.nx, solver.ny)
    assert np.issubdtype(u0.dtype, np.floating)

    assert np.isclose(u0.min(), solver.T_cold)
    assert np.isclose(u0.max(), solver.T_hot)


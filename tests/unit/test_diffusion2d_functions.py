"""
Tests for functions in class SolveDiffusion2D
"""

import unittest
from diffusion2d import SolveDiffusion2D


def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    w = 20.
    h = 10.
    dx = 2.
    dy = 2.
    # init solver
    solver = SolveDiffusion2D()
    
    # run function and assert
    solver.initialize_domain(w, h, dx, dy)
    assert solver.nx == 10
    assert solver.ny == 5

def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    # init solver
    solver = SolveDiffusion2D()
    solver.dx = 2.
    solver.dy = 2.

    d = 4.
    t_cold = 300.
    t_hot = 700.

    solver.initialize_physical_parameters(d, t_cold, t_hot)
    assert solver.dt == 0.25


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    # init solver
    solver = SolveDiffusion2D()
    solver.nx = 3
    solver.ny = 3
    solver.dx = 1.
    solver.dy = 1.
    solver.T_cold = 200.
    solver.T_hot = 500.

    # call function and assert
    u = solver.set_initial_condition()
    assert u.shape == (3, 3)
    assert u[0, 0] == 200.

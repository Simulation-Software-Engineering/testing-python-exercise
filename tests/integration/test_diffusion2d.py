"""
Tests for functionality checks in class SolveDiffusion2D
"""
import unittest
import numpy as np
from diffusion2d import SolveDiffusion2D


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    w = 10.
    h = 10.
    dx = 1.
    dy = 1.
    d = 4.
    t_cold = 300.
    t_hot = 700.
    solver.initialize_domain(w, h, dx,dy)
    solver.initialize_physical_parameters(d, t_cold, t_hot)

    assert solver.dt == 0.0625

def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    w = 4.
    h = 4.
    dx = 1.
    dy = 1.
    d = 4.
    t_cold = 300.
    t_hot = 700.
    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d, t_cold, t_hot)
    
    u = solver.set_initial_condition()

    assert u.shape == (4, 4)
    assert u[0, 0] == 300.

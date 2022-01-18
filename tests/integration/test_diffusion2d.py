"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import numpy as np
import pytest


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(100.0, 200.0, 0.4, 0.2)
    
    solver.initialize_physical_parameters(20.0, 500.0, 550.0)
    assert abs(solver.dt - 0.0512) < 1e-10


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(100.0, 200.0, 0.4, 0.2)
    
    solver.initialize_physical_parameters(20.0, 500.0, 550.0)
    
    # I feel like this is bad practice because I should calculate these 
    # values manualy, but my Input values are to high, so I do it automated ;-)
    manuel_u = 500.0 * np.ones((250, 1000))
    r, cx, cy = 2, 5, 5
    r2 = r ** 2
    for i in range(250):
        for j in range(1000):
            p2 = (i * 0.4 - cx) ** 2 + (j * 0.2 - cy) ** 2
            if p2 < r2:
                manuel_u[i, j] = 550.0
        
    automated_u = solver.set_initial_condition()
    for i in range(solver.nx):
        for j in range(solver.ny):
            assert manuel_u[i,j] == automated_u[i,j]

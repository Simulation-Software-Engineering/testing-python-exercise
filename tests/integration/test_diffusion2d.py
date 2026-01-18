"""
Tests for functionality checks in class SolveDiffusion2D
"""
import numpy as np
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  
from diffusion2d import SolveDiffusion2D

def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_physical_parameters 
    Integration test: domain setup affects dt calculation
    """
    solver = SolveDiffusion2D()
    
    # Non-default values for integration test
    w, h, dx, dy = 12.0, 8.0, 0.2, 0.1
    D, T_cold, T_hot = 3.5, 280.0, 750.0
    
    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(D, T_cold, T_hot)
    
    # Manual calculation of expected dt (depends on domain dx,dy)
    dx2, dy2 = dx**2, dy**2
    expected_dt = dx2 * dy2 / (2 * D * (dx2 + dy2))
    
    assert abs(solver.dt - expected_dt) < 1e-12
    assert solver.D == D
    assert solver.T_cold == T_cold
    assert solver.T_hot == T_hot

def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.set_initial_condition
    Integration test: domain + physics → correct initial field u
    """
    solver = SolveDiffusion2D()
    
    # Default-like params to match code's circle
    solver.initialize_domain()
    solver.initialize_physical_parameters()
    
    u = solver.set_initial_condition()
    
    # Replicate exact circle logic from set_initial_condition
    r, cx, cy = 2, 5, 5
    r2 = r**2
    expected_u = solver.T_cold * np.ones((solver.nx, solver.ny))
    
    for i in range(solver.nx):
        for j in range(solver.ny):
            p2 = (i * solver.dx - cx)**2 + (j * solver.dy - cy)**2
            if p2 < r2:
                expected_u[i,j] = solver.T_hot
    
    # Exact match (no floating point issues)
    assert np.array_equal(u, expected_u)
    assert u.shape == (solver.nx, solver.ny)

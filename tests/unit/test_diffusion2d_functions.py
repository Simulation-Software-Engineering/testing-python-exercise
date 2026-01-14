"""
Tests for functions in class SolveDiffusion2D
"""

import numpy as np
from diffusion2d import SolveDiffusion2D


def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    
    # Use non-default values to test properly
    w = 20.0
    h = 30.0
    dx = 0.5
    dy = 0.2
    
    # Call the function
    solver.initialize_domain(w, h, dx, dy)
    
    # Manually calculate expected values
    expected_nx = int(w / dx)  # int(20.0 / 0.5) = 40
    expected_ny = int(h / dy)  # int(30.0 / 0.2) = 150
    
    # Assert that the values match
    assert solver.nx == expected_nx, f"Expected nx={expected_nx}, but got {solver.nx}"
    assert solver.ny == expected_ny, f"Expected ny={expected_ny}, but got {solver.ny}"
    assert solver.w == w
    assert solver.h == h
    assert solver.dx == dx
    assert solver.dy == dy


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_physical_parameters
    """
    # Create solver and mock the required member variables (instead of calling initialize_domain)
    solver = SolveDiffusion2D()
    
    # Manually set the required member variables
    dx = 0.3
    dy = 0.3
    solver.dx = dx
    solver.dy = dy
    
    # Test parameters
    d = 2.5
    T_cold = 250.0
    T_hot = 750.0
    
    # Call the function
    solver.initialize_physical_parameters(d, T_cold, T_hot)
    
    # Manually calculate expected dt
    dx2 = dx * dx
    dy2 = dy * dy
    expected_dt = dx2 * dy2 / (2 * d * (dx2 + dy2))
    
    # Assert values
    assert solver.D == d
    assert solver.T_cold == T_cold
    assert solver.T_hot == T_hot
    assert abs(solver.dt - expected_dt) < 1e-10, f"Expected dt={expected_dt}, but got {solver.dt}"


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.set_initial_condition
    """
    # Create solver and manually set required member variables (mocking initialize_domain and initialize_physical_parameters)
    solver = SolveDiffusion2D()
    
    # Mock the required member variables
    w = 10.0
    h = 10.0
    dx = 0.5
    dy = 0.5
    solver.w = w
    solver.h = h
    solver.dx = dx
    solver.dy = dy
    solver.nx = int(w / dx)
    solver.ny = int(h / dy)
    
    T_cold = 300.0
    T_hot = 700.0
    solver.T_cold = T_cold
    solver.T_hot = T_hot
    
    # Call the function
    u = solver.set_initial_condition()
    
    # Check properties of the returned array
    assert u.shape == (solver.nx, solver.ny), f"Expected shape {(solver.nx, solver.ny)}, got {u.shape}"
    
    # Check that most values are T_cold
    assert np.all(u >= T_cold), f"Some values are below T_cold={T_cold}"
    assert np.all(u <= T_hot), f"Some values are above T_hot={T_hot}"
    
    # Check that center has hot temperature (circular disc at center)
    cx, cy = 5, 5
    r = 2
    assert u[int(cx/dx), int(cy/dy)] == T_hot, "Center should have T_hot"

"""
Tests for functionality checks in class SolveDiffusion2D
"""

import numpy as np
from diffusion2d import SolveDiffusion2D


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    
    # Initialize domain with specific values
    w = 12.0
    h = 12.0
    dx = 0.4
    dy = 0.4
    solver.initialize_domain(w, h, dx, dy)
    
    # Initialize physical parameters
    d = 3.0
    T_cold = 250.0
    T_hot = 750.0
    solver.initialize_physical_parameters(d, T_cold, T_hot)
    
    # Manually calculate expected dt
    dx2 = dx * dx
    dy2 = dy * dy
    expected_dt = dx2 * dy2 / (2 * d * (dx2 + dy2))
    
    # Verify the dt calculation
    assert abs(solver.dt - expected_dt) < 1e-10, \
        f"Expected dt={expected_dt}, but got {solver.dt}"
    
    # Also verify that all parameters are set correctly
    assert solver.D == d
    assert solver.T_cold == T_cold
    assert solver.T_hot == T_hot
    assert solver.dx == dx
    assert solver.dy == dy


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    w = 10.0
    h = 10.0
    dx = 0.5
    dy = 0.5
    solver.initialize_domain(w, h, dx, dy)
    
    # Initialize physical parameters
    d = 4.0
    T_cold = 300.0
    T_hot = 700.0
    solver.initialize_physical_parameters(d, T_cold, T_hot)
    
    # Get initial condition
    u = solver.set_initial_condition()
    
    # Verify shape matches domain
    expected_shape = (solver.nx, solver.ny)
    assert u.shape == expected_shape, \
        f"Expected shape {expected_shape}, but got {u.shape}"
    
    # Manually compute expected initial condition
    # Most values should be T_cold
    u_expected = T_cold * np.ones((solver.nx, solver.ny))
    
    # Circular disc at center with T_hot
    r, cx, cy = 2, 5, 5
    r2 = r ** 2
    for i in range(solver.nx):
        for j in range(solver.ny):
            p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
            if p2 < r2:
                u_expected[i, j] = T_hot
    
    # Check that the computed u matches expected
    assert np.allclose(u, u_expected), \
        "Initial condition array does not match expected values"
    
    # Verify all values are within [T_cold, T_hot]
    assert np.all(u >= T_cold), f"Some values are below T_cold={T_cold}"
    assert np.all(u <= T_hot), f"Some values are above T_hot={T_hot}"

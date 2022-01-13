"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import numpy as np

def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    # set values
    w  = 2.
    h  = 3.
    dx = 0.5
    dy = 0.5

    nx_expected = 4
    ny_expected = 6

    solver = SolveDiffusion2D()
    solver.initialize_domain(w, h, dx, dy)
    
    assert nx_expected == solver.nx
    assert ny_expected == solver.ny


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()

    T_cold = 100.
    T_hot  = 1000.

    d      = 2. 
    dx     = 1.
    dy     = 1.
    
    dt_expected = 0.125

    solver.dx = dx 
    solver.dy = dy

    solver.initialize_physical_parameters(d, T_cold, T_hot)

    assert dt_expected == solver.dt
    assert T_cold == solver.T_cold
    assert T_hot == solver.T_hot
    

def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()

    solver.T_hot  = 333. 
    solver.T_cold = -17.
    solver.nx     = 2
    solver.ny     = 2
    solver.dx     = 4.5
    solver.dy     = 5.5

    u_expected = np.array([[-17., -17.], [-17., 333.]])
    u_returned  = solver.set_initial_condition()
    
    #assert all([a == b for a, b in zip(u_expected, u_returned)])
    assert u_expected[0][0] == u_returned[0][0]
    assert u_expected[1][0] == u_returned[1][0]
    assert u_expected[0][1] == u_returned[0][1]
    assert u_expected[1][1] == u_returned[1][1]

    
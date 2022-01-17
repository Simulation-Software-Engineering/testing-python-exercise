"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import numpy as np

def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    # input param.
    w=20.0
    h=40.0
    dx=0.1
    dy=0.5
    T_cold=100.
    T_hot=500.
    d=5.
    
    # expect result
    expect_dt=9.61538*10**(-4)
    tol=10**(-5)
    
    # actual
    solver = SolveDiffusion2D()
    solver.initialize_domain(w,h,dx,dy)
    solver.initialize_physical_parameters(d,T_cold,T_hot)
    
    # test
    assert np.abs(expect_dt-solver.dt) < tol
    


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    # input param.
    w=20.0
    h=40.0
    dx=0.1
    dy=0.5
    nx=40
    ny=80
    
    T_cold=100.
    T_hot=500.
    d=5.
    
    # expect result
    exact_u = T_cold * np.ones((nx, ny))
    r, cx, cy = 2, 5, 5
    r2 = r ** 2
    for i in range(nx):
        for j in range(ny):
            p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
            if p2 < r2:
                exact_u[i, j] = T_hot

    # actual
    solver = SolveDiffusion2D()
    solver.initialize_domain(w,h,dx,dy)
    solver.initialize_physical_parameters(d,T_cold,T_hot)
    actual_u = solver.set_initial_condition()
    
    # test
    for i in range(nx):
        for j in range(ny):
            assert exact_u[i,j] == actual_u[i,j]
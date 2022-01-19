"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import numpy as np
    

def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """

    # input functions for init physical param and init domain
    w  = 1.
    h  = 2.
    dx = 1.
    dy = 1.

    d      =   2.
    T_cold = -13.
    T_hot  =  127. 
    
    # comp dt_expected
    dt_expected = 0.125
    
    # call init domain and init physical param
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
    solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)

    assert dt_expected == solver.dt
    
def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()

    w  = 9.
    h  = 11.
    dx = 4.5
    dy = 5.5

    d      =   2.
    T_cold = -13.
    T_hot  =  127.

    # expected outcome
    nx = int(w/dx)
    ny = int(h/dy)
    u_expected = T_cold * np.ones((nx, ny)) 
    u_expected[1,1] = T_hot 

    # computed u
    solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
    solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)

    u_computed = solver.set_initial_condition()

    for x in range(nx):
        for y in range(ny):
            assert u_computed[x,y] == u_expected[x,y]


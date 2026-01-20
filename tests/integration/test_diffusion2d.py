"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import pytest

def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    w, h, dx, dy = 10.0, 10.0, 0.1, 0.1
    d = 4.0
    expected_dt = 0.000625
    
    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d=d)
    
    assert solver.dt == pytest.approx(expected_dt)


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.set_initial_condition
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=10.0, h=10.0, dx=0.1, dy=0.1)
    solver.initialize_physical_parameters(d=4.0, T_cold=300.0, T_hot=700.0)
    
    u = solver.set_initial_condition()
    
    assert u.shape == (100, 100)
    assert u[50, 50] == 700.0
    assert u[0, 0] == 300.0
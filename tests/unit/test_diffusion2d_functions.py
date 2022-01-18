"""
Tests for functions in class SolveDiffusion2D
"""

from cv2 import solve
from diffusion2d import SolveDiffusion2D


def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(20.,20.,0.01,0.01)
    expected_nx = 2000
    expected_ny = 2000
    assert expected_nx == solver.nx
    assert expected_ny == solver.ny


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.dx = 0.1
    solver.dy = 0.1
    solver.initialize_physical_parameters(5.,200.,800.)
    expected_dt = 0.0005
    assert expected_dt == solver.dt


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()

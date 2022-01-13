"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D


def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    # test as many variations as possible
    solver.initialize_domain(5., 4., .3, .35)

    assert type(solver.w) == float
    assert solver.w == 5.
    assert type(solver.h) == float
    assert solver.h == 4.
    assert type(solver.dx) == float
    assert solver.dx == .3
    assert type(solver.dy) == float
    assert solver.dy == .35
    assert type(solver.nx) == int
    assert solver.nx == 16 # int() truncates from 16 2/3 as usual
    assert type(solver.ny) == int
    assert solver.ny == 11 # this should also round down as usual


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_physical_parameters
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(5., 4., .3, .35)
    solver.initialize_physical_parameters(3., 250., 800.)

    assert type(solver.D) == float
    assert solver.D == 3.
    assert type(solver.T_cold) == float
    assert solver.T_cold == 250.
    assert type(solver.T_hot) == float
    assert solver.T_hot == 800.
    assert type(solver.dt) == float
    # standard test approach for float equality
    assert abs(solver.dt - .008647059) < 1e-9

def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    T_cold = 250.
    T_hot = 800.

    solver = SolveDiffusion2D()
    solver.initialize_domain(5., 4., .3, .35)
    solver.initialize_physical_parameters(3., T_cold, T_hot)
    u = solver.set_initial_condition()

    # Test center of (quarter-)circle for equality to T_hot
    assert u[15, 10] == T_hot

    # Test a few random points outside circle for equality to T_cold
    assert u[0, 0] == T_cold
    assert u[10, 3] == T_cold
    assert u[5, 6] == T_cold

    # Test edge of circle to ensure proper sizing and positioning
    assert u[14, 10] == T_hot and u[13, 10] == T_hot and u[15, 9] == T_hot
    assert u[12, 10] == T_cold and u[13, 9] == T_cold and u[15, 8] == T_cold and u[14, 9] == T_cold


    



"""
Tests for functions in class SolveDiffusion2D
"""
import numpy as np
import pytest

from diffusion2d import SolveDiffusion2D

@pytest.fixture
def solver():
    solver = SolveDiffusion2D()
    solver.dx = 0.2
    solver.dy = 0.2
    solver.nx = 200
    solver.ny = 250
    solver.T_cold = 200
    solver.T_hot = 800

    return solver

@pytest.mark.parametrize("w, h, dx, dy, exp_nx, exp_ny", [
    (40., 50., 0.2, 0.2, 200, 250),
    (40., 50., 0.2, 0.4, 200, 125)
])
def test_initialize_domain(solver, w, h, dx, dy, exp_nx, exp_ny):
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    solver.initialize_domain(w, h, dx, dy)

    assert solver.w == w
    assert solver.h == h
    assert solver.dx == dx
    assert solver.dy == dy
    assert solver.nx == exp_nx
    assert solver.ny == exp_ny

@pytest.mark.parametrize("w, h, dx, dy", [
    (40, 50., 0.2, 0.2),
    (40., 50, 0.2, 0.2),
    (40., 50., 1, 0.2),
    (40., 50., 0.2, 1)
])
def test_initialize_domain_assertion_error(solver, w, h, dx, dy):
    """
    Check function SolveDiffusion2D.initialize_domain.

    Check with the condition, that a parameter is not of type float.
    """
    with pytest.raises(AssertionError):
        solver.initialize_domain(w, h, dx, dy)

@pytest.mark.parametrize("dx, dy", [
    (.2, 0.),
    (0., .2)
])
def test_initialize_domain_zero_division(solver, dx, dy):
    """
    Check function SolveDiffusion2D.initialize_domain.

    Check with the condition, that either disk width or height is zero (error).
    """
    with pytest.raises(ZeroDivisionError):
        solver.initialize_domain(40., 50., dx, dy)

@pytest.mark.parametrize("d, T_cold, T_hot, exp_dt", [
    (5., 200., 800., 0.002)
])
def test_initialize_physical_parameters(solver, d, T_cold, T_hot, exp_dt):
    """
    Checks function SolveDiffusion2D.initialize_physical_parameters.
    """
    solver.initialize_physical_parameters(d, T_cold, T_hot)

    assert solver.D == d
    assert solver.T_cold == T_cold
    assert solver.T_hot == T_hot
    assert solver.dt == pytest.approx(exp_dt)

@pytest.mark.parametrize("d, T_cold, T_hot", [
    (5, 200., 800.),
    (5., 200, 800.),
    (5., 200., 800)
])
def test_initialize_physical_parameters_assertion_error(solver, d, T_cold, T_hot):
    """
    Checks function SolveDiffusion2D.initialize_physical_parameters.

    Check with the condition, that a parameter is not of type float.
    """
    with pytest.raises(AssertionError):
        solver.initialize_physical_parameters(d, T_cold, T_hot)


def test_initialize_physical_parameters_zero_division(solver):
    """
    Checks function SolveDiffusion2D.initialize_physical_parameters.

    Check that the correct error is thrown when zero division happens.
    """
    with pytest.raises(ZeroDivisionError):
        solver.initialize_physical_parameters(0., 200., 800.)

    with pytest.raises(ZeroDivisionError):
        solver.dx = 0.
        solver.dy = 0.
        solver.initialize_physical_parameters(5., 200., 800.)


def test_set_initial_condition(solver):
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver.nx = 2
    solver.ny = 2
    np.testing.assert_array_almost_equal(solver.set_initial_condition(), 200 * np.ones((solver.nx, solver.ny)))

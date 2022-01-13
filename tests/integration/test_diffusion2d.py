"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
from numpy import ones, array_equal

# just a copy of those from the other file
testing_params = {
        'domain': {
            # test as many variations as possible, also last two test rounding/truncation
            'w': 5., 'h': 4., 'dx': .3, 'dy': .35, 'nx': 16, 'ny': 11
        },
        'physical': {
            # assuming above values previously in use
            'D': 3., 'T_cold': 250., 'T_hot': 800., 'dt': .008647059
        }
    }

def init_solver():
    solver = SolveDiffusion2D()
    solver.initialize_domain(
        testing_params['domain']['w'],
        testing_params['domain']['h'],
        testing_params['domain']['dx'], 
        testing_params['domain']['dy']
    )
    solver.initialize_physical_parameters(
        testing_params['physical']['D'],
        testing_params['physical']['T_cold'],
        testing_params['physical']['T_hot']
    )
    return solver

def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = init_solver()
    
    # standard test approach for float equality
    assert abs(solver.dt - .008647059) < 1e-9


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    test_u = testing_params['physical']['T_cold'] * ones(
        (testing_params['domain']['nx'], testing_params['domain']['ny'])
    )
    # set quarter-circle to hot
    test_u[15, 9:11] = testing_params['physical']['T_hot']
    test_u[13:15, 10] = testing_params['physical']['T_hot']

    solver = init_solver()
    u = solver.set_initial_condition()
    assert array_equal(u, test_u)


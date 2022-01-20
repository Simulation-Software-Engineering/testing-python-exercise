"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import numpy as np
import math
from unittest import TestCase

#################
#### pyTEST #####
#################

# def test_initialize_domain():
#     """
#     Check function SolveDiffusion2D.initialize_domain
#     for a rectangual domain
#     """
#     # Fixture
#     rect_case_domain = {'w': 10., 'h': 1., 'dx': 0.1, 'dy': 0.1}

#     # Expected result
#     solution = {'nx': 100,'ny': 10}

#     # Actual result
#     solver = SolveDiffusion2D()
#     solver.initialize_domain(**rect_case_domain)

#     # Test
#     assert math.isclose(solver.nx, solution['nx']), "nx in initialize_domain"
#     assert math.isclose(solver.ny, solution['ny']), "ny in initialize_domain"

# def test_initialize_physical_parameters():
#     """
#     Checks function SolveDiffusion2D.initialize_domain
#     for a square case
#     """
#     # Fixture
#     square_domain = {'w': 1., 'h': 1., 'dx': 0.2, 'dy': 0.2}
#     easy_physical = {'d': 2., 'T_cold': 300.,'T_hot': 450.}

#     # Expected result
#     solution = {'dt': 0.005}

#     # Actual result
#     solver = SolveDiffusion2D()
#     solver.dx = square_domain['dx']
#     solver.dy = square_domain['dy']
#     solver.initialize_physical_parameters(**easy_physical)

#     # Test
#     assert math.isclose(solver.dt, solution['dt']), "dt in initialize_physical_parameters"

# def test_set_initial_condition():
#     """
#     Checks function SolveDiffusion2D.get_initial_function
#     when all points are cold
#     """
#     # Fixture
#     easy_physical = {'d': 2., 'T_cold': 300.,'T_hot': 450.}
#     square_domain = {'w': 1., 'h': 1., 'dx': 0.2, 'dy': 0.2}
#     nx = 5
#     ny = 5

#     # Expected result
#     solution = np.array([[300., 300., 300., 300., 300.],
#                             [300., 300., 300., 300., 300.],
#                             [300., 300., 300., 300., 300.],
#                             [300., 300., 300., 300., 300.],
#                             [300., 300., 300., 300., 300.]])

#     # Actual result
#     solver = SolveDiffusion2D()
#     solver.T_cold = easy_physical['T_cold']
#     solver.T_hot = easy_physical['T_hot']
#     solver.nx = nx
#     solver.ny = ny
#     solver.dx = square_domain['dx']
#     solver.dy = square_domain['dy']
#     result = solver.set_initial_condition()

#     # Test
#     assert np.testing.assert_array_equal(result, solution) is None, "u in set_initial_condition"

############################
####### UNITTEST ###########
############################


class TestDiffusion2D(TestCase):
    def setUp(self):
        # Fixture
        self.solver = SolveDiffusion2D()

        ## domain
        self.rect_case_domain = {'w': 10., 'h': 1., 'dx': 0.1, 'dy': 0.1}
        self.uneven_dx_domain = {'w': 1., 'h': 1., 'dx': 0.16, 'dy': 0.1}
        self.easy_domain = {'w': 1., 'h': 1., 'dx': 1., 'dy': 0.5}
        self.square_domain = {'w': 1., 'h': 1., 'dx': 0.2, 'dy': 0.2}

        ## physical parameters
        self.easy_physical = {'d': 2., 'T_cold': 300.,'T_hot': 450.}

    # Unit test
    def test_initialize_domain_rect(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        for a rectangual domain
        """
        # Expected result
        solution = {'nx': 100,'ny': 10}

        # Actual result
        self.solver.initialize_domain(**self.rect_case_domain)

        # Test
        self.assertAlmostEqual(self.solver.nx, solution['nx'], 5)
        self.assertAlmostEqual(self.solver.ny, solution['ny'], 5)


    # Unit test
    def test_initialize_domain_uneven_dx(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        for an uneven dx
        """
        # Expected result
        solution = {'nx': 6,'ny': 10}

        # Actual result
        self.solver.initialize_domain(**self.uneven_dx_domain)

        # Test
        self.assertAlmostEqual(self.solver.nx, solution['nx'], 5)
        self.assertAlmostEqual(self.solver.ny, solution['ny'], 5)

    # Unit test
    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        for a square case
        """
        # Fixture
        self.solver.dx = self.square_domain['dx']
        self.solver.dy = self.square_domain['dy']

        # Expected result
        solution = {'dt': 0.005}

        # Actual result
        self.solver.initialize_physical_parameters(**self.easy_physical)

        # Test
        self.assertAlmostEqual(self.solver.dt, solution['dt'], 5)

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        when all points are cold
        """
        # Fixture
        self.solver.T_cold = self.easy_physical['T_cold']
        self.solver.T_hot = self.easy_physical['T_hot']
        self.solver.dx = self.square_domain['dx']
        self.solver.dy = self.square_domain['dy']
        self.solver.nx = 5
        self.solver.ny = 5

        # Expected result
        solution = np.array([[300., 300., 300., 300., 300.],
                                [300., 300., 300., 300., 300.],
                                [300., 300., 300., 300., 300.],
                                [300., 300., 300., 300., 300.],
                                [300., 300., 300., 300., 300.]])

        # Actual result
        result = self.solver.set_initial_condition()

        # Test
        self.assertIsNone(np.testing.assert_array_equal(result, solution))

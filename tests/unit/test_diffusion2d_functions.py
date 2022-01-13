"""
Tests for functions in class SolveDiffusion2D
"""
import unittest
from diffusion2d import SolveDiffusion2D

class TestDiffusion2D(unittest.TestCase):

    """
    Parameters to use/check for solver initialization (includes results for the use of further test ste)
    """
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

    def setUp(self):
        self.solver = SolveDiffusion2D


    def init_solver_attrs(self, *categories):
        """
        Initialize solver attributes with fixed values
        """
        for category in categories:
            for key in self.testing_params[category]:
                setattr(self.solver, key, self.testing_params[category][key])


    def check_solver_attrs(self, *categories):
        """
        Check if solver attributes have expected types and values
        """
        for category in categories:
            for key in self.testing_params[category]:
                attr_should = self.testing_params[category][key]
                attr_is = getattr(self.solver, key)

                self.assertEqual(type(attr_should), type(attr_is))
                if type(attr_should) == float:
                    self.assertAlmostEqual(attr_should, attr_is)
                else:
                    self.assertEqual(attr_should, attr_is)


    def test_initialize_domain(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        # somehow need to manually pass the "self" context here?
        self.solver.initialize_domain(
            self.solver,
            self.testing_params['domain']['w'],
            self.testing_params['domain']['h'],
            self.testing_params['domain']['dx'], 
            self.testing_params['domain']['dy']
        )
        self.check_solver_attrs('domain')


    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_physical_parameters
        """
        self.init_solver_attrs('domain')
        self.solver.initialize_physical_parameters(
            self.solver,
            self.testing_params['physical']['D'],
            self.testing_params['physical']['T_cold'],
            self.testing_params['physical']['T_hot'], 
        )        
        self.check_solver_attrs('physical')


    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        self.init_solver_attrs('domain', 'physical')
        u = self.solver.set_initial_condition(self.solver)
        T_cold = self.testing_params['physical']['T_cold']
        T_hot = self.testing_params['physical']['T_hot']

        # Test center of (quarter-)circle for equality to T_hot
        assert u[15, 10] == T_hot

        # Test a few random points outside circle for equality to T_cold
        assert u[0, 0] == T_cold
        assert u[10, 3] == T_cold
        assert u[5, 6] == T_cold

        # Test edge of circle to ensure proper sizing and positioning
        assert u[14, 10] == T_hot and u[13, 10] == T_hot and u[15, 9] == T_hot
        assert u[12, 10] == T_cold and u[13, 9] == T_cold and u[15, 8] == T_cold and u[14, 9] == T_cold


if __name__ == '__main__':
    unittest.main()


    



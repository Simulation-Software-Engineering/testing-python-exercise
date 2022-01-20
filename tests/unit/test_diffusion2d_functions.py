"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import pytest
import numpy as np
import unittest

class TestDiffusion2D(unittest.TestCase):

    def setUp(self) -> None:

        # first solver
        self.solver1 = SolveDiffusion2D()
        self.w1, self.h1, self.dx1, self.dy1 = 20.0, 40.0, 0.1, 0.1
        self.d1, self.T_cold1, self.T_hot1 = 2.5, 200.0, 500.0


        # defining the variables for initialize
        self.nx1 = 200
        self.ny1 = 400

        self.dt1 = 0.001

        # second solver
        self.solver2 = SolveDiffusion2D()
        self.solver2.w, self.solver2.h, self.solver2.dx, self.solver2.dy = 10.0, 12.0, 5.0, 6.0
        self.solver2.d, self.solver2.T_cold, self.solver2.T_hot = 2.5, 200.0, 500.0


        # defining the variables for initialize
        self.solver2.nx = 2
        self.solver2.ny = 2 

        # self dt is not needed


    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        expected_nx = 200
        expected_ny = 400

        self.solver1.initialize_domain(self.w1, self.h1, self.dx1, self.dy1)

        self.assertEqual(self.solver1.nx, expected_nx)
        self.assertEqual(self.solver1.ny, expected_ny) 

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """

        expected_dt = 0.001

        self.solver1.dx = self.dx1
        self.solver1.dy = self.dy1

        self.solver1.initialize_physical_parameters(self.d1, self.T_cold1, self.T_hot1)

        self.assertAlmostEqual(self.solver1.dt, expected_dt, 5)


    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        expected_u = self.solver2.T_cold * np.ones((self.solver2.nx, self.solver2.ny))
        expected_u[1,1] = self.solver2.T_hot

        self.assertTrue((self.solver2.set_initial_condition() == expected_u).all())



#def test_initialize_domain():
    #"""
    #Check function SolveDiffusion2D.initialize_domain
    #"""
    #solver = SolveDiffusion2D()

    #w, h, dx, dy = 20.0, 40.0, 0.1, 0.1
    #expected_nx = 200
    #expected_ny = 400

    #solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)

    #assert solver.nx == expected_nx
    #assert solver.ny == expected_ny


#def test_initialize_physical_parameters():
    #"""
    #Checks function SolveDiffusion2D.initialize_domain
    #"""
    #solver = SolveDiffusion2D()
    #solver.w, solver.h, solver.dx, solver.dy = 20.0, 40.0, 0.1, 0.1
    #d, T_cold, T_hot = 2.5, 200.0, 500.0

    ## defining the variables for initialize
    #solver.nx = 200
    #solver.ny = 400

    #solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)

    #expected_dt = pytest.approx(0.001, abs=0.0001)

    #assert solver.dt == expected_dt


#def test_set_initial_condition():
    #"""
    #Checks function SolveDiffusion2D.get_initial_function
    #"""

    #solver = SolveDiffusion2D()
    #solver.w, solver.h, solver.dx, solver.dy = 10.0, 12.0, 5.0, 6.0
    #solver.d, solver.T_cold, solver.T_hot = 2.5, 200.0, 500.0

    ## defining the variables for initialize
    #solver.nx = 2
    #solver.ny = 2

    #solver.dt = 0.001

    #expected_u = solver.T_cold * np.ones((solver.nx, solver.ny))
    #expected_u[1,1] = solver.T_hot

    #assert (solver.set_initial_condition() == expected_u).all()

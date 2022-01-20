# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

==================================================================================== test session starts =====================================================================================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /home/andrei/Desktop/Simulation Software Engineering/testing-python-exercise
collected 5 items                                                                                                                                                                            

tests/integration/test_diffusion2d.py ..                                                                                                                                               [ 40%]
tests/unit/test_diffusion2d_functions.py FFF                                                                                                                                           [100%]

========================================================================================== FAILURES ==========================================================================================
___________________________________________________________________________________ test_initialize_domain ___________________________________________________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
    
        w, h, dx, dy = 20.0, 40.0, 0.1, 0.1
        expected_nx = 200
        expected_ny = 400
    
        solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
    
>       assert solver.nx == expected_nx
E       assert 400 == 200
E        +  where 400 = <diffusion2d.SolveDiffusion2D object at 0x7f2c3f7015b0>.nx

tests/unit/test_diffusion2d_functions.py:81: AssertionError
____________________________________________________________________________ test_initialize_physical_parameters _____________________________________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.w, solver.h, solver.dx, solver.dy = 20.0, 40.0, 0.1, 0.1
        d, T_cold, T_hot = 2.5, 200.0, 500.0
    
        # defining the variables for initialize
        solver.nx = 200
        solver.ny = 400
    
        solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)
    
        expected_dt = pytest.approx(0.001, abs=0.0001)
    
>       assert solver.dt == expected_dt
E       assert 0.11000000000000001 == 0.001 ± 1.0e-04
E        +  where 0.11000000000000001 = <diffusion2d.SolveDiffusion2D object at 0x7f2c3f701d60>.dt

tests/unit/test_diffusion2d_functions.py:101: AssertionError
------------------------------------------------------------------------------------ Captured stdout call ------------------------------------------------------------------------------------
dt = 0.11000000000000001
_________________________________________________________________________________ test_set_initial_condition _________________________________________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
    
        solver = SolveDiffusion2D()
        solver.w, solver.h, solver.dx, solver.dy = 10.0, 12.0, 5.0, 6.0
        solver.d, solver.T_cold, solver.T_hot = 2.5, 200.0, 500.0
    
        # defining the variables for initialize
        solver.nx = 2
        solver.ny = 2
    
        solver.dt = 0.001
    
        expected_u = solver.T_cold * np.ones((solver.nx, solver.ny))
        expected_u[1,1] = solver.T_hot
    
>       assert (solver.set_initial_condition() == expected_u).all()
E       assert False
E        +  where False = <built-in method all of numpy.ndarray object at 0x7f2c3f6b0930>()
E        +    where <built-in method all of numpy.ndarray object at 0x7f2c3f6b0930> = array([[500.,...[500., 500.]]) == array([[200.,...[200., 500.]])
E             Use -v to get the full diff.all

tests/unit/test_diffusion2d_functions.py:122: AssertionError
================================================================================== short test summary info ===================================================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 400 == 200
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - assert 0.11000000000000001 == 0.001 ± 1.0e-04
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - assert False
================================================================================ 3 failed, 2 passed in 0.82s =================================================================================

### pytest (integration test)

==================================================================================== test session starts =====================================================================================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /home/andrei/Desktop/Simulation Software Engineering/testing-python-exercise
collected 2 items                                                                                                                                                                            

tests/integration/test_diffusion2d.py FF                                                                                                                                               [100%]

========================================================================================== FAILURES ==========================================================================================
____________________________________________________________________________ test_initialize_physical_parameters _____________________________________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
    
        solver = SolveDiffusion2D()
        w, h, dx, dy = 20.0, 40.0, 0.1, 0.1
        d, T_cold, T_hot = 2.5, 200.0, 500.0
    
        solver.initialize_domain(w, h, dx, dy)
        solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)
    
        expected_dt = pytest.approx(0.001, abs=0.0001)
    
>       assert solver.dt == expected_dt
E       assert 0.11000000000000001 == 0.001 ± 1.0e-04
E        +  where 0.11000000000000001 = <diffusion2d.SolveDiffusion2D object at 0x7f63a8ca9e20>.dt

tests/integration/test_diffusion2d.py:24: AssertionError
------------------------------------------------------------------------------------ Captured stdout call ------------------------------------------------------------------------------------
dt = 0.11000000000000001
_________________________________________________________________________________ test_set_initial_condition _________________________________________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        w, h, dx, dy = 10.0, 12.0, 5.0, 6.0
        d, T_cold, T_hot = 2.5, 200.0, 500.0
    
        solver.initialize_domain(w, h, dx, dy)
        solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)
    
        expected_u = solver.T_cold * np.ones((solver.nx, solver.ny))
        expected_u[1,1] = solver.T_hot
    
>       assert (solver.set_initial_condition() == expected_u).all()
E       assert False
E        +  where False = <built-in method all of numpy.ndarray object at 0x7f63a5ac7750>()
E        +    where <built-in method all of numpy.ndarray object at 0x7f63a5ac7750> = array([[500.,...[500., 500.]]) == array([[200.,...[200., 500.]])
E             Use -v to get the full diff.all

tests/integration/test_diffusion2d.py:40: AssertionError
------------------------------------------------------------------------------------ Captured stdout call ------------------------------------------------------------------------------------
dt = 25.118032786885244
================================================================================== short test summary info ===================================================================================
FAILED tests/integration/test_diffusion2d.py::test_initialize_physical_parameters - assert 0.11000000000000001 == 0.001 ± 1.0e-04
FAILED tests/integration/test_diffusion2d.py::test_set_initial_condition - assert False
===================================================================================== 2 failed in 0.78s ======================================================================================


### unittest log

Fdt = 0.11000000000000001
FF
======================================================================
FAIL: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/andrei/Desktop/Simulation Software Engineering/testing-python-exercise/tests/unit/test_diffusion2d_functions.py", line 48, in test_initialize_domain
    self.assertEqual(self.solver1.nx, expected_nx)
AssertionError: 400 != 200

======================================================================
FAIL: test_initialize_physical_parameters (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/andrei/Desktop/Simulation Software Engineering/testing-python-exercise/tests/unit/test_diffusion2d_functions.py", line 63, in test_initialize_physical_parameters
    self.assertAlmostEqual(self.solver1.dt, expected_dt, 5)
AssertionError: 0.11000000000000001 != 0.001 within 5 places (0.10900000000000001 difference)

======================================================================
FAIL: test_set_initial_condition (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.get_initial_function
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/andrei/Desktop/Simulation Software Engineering/testing-python-exercise/tests/unit/test_diffusion2d_functions.py", line 73, in test_set_initial_condition
    self.assertTrue((self.solver2.set_initial_condition() == expected_u).all())
AssertionError: False is not true

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=3)

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

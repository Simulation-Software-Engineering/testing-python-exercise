# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

Functions were intentionally broken in the following manner each time:

 * initialize\_domain: Calculate ny by dividing by dx instead of dy
 * initialize\_physical\_parameters: Add an additional dy2 factor in the divisor of the dt calculation
 * set\_initial\_condition: Multiply T\_cold and T\_hot by 2 before assigning them, as well as the squared radius before using it.

### pytest log

```
========================================== test session starts ==========================================
platform linux -- Python 3.8.10, pytest-4.6.9, py-1.8.1, pluggy-0.13.0
rootdir: /home/geldnens/Documents/carp/bild/2022.1/SSE/repos/testing-python-exercise
collected 5 items                                                                                       

tests/integration/test_diffusion2d.py ..                                                          [ 40%]
tests/unit/test_diffusion2d_functions.py FFF                                                      [100%]

=============================================== FAILURES ================================================
________________________________________ test_initialize_domain _________________________________________

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
>       assert solver.ny == 11
E       assert 13 == 11
E        +  where 13 = <diffusion2d.SolveDiffusion2D object at 0x7fb1c13e8a30>.ny

tests/unit/test_diffusion2d_functions.py:27: AssertionError
__________________________________ test_initialize_physical_parameters __________________________________

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
>       assert abs(solver.dt - .008647059) < 1e-9
E       assert 0.06194117629411765 < 1e-09
E        +  where 0.06194117629411765 = abs((0.07058823529411765 - 0.008647059))
E        +    where 0.07058823529411765 = <diffusion2d.SolveDiffusion2D object at 0x7fb1c13e8160>.dt

tests/unit/test_diffusion2d_functions.py:46: AssertionError
----------------------------------------- Captured stdout call ------------------------------------------
dt = 0.07058823529411765
______________________________________ test_set_initial_condition _______________________________________

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
>       assert u[15, 10] == T_hot
E       assert 1600.0 == 800.0

tests/unit/test_diffusion2d_functions.py:61: AssertionError
----------------------------------------- Captured stdout call ------------------------------------------
dt = 0.07058823529411765
================================== 3 failed, 2 passed in 0.44 seconds ===================================
```

### unittest log

Run using ```python3 -m unittest tests/unit/test_diffusion2d_functions.py```

```
Fdt = 0.07058823529411765
FF
======================================================================
FAIL: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/geldnens/Documents/carp/bild/2022.1/SSE/repos/testing-python-exercise-fork/tests/unit/test_diffusion2d_functions.py", line 64, in test_initialize_domain
    self.check_solver_attrs('domain')
  File "/home/geldnens/Documents/carp/bild/2022.1/SSE/repos/testing-python-exercise-fork/tests/unit/test_diffusion2d_functions.py", line 49, in check_solver_attrs
    self.assertEqual(attr_should, attr_is)
AssertionError: 11 != 13

======================================================================
FAIL: test_initialize_physical_parameters (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.initialize_physical_parameters
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/geldnens/Documents/carp/bild/2022.1/SSE/repos/testing-python-exercise-fork/tests/unit/test_diffusion2d_functions.py", line 78, in test_initialize_physical_parameters
    self.check_solver_attrs('physical')
  File "/home/geldnens/Documents/carp/bild/2022.1/SSE/repos/testing-python-exercise-fork/tests/unit/test_diffusion2d_functions.py", line 47, in check_solver_attrs
    self.assertAlmostEqual(attr_should, attr_is)
AssertionError: 0.008647059 != 0.07058823529411765 within 7 places (0.06194117629411765 difference)

======================================================================
FAIL: test_set_initial_condition (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.get_initial_function
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/geldnens/Documents/carp/bild/2022.1/SSE/repos/testing-python-exercise-fork/tests/unit/test_diffusion2d_functions.py", line 91, in test_set_initial_condition
    assert u[15, 10] == T_hot
AssertionError

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=3)
```

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

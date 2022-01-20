# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

## pytest log

Run pytest with `python3 -m pytest tests/unit/test_diffusion2d_functions.py`.

```python
============================= test session starts =============================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.10.0, pluggy-0.13.1
rootdir: /home/work/Schreibtisch/simulation/testing-python-exercise
plugins: anyio-2.2.0
collected 3 items                                                             

tests/unit/test_diffusion2d_functions.py FFF                            [100%]

================================== FAILURES ===================================
___________________________ test_initialize_domain ____________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        for a rectangual domain
        """
        # Fixture
        rect_case_domain = {'w': 10., 'h': 1., 'dx': 0.1, 'dy': 0.1}
    
        # Expected result
        solution = {'nx': 100,'ny': 10}
    
        # Actual result
        solver = SolveDiffusion2D()
        solver.initialize_domain(**rect_case_domain)
    
        # Test
>       assert math.isclose(solver.nx, solution['nx']), "nx in initialize_domain"
E       AssertionError: nx in initialize_domain
E       assert False
E        +  where False = <built-in function isclose>(10, 100)
E        +    where <built-in function isclose> = math.isclose
E        +    and   10 = <diffusion2d.SolveDiffusion2D object at 0x7f17b2b1be80>.nx

tests/unit/test_diffusion2d_functions.py:30: AssertionError
_____________________ test_initialize_physical_parameters _____________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        for a square case
        """
        # Fixture
        square_domain = {'w': 1., 'h': 1., 'dx': 0.2, 'dy': 0.2}
        easy_physical = {'d': 2., 'T_cold': 300.,'T_hot': 450.}
    
        # Expected result
        solution = {'dt': 0.005}
    
        # Actual result
        solver = SolveDiffusion2D()
        solver.dx = square_domain['dx']
        solver.dy = square_domain['dy']
        solver.initialize_physical_parameters(**easy_physical)
    
        # Test
>       assert math.isclose(solver.dt, solution['dt']), "dt in initialize_physical_parameters"
E       AssertionError: dt in initialize_physical_parameters
E       assert False
E        +  where False = <built-in function isclose>(0.010000000000000002, 0.005)
E        +    where <built-in function isclose> = math.isclose
E        +    and   0.010000000000000002 = <diffusion2d.SolveDiffusion2D object at 0x7f17b2ade4f0>.dt

tests/unit/test_diffusion2d_functions.py:52: AssertionError
---------------------------- Captured stdout call -----------------------------
dt = 0.010000000000000002
_________________________ test_set_initial_condition __________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        when all points are cold
        """
        # Fixture
        easy_physical = {'d': 2., 'T_cold': 300.,'T_hot': 450.}
        square_domain = {'w': 1., 'h': 1., 'dx': 0.2, 'dy': 0.2}
        nx = 5
        ny = 5
    
        # Expected result
        solution = np.array([[300., 300., 300., 300., 300.],
                                [300., 300., 300., 300., 300.],
                                [300., 300., 300., 300., 300.],
                                [300., 300., 300., 300., 300.],
                                [300., 300., 300., 300., 300.]])
    
        # Actual result
        solver = SolveDiffusion2D()
        solver.T_cold = easy_physical['T_cold']
        solver.T_hot = easy_physical['T_hot']
        solver.nx = nx
        solver.ny = ny
        solver.dx = square_domain['dx']
        solver.dy = square_domain['dy']
        result = solver.set_initial_condition()
    
        # Test
>       assert np.testing.assert_array_equal(result, solution) is None, "u in set_initial_condition"
E       AssertionError: 
E       Arrays are not equal
E       
E       Mismatched elements: 25 / 25 (100%)
E       Max absolute difference: 150.
E       Max relative difference: 0.5
E        x: array([[450., 450., 450., 450., 450.],
E              [450., 450., 450., 450., 450.],
E              [450., 450., 450., 450., 450.],...
E        y: array([[300., 300., 300., 300., 300.],
E              [300., 300., 300., 300., 300.],
E              [300., 300., 300., 300., 300.],...

tests/unit/test_diffusion2d_functions.py:83: AssertionError
=========================== short test summary info ===========================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - As...
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition
============================== 3 failed in 0.37s ==============================
```

## unittest log

Run with `python3 -m unittest tests/unit/test_diffusion2d_functions.py`.

```python
F.dt = 0.010000000000000002
FF
======================================================================
FAIL: test_initialize_domain_rect (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/work/Schreibtisch/simulation/testing-python-exercise/tests/unit/test_diffusion2d_functions.py", line 117, in test_initialize_domain_rect
    self.assertAlmostEqual(self.solver.nx, solution['nx'], 5)
AssertionError: 10 != 100 within 5 places (90 difference)

======================================================================
FAIL: test_initialize_physical_parameters (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/work/Schreibtisch/simulation/testing-python-exercise/tests/unit/test_diffusion2d_functions.py", line 154, in test_initialize_physical_parameters
    self.assertAlmostEqual(self.solver.dt, solution['dt'], 5)
AssertionError: 0.010000000000000002 != 0.005 within 5 places (0.005000000000000002 difference)

======================================================================
FAIL: test_set_initial_condition (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.get_initial_function
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/work/Schreibtisch/simulation/testing-python-exercise/tests/unit/test_diffusion2d_functions.py", line 180, in test_set_initial_condition
    self.assertIsNone(np.testing.assert_array_equal(result, solution))
  File "/home/work/.local/lib/python3.8/site-packages/numpy/testing/_private/utils.py", line 934, in assert_array_equal
    assert_array_compare(operator.__eq__, x, y, err_msg=err_msg,
  File "/home/work/.local/lib/python3.8/site-packages/numpy/testing/_private/utils.py", line 844, in assert_array_compare
    raise AssertionError(msg)
AssertionError: 
Arrays are not equal

Mismatched elements: 25 / 25 (100%)
Max absolute difference: 150.
Max relative difference: 0.5
 x: array([[450., 450., 450., 450., 450.],
       [450., 450., 450., 450., 450.],
       [450., 450., 450., 450., 450.],...
 y: array([[300., 300., 300., 300., 300.],
       [300., 300., 300., 300., 300.],
       [300., 300., 300., 300., 300.],...

----------------------------------------------------------------------
Ran 4 tests in 0.011s

FAILED (failures=3)
```

## integration test log

Run with `python3 -m pytest tests/integration/test_diffusion2d.py`.

```python
============================= test session starts =============================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.10.0, pluggy-0.13.1
rootdir: /home/work/Schreibtisch/simulation/testing-python-exercise
plugins: anyio-2.2.0
collected 2 items                                                             

tests/integration/test_diffusion2d.py FF                                [100%]

================================== FAILURES ===================================
_____________________ test_initialize_physical_parameters _____________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        # Fixture
        square_domain = {'w': 1., 'h': 1., 'dx': 0.2, 'dy': 0.2}
        easy_physical = {'d': 2., 'T_cold': 300.,'T_hot': 450.}
    
        # Expected result
        solution = {'dt': 0.005}
    
        # Actual Result
        solver = SolveDiffusion2D()
        solver.initialize_domain(**square_domain)
        solver.initialize_physical_parameters(**easy_physical)
    
        # Test
>       assert math.isclose(solver.dt, solution['dt']), "dt for case 1"
E       AssertionError: dt for case 1
E       assert False
E        +  where False = <built-in function isclose>(0.010000000000000002, 0.005)
E        +    where <built-in function isclose> = math.isclose
E        +    and   0.010000000000000002 = <diffusion2d.SolveDiffusion2D object at 0x7f71a933aac0>.dt

tests/integration/test_diffusion2d.py:27: AssertionError
---------------------------- Captured stdout call -----------------------------
dt = 0.010000000000000002
_________________________ test_set_initial_condition __________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        # Fixture
        square_domain = {'w': 1., 'h': 1., 'dx': 0.2, 'dy': 0.2}
        easy_physical = {'d': 2., 'T_cold': 300.,'T_hot': 450.}
    
        # Expected Result
        solution = np.array([[300., 300., 300., 300., 300.],
                            [300., 300., 300., 300., 300.],
                            [300., 300., 300., 300., 300.],
                            [300., 300., 300., 300., 300.],
                            [300., 300., 300., 300., 300.]])
    
        # Set-up
        solver = SolveDiffusion2D()
        solver.initialize_domain(**square_domain)
        solver.initialize_physical_parameters(**easy_physical)
    
        # Test
        result = solver.set_initial_condition()
>       assert (np.allclose(result, solution)) and result.shape == solution.shape
E       assert (False)
E        +  where False = <function allclose at 0x7f71b329d820>(array([[450., 450., 450., 450., 450.],\n       [450., 450., 450., 450., 450.],\n       [450., 450., 450., 450., 450.],\n       [450., 450., 450., 450., 450.],\n       [450., 450., 450., 450., 450.]]), array([[300., 300., 300., 300., 300.],\n       [300., 300., 300., 300., 300.],\n       [300., 300., 300., 300., 300.],\n       [300., 300., 300., 300., 300.],\n       [300., 300., 300., 300., 300.]]))
E        +    where <function allclose at 0x7f71b329d820> = np.allclose

tests/integration/test_diffusion2d.py:51: AssertionError
---------------------------- Captured stdout call -----------------------------
dt = 0.010000000000000002
=========================== short test summary info ===========================
FAILED tests/integration/test_diffusion2d.py::test_initialize_physical_parameters
FAILED tests/integration/test_diffusion2d.py::test_set_initial_condition - a...
============================== 2 failed in 0.35s ==============================
```

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

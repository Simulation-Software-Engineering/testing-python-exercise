# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

(base) axel@axel:~/Documents/SSE/GitHub/testing-python-exercise$ python -m pytest
============================= test session starts ==============================
platform linux -- Python 3.8.8, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /home/axel/Documents/SSE/GitHub/testing-python-exercise
plugins: anyio-3.4.0
collected 5 items                                                              

tests/integration/test_diffusion2d.py ..                                 [ 40%]
tests/unit/test_diffusion2d_functions.py FFF                             [100%]

=================================== FAILURES ===================================
____________________________ test_initialize_domain ____________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        w = 25.
        h = 4.
        dx = 0.5
        dy = 0.1
        expected_nx = 50
        expected_ny = 40
        solver.initialize_domain(w, h, dx, dy)
>       np.testing.assert_equal(solver.nx, expected_nx)
E       AssertionError:
E       Items are not equal:
E        ACTUAL: 8
E        DESIRED: 50

tests/unit/test_diffusion2d_functions.py:22: AssertionError
_____________________ test_initialize_physical_parameters ______________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        d = 5.
        T_cold = 250.
        T_hot = 850.
        solver.dx = 0.5
        solver.dy = 0.1
        expected_dt = 9.6153846e-04
        solver.initialize_physical_parameters(d, T_cold, T_hot)
>       np.testing.assert_almost_equal(solver.dt, expected_dt, decimal=6)
E       AssertionError:
E       Arrays are not almost equal to 6 decimals
E        ACTUAL: 0.1
E        DESIRED: 0.00096153846

tests/unit/test_diffusion2d_functions.py:38: AssertionError
----------------------------- Captured stdout call -----------------------------
dt = 0.1
__________________________ test_get_initial_condition __________________________

    def test_get_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.T_cold = 250.
        solver.T_hot = 850.
        solver.nx = 3
        solver.ny = 4
        solver.dx = 2.5
        solver.dy = 1.6667

        u_expected = np.array([[250., 250., 250., 250.], [250., 250., 250., 250.], [250., 250., 850., 850.]])
        u_return = solver.get_initial_condition()
>       np.testing.assert_almost_equal(u_return, u_expected)
E       AssertionError:
E       Arrays are not almost equal to 7 decimals
E       
E       Mismatched elements: 1 / 12 (8.33%)
E       Max absolute difference: 600.
E       Max relative difference: 0.70588235
E        x: array([[250., 250., 250., 250.],
E              [250., 250., 250., 250.],
E              [250., 250., 850., 250.]])
E        y: array([[250., 250., 250., 250.],
E              [250., 250., 250., 250.],
E              [250., 250., 850., 850.]])

tests/unit/test_diffusion2d_functions.py:55: AssertionError
=========================== short test summary info ============================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - Ass...
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters
FAILED tests/unit/test_diffusion2d_functions.py::test_get_initial_condition
========================= 3 failed, 2 passed in 1.00s ==========================



### unittest log

(base) axel@axel:~/Documents/SSE/GitHub/testing-python-exercise$ python -m pytest
============================= test session starts ==============================
platform linux -- Python 3.8.8, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /home/axel/Documents/SSE/GitHub/testing-python-exercise
plugins: anyio-3.4.0
collected 5 items                                                              

tests/integration/test_diffusion2d.py ..                                 [ 40%]
tests/unit/test_diffusion2d_functions_unittest.py FFF                    [100%]

=================================== FAILURES ===================================
_____________ TestDiffusion2DFunctions.test_get_initial_condition ______________

self = <test_diffusion2d_functions_unittest.TestDiffusion2DFunctions testMethod=test_get_initial_condition>

    def test_get_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        self.solver.T_cold = 250.
        self.solver.T_hot = 850.
        self.solver.nx = 3
        self.solver.ny = 4
        self.solver.dx = 2.5
        self.solver.dy = 1.6667

        u_expected = np.array([[250., 250., 250., 250.], [250., 250., 250., 250.], [250., 250., 850., 850.]])
        u_return = self.solver.get_initial_condition()
>       np.testing.assert_almost_equal(u_return, u_expected)
E       AssertionError:
E       Arrays are not almost equal to 7 decimals
E       
E       Mismatched elements: 1 / 12 (8.33%)
E       Max absolute difference: 600.
E       Max relative difference: 0.70588235
E        x: array([[250., 250., 250., 250.],
E              [250., 250., 250., 250.],
E              [250., 250., 850., 250.]])
E        y: array([[250., 250., 250., 250.],
E              [250., 250., 250., 250.],
E              [250., 250., 850., 850.]])

tests/unit/test_diffusion2d_functions_unittest.py:55: AssertionError
_______________ TestDiffusion2DFunctions.test_initialize_domain ________________

self = <test_diffusion2d_functions_unittest.TestDiffusion2DFunctions testMethod=test_initialize_domain>

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        w = 25.
        h = 4.
        dx = 0.5
        dy = 0.1
        expected_nx = 50
        expected_ny = 40
        self.solver.initialize_domain(w, h, dx, dy)
>       np.testing.assert_equal(self.solver.nx, expected_nx)
E       AssertionError:
E       Items are not equal:
E        ACTUAL: 8
E        DESIRED: 50

tests/unit/test_diffusion2d_functions_unittest.py:24: AssertionError
_________ TestDiffusion2DFunctions.test_initialize_physical_parameters _________

self = <test_diffusion2d_functions_unittest.TestDiffusion2DFunctions testMethod=test_initialize_physical_parameters>

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        d = 5.
        T_cold = 250.
        T_hot = 850.
        self.solver.dx = 0.5
        self.solver.dy = 0.1
        expected_dt = 9.6153846e-04
        self.solver.initialize_physical_parameters(d, T_cold, T_hot)
>       np.testing.assert_almost_equal(self.solver.dt, expected_dt, decimal=6)
E       AssertionError:
E       Arrays are not almost equal to 6 decimals
E        ACTUAL: 0.1
E        DESIRED: 0.00096153846

tests/unit/test_diffusion2d_functions_unittest.py:39: AssertionError
----------------------------- Captured stdout call -----------------------------
dt = 0.1
=========================== short test summary info ============================
FAILED tests/unit/test_diffusion2d_functions_unittest.py::TestDiffusion2DFunctions::test_get_initial_condition
FAILED tests/unit/test_diffusion2d_functions_unittest.py::TestDiffusion2DFunctions::test_initialize_domain
FAILED tests/unit/test_diffusion2d_functions_unittest.py::TestDiffusion2DFunctions::test_initialize_physical_parameters
========================= 3 failed, 2 passed in 0.92s ==========================



### Integration test logs

(base) axel@axel:~/Documents/SSE/GitHub/testing-python-exercise$ python -m pytest tests/integration/
============================= test session starts ==============================
platform linux -- Python 3.8.8, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /home/axel/Documents/SSE/GitHub/testing-python-exercise
plugins: anyio-3.4.0
collected 2 items                                                              

tests/integration/test_diffusion2d.py FF                                 [100%]

=================================== FAILURES ===================================
_____________________ test_initialize_physical_parameters ______________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        w = 25.
        h = 4.
        dx = 0.5
        dy = 0.1
        d = 5.
        T_cold = 250.
        T_hot = 850.
        expected_dt = 9.6153846e-04
        solver.initialize_domain(w, h, dx, dy)
        solver.initialize_physical_parameters(d, T_cold, T_hot)
>       np.testing.assert_almost_equal(solver.dt, expected_dt)
E       AssertionError:
E       Arrays are not almost equal to 7 decimals
E        ACTUAL: 0.1
E        DESIRED: 0.00096153846

tests/integration/test_diffusion2d.py:24: AssertionError
----------------------------- Captured stdout call -----------------------------
dt = 0.1
__________________________ test_get_initial_condition __________________________

    def test_get_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        w = 10.
        h = 6.6668
        solver.T_cold = 250.
        solver.T_hot = 850.
        solver.nx = 3
        solver.ny = 4
        solver.dx = 2.5
        solver.dy = 1.6667

        u_expected = np.array([[250., 250., 250., 250.], [250., 250., 250., 250.], [250., 250., 850., 850.]])
        u_return = solver.get_initial_condition()
>       np.testing.assert_almost_equal(u_return, u_expected)
E       AssertionError:
E       Arrays are not almost equal to 7 decimals
E       
E       Mismatched elements: 1 / 12 (8.33%)
E       Max absolute difference: 600.
E       Max relative difference: 0.70588235
E        x: array([[250., 250., 250., 250.],
E              [250., 250., 250., 250.],
E              [250., 250., 850., 250.]])
E        y: array([[250., 250., 250., 250.],
E              [250., 250., 250., 250.],
E              [250., 250., 850., 850.]])

tests/integration/test_diffusion2d.py:44: AssertionError
=========================== short test summary info ============================
FAILED tests/integration/test_diffusion2d.py::test_initialize_physical_parameters
FAILED tests/integration/test_diffusion2d.py::test_get_initial_condition - As...
============================== 2 failed in 0.93s ===============================

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

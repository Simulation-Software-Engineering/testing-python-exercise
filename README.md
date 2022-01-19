# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

```
$ python -m pytest
================================================= test session starts =================================================
platform linux -- Python 3.9.6, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /home/max/sse/testing-python-exercise
collected 5 items

tests/integration/test_diffusion2d.py ..                                                                        [ 40%]
tests/unit/test_diffusion2d_functions.py FFF                                                                    [100%]

====================================================== FAILURES =======================================================
_______________________________________________ test_initialize_domain ________________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()

        expected_nx = 6
        expected_ny = 2

        # nx = int(w / dx)
        # ny = int(h / dy)

        solver.initialize_domain(w=9.1, h=6.2, dx=1.4, dy=2.6)

>       assert solver.nx == expected_nx, 'initialize_domain produced wrong nx value'
E       AssertionError: initialize_domain produced wrong nx value
E       assert 4 == 6
E        +  where 4 = <diffusion2d.SolveDiffusion2D object at 0x7f58ab71d640>.nx

tests/unit/test_diffusion2d_functions.py:26: AssertionError
_________________________________________ test_initialize_physical_parameters _________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()

        solver.w = 9.1
        solver.h = 6.2
        solver.dx = 1.3
        solver.dy = 2.6
        solver.nx = 6
        solver.ny = 2

        # dx2, dy2 = self.dx * self.dx, self.dy * self.dy
        # dt = dx2 * dy2 / (2 * self.D * (dx2 + dy2))

        expected_dt = approx(0.25037037037037035)

        solver.initialize_physical_parameters(d=2.7, T_cold=321.3, T_hot=657.4)

>       assert solver.dt == expected_dt
E       assert -0.41728395061728396 == 0.25037037037037035 ± 2.5e-07
E        +  where -0.41728395061728396 = <diffusion2d.SolveDiffusion2D object at 0x7f58ab6e0c40>.dt

tests/unit/test_diffusion2d_functions.py:50: AssertionError
------------------------------------------------ Captured stdout call -------------------------------------------------
dt = -0.41728395061728396
_____________________________________________ test_set_initial_condition ______________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()

        # u = self.T_cold * np.ones((self.nx, self.ny))
        #
        # # Initial conditions - circle of radius r centred at (cx,cy) (mm)
        # r, cx, cy = 2, 5, 5
        # r2 = r ** 2
        # for i in range(self.nx):
        #     for j in range(self.ny):
        #         p2 = (i * self.dx - cx) ** 2 + (j * self.dy - cy) ** 2
        #         if p2 < r2:
        #             u[i, j] = self.T_hot
        #
        # return u.copy()

        solver.w = 9.8
        solver.h = 10.2
        solver.dx = 0.3
        solver.dy = 0.4
        solver.nx = 32
        solver.ny = 25
        solver.D = 6.7
        solver.T_cold = 321.3
        solver.T_hot = 657.4
        solver.dt = 0.004298507462686568

        expected_u = array([
            [321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],
            [321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],
            [321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],
            [321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],
            [321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],
            [321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],
            [321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],
            [321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],
            [321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],
            [321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],
            [321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],
            [321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],
            [321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],
            [321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],
            [321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],
            [321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],
            [321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],
            [321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],
            [321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],
            [321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],
            [321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],
            [321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],
            [321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 657.4, 657.4, 657.4, 657.4, 657.4, 657.4, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],
            [321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 657.4, 657.4, 657.4, 657.4, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],
            [321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],
            [321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],
            [321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],
            [321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],
            [321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],
            [321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],
            [321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],
            [321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3]])

        actual_u = solver.set_initial_condition()
>       assert_allclose(actual_u, expected_u)
E       AssertionError:
E       Not equal to tolerance rtol=1e-07, atol=0
E
E       Mismatched elements: 142 / 800 (17.8%)
E       Max absolute difference: 336.1
E       Max relative difference: 1.04606287
E        x: array([[321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3,
E               321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3,
E               321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],...
E        y: array([[321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3,
E               321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3,
E               321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],...

tests/unit/test_diffusion2d_functions.py:118: AssertionError
=============================================== short test summary info ===============================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - AssertionError: initialize_domain produced...
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - assert -0.41728395061728396 =...
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - AssertionError:
============================================= 3 failed, 2 passed in 0.56s =============================================
```

### unittest log

```
$ python -m unittest tests/unit/test_diffusion2d_functions.py
Fdt = -0.41728395061728396
FF
======================================================================
FAIL: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/max/sse/testing-python-exercise/tests/unit/test_diffusion2d_functions.py", line 30, in test_initialize_domain
    self.assertEqual(self.solver.nx, expected_nx, 'initialize_domain produced wrong nx value')
AssertionError: 4 != 6 : initialize_domain produced wrong nx value

======================================================================
FAIL: test_initialize_physical_parameters (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/max/sse/testing-python-exercise/tests/unit/test_diffusion2d_functions.py", line 51, in test_initialize_physical_parameters
    self.assertEqual(self.solver.dt, expected_dt, 'dt is not calculated correctly')
AssertionError: -0.41728395061728396 != 0.25037037037037035 ± 2.5e-07 : dt is not calculated correctly

======================================================================
FAIL: test_set_initial_condition (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.get_initial_function
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/max/sse/testing-python-exercise/tests/unit/test_diffusion2d_functions.py", line 103, in test_set_initial_condition
    assert_allclose(actual_u, expected_u)
  File "/nix/store/10rxgb060b4l5cp9xjn630qhxvb0ii9z-python3-3.9.6-env/lib/python3.9/site-packages/numpy/testing/_private/utils.py", line 1530, in assert_allclose
    assert_array_compare(compare, actual, desired, err_msg=str(err_msg),
  File "/nix/store/10rxgb060b4l5cp9xjn630qhxvb0ii9z-python3-3.9.6-env/lib/python3.9/site-packages/numpy/testing/_private/utils.py", line 844, in assert_array_compare
    raise AssertionError(msg)
AssertionError:
Not equal to tolerance rtol=1e-07, atol=0

Mismatched elements: 108 / 800 (13.5%)
Max absolute difference: 336.1
Max relative difference: 0.51125646
 x: array([[321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3,
        321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3,
        321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],...
 y: array([[321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3,
        321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3,
        321.3, 321.3, 321.3, 321.3, 321.3, 321.3, 321.3],...

----------------------------------------------------------------------
Ran 3 tests in 0.010s

FAILED (failures=3)
```

Integration test log

```
$ python -m pytest
===================================================== test session starts =====================================================
platform linux -- Python 3.9.6, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /home/max/sse/testing-python-exercise
collected 5 items

tests/integration/test_diffusion2d.py FF                                                                                [ 40%]
tests/unit/test_diffusion2d_functions.py FF.                                                                            [100%]

========================================================== FAILURES ===========================================================
_____________________________________________ test_initialize_physical_parameters _____________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        expected_dt = 0.0532539717274279

        solver = SolveDiffusion2D()
        solver.initialize_domain(w=13., h=7., dx=1.3, dy=1.2)
        solver.initialize_physical_parameters(d=7.3, T_cold=321., T_hot=720.)

>       assert solver.dt == approx(expected_dt)
E       assert 0.6667397260273967 == 0.0532539717274279 ± 5.3e-08
E        +  where 0.6667397260273967 = <diffusion2d.SolveDiffusion2D object at 0x7f74366fe670>.dt
E        +  and   0.0532539717274279 ± 5.3e-08 = approx(0.0532539717274279)

tests/integration/test_diffusion2d.py:21: AssertionError
---------------------------------------------------- Captured stdout call -----------------------------------------------------
dt = 0.6667397260273967
_________________________________________________ test_set_initial_condition __________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        expected_u = [
            [321., 321., 321., 321., 321.],
            [321., 321., 321., 321., 321.],
            [321., 321., 321., 321., 321.],
            [321., 321., 321., 720., 720.],
            [321., 321., 321., 720., 720.],
            [321., 321., 321., 321., 720.],
            [321., 321., 321., 321., 321.],
            [321., 321., 321., 321., 321.],
            [321., 321., 321., 321., 321.],
            [321., 321., 321., 321., 321.],
        ]

        solver = SolveDiffusion2D()

        solver.initialize_domain(w=13., h=7., dx=1.3, dy=1.2)
        solver.initialize_physical_parameters(d=7.3, T_cold=321., T_hot=720.)
        actual_u = solver.set_initial_condition()

>       assert_allclose(actual_u, expected_u)
E       AssertionError:
E       Not equal to tolerance rtol=1e-07, atol=0
E
E       (shapes (5, 5), (10, 5) mismatch)
E        x: array([[321., 321., 321., 321., 321.],
E              [321., 321., 321., 321., 321.],
E              [321., 321., 321., 321., 321.],...
E        y: array([[321., 321., 321., 321., 321.],
E              [321., 321., 321., 321., 321.],
E              [321., 321., 321., 321., 321.],...

tests/integration/test_diffusion2d.py:47: AssertionError
---------------------------------------------------- Captured stdout call -----------------------------------------------------
dt = 0.6667397260273967
___________________________________________ TestDiffusion2D.test_initialize_domain ____________________________________________

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_domain>

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        expected_nx = 6
        expected_ny = 2

        # nx = int(w / dx)
        # ny = int(h / dy)

        self.solver.initialize_domain(w=9.1, h=6.2, dx=1.4, dy=2.6)

>       self.assertEqual(self.solver.nx, expected_nx, 'initialize_domain produced wrong nx value')
E       AssertionError: 4 != 6 : initialize_domain produced wrong nx value

tests/unit/test_diffusion2d_functions.py:30: AssertionError
_____________________________________ TestDiffusion2D.test_initialize_physical_parameters _____________________________________

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_physical_parameters>

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        self.solver.w = 9.1
        self.solver.h = 6.2
        self.solver.dx = 1.3
        self.solver.dy = 2.6
        self.solver.nx = 6
        self.solver.ny = 2

        # dx2, dy2 = self.dx * self.dx, self.dy * self.dy
        # dt = dx2 * dy2 / (2 * self.D * (dx2 + dy2))

        expected_dt = approx(0.25037037037037035)

        self.solver.initialize_physical_parameters(d=2.7, T_cold=321.3, T_hot=657.4)

>       self.assertEqual(self.solver.dt, expected_dt, 'dt is not calculated correctly')
E       AssertionError: -0.41728395061728396 != 0.25037037037037035 ± 2.5e-07 : dt is not calculated correctly

tests/unit/test_diffusion2d_functions.py:51: AssertionError
---------------------------------------------------- Captured stdout call -----------------------------------------------------
dt = -0.41728395061728396
=================================================== short test summary info ===================================================
FAILED tests/integration/test_diffusion2d.py::test_initialize_physical_parameters - assert 0.6667397260273967 == 0.053253971...
FAILED tests/integration/test_diffusion2d.py::test_set_initial_condition - AssertionError:
FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_domain - AssertionError: 4 != 6 : initiali...
FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_physical_parameters - AssertionError: -0.4...
================================================= 4 failed, 1 passed in 0.30s =================================================
```

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

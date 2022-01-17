# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

=================================================================================== test session starts ====================================================================================
platform win32 -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: D:\SSE\test_exercise\testing-python-exercise
collected 5 items

tests\integration\test_diffusion2d.py ..                                                                                                                                              [ 40%]
tests\unit\test_diffusion2d_functions.py F..                                                                                                                                          [100%]

========================================================================================= FAILURES =========================================================================================
__________________________________________________________________________________ test_initialize_domain __________________________________________________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()

        w=20.0
        h=40.0
        dx=0.5
        dy=0.5

        exact_nx=40
        exact_ny=80

        solver.initialize_domain(w,h,dx,dy)

>       assert exact_nx == solver.nx
E       assert 40 == 80
E        +  where 80 = <diffusion2d.SolveDiffusion2D object at 0x0000010862CEA2E0>.nx

tests\unit\test_diffusion2d_functions.py:30: AssertionError
================================================================================= short test summary info ==================================================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 40 == 80
=============================================================================== 1 failed, 4 passed in 1.09s ================================================================================

=================================================================================== test session starts ====================================================================================
platform win32 -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: D:\SSE\test_exercise\testing-python-exercise
collected 5 items

tests\integration\test_diffusion2d.py ..                                                                                                                                              [ 40%]
tests\unit\test_diffusion2d_functions.py FFF                                                                                                                                          [100%]

========================================================================================= FAILURES =========================================================================================
__________________________________________________________________________________ test_initialize_domain __________________________________________________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()

        w=20.0
        h=40.0
        dx=0.1
        dy=0.5

        exact_nx=200
        exact_ny=80

        solver.initialize_domain(w,h,dx,dy)

>       assert exact_nx == solver.nx
E       assert 200 == 400
E        +  where 400 = <diffusion2d.SolveDiffusion2D object at 0x0000023ACB1E8B80>.nx

tests\unit\test_diffusion2d_functions.py:30: AssertionError
___________________________________________________________________________ test_initialize_physical_parameters ____________________________________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_physical_parameters_domain
        """

        solver = SolveDiffusion2D()

        dx=0.1
        dy=0.5
        d=5.

        exact_dt=9.61538*10**(-4)
        tol=10**(-5)

        solver.dx=dx
        solver.dy=dy
        solver.initialize_physical_parameters(d)

        #assertEqual(exact_dt,solver.dt)
>       assert np.abs(exact_dt - solver.dt) < tol
E       AssertionError: assert 0.00046153799999999994 < 1e-05
E        +  where 0.00046153799999999994 = <ufunc 'absolute'>((0.0009615380000000001 - 0.0005000000000000001))
E        +    where <ufunc 'absolute'> = np.abs
E        +    and   0.0005000000000000001 = <diffusion2d.SolveDiffusion2D object at 0x0000023ACB23F5E0>.dt

tests\unit\test_diffusion2d_functions.py:55: AssertionError
----------------------------------------------------------------------------------- Captured stdout call -----------------------------------------------------------------------------------
dt = 0.0005000000000000001
________________________________________________________________________________ test_set_initial_condition ________________________________________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.set_initial_function
        """

        solver = SolveDiffusion2D()

        dx=0.1
        dy=0.5
        nx=40
        ny=80

        T_cold=100.
        T_hot=500.

        exact_u = T_cold * np.ones((nx, ny))
        r, cx, cy = 2, 5, 5
        r2 = r ** 2
        for i in range(nx):
            for j in range(ny):
                p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
                if p2 < r2:
                    exact_u[i, j] = T_hot

        solver.dx=dx
        solver.dy=dy
        solver.nx=nx
        solver.ny=ny
        solver.T_cold=T_cold
        solver.T_hot=T_hot
        actual_u = solver.set_initial_condition()

        for i in range(nx):
            for j in range(ny):
>               assert exact_u[i,j] == actual_u[i,j]
E               assert 500.0 == 100.0

tests\unit\test_diffusion2d_functions.py:92: AssertionError
================================================================================= short test summary info ==================================================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 200 == 400
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - AssertionError: assert 0.00046153799999999994 < 1e-05
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - assert 500.0 == 100.0
=============================================================================== 3 failed, 2 passed in 0.99s ================================================================================

### unittest log

Fdt = 0.0009615384615384617
..
======================================================================
FAIL: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\SSE\test_exercise\testing-python-exercise\tests\unit\test_diffusion2d_functions.py", line 32, in test_initialize_domain
    self.assertEqual(exact_nx,self.solver.nx)
AssertionError: 200 != 400

----------------------------------------------------------------------
Ran 3 tests in 0.006s

FAILED (failures=1)

Fdt = 0.0005000000000000001
FF
======================================================================
FAIL: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\SSE\test_exercise\testing-python-exercise\tests\unit\test_diffusion2d_functions.py", line 32, in test_initialize_domain
    self.assertEqual(exact_nx,self.solver.nx)
AssertionError: 200 != 400

======================================================================
FAIL: test_initialize_physical_parameters (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.initialize_physical_parameters_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\SSE\test_exercise\testing-python-exercise\tests\unit\test_diffusion2d_functions.py", line 51, in test_initialize_physical_parameters
    self.assertAlmostEqual(exact_dt,self.solver.dt,5)
AssertionError: 0.0009615380000000001 != 0.0005000000000000001 within 5 places (0.00046153799999999994 difference)

======================================================================
FAIL: test_set_initial_condition (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.set_initial_function
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\SSE\test_exercise\testing-python-exercise\tests\unit\test_diffusion2d_functions.py", line 86, in test_set_initial_condition
    self.assertEqual(exact_u[i,j], actual_u[i,j])
AssertionError: 100.0 != 500.0

----------------------------------------------------------------------
Ran 3 tests in 0.004s

FAILED (failures=3)

### Integration test log

=================================================================================== test session starts ====================================================================================
platform win32 -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: D:\SSE\test_exercise\testing-python-exercise
collected 5 items

tests\integration\test_diffusion2d.py FF                                                                                                                                              [ 40%]
tests\unit\test_diffusion2d_functions.py FFF                                                                                                                                          [100%]

========================================================================================= FAILURES =========================================================================================
___________________________________________________________________________ test_initialize_physical_parameters ____________________________________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        w=20.0
        h=40.0
        dx=0.1
        dy=0.5
        T_cold=100.
        T_hot=500.
        d=5.

        expect_dt=9.61538*10**(-4)
        tol=10**(-5)

        solver = SolveDiffusion2D()


        solver.initialize_domain(w,h,dx,dy)
        solver.initialize_physical_parameters(d,T_cold,T_hot)

>       assert np.abs(expect_dt-solver.dt) < tol
E       AssertionError: assert 0.00046153799999999994 < 1e-05
E        +  where 0.00046153799999999994 = <ufunc 'absolute'>((0.0009615380000000001 - 0.0005000000000000001))
E        +    where <ufunc 'absolute'> = np.abs
E        +    and   0.0005000000000000001 = <diffusion2d.SolveDiffusion2D object at 0x000002CE434A21C0>.dt

tests\integration\test_diffusion2d.py:29: AssertionError
----------------------------------------------------------------------------------- Captured stdout call -----------------------------------------------------------------------------------
dt = 0.0005000000000000001
________________________________________________________________________________ test_set_initial_condition ________________________________________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """

        w=20.0
        h=40.0
        dx=0.1
        dy=0.5
        nx=40
        ny=80

        T_cold=100.
        T_hot=500.
        d=5.

        exact_u = T_cold * np.ones((nx, ny))
        r, cx, cy = 2, 5, 5
        r2 = r ** 2
        for i in range(nx):
            for j in range(ny):
                p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
                if p2 < r2:
                    exact_u[i, j] = T_hot

        solver = SolveDiffusion2D()
        solver.initialize_domain(w,h,dx,dy)
        solver.initialize_physical_parameters(d,T_cold,T_hot)
        actual_u = solver.set_initial_condition()

        for i in range(nx):
            for j in range(ny):
>               assert exact_u[i,j] == actual_u[i,j]
E               assert 500.0 == 100.0

tests\integration\test_diffusion2d.py:65: AssertionError
----------------------------------------------------------------------------------- Captured stdout call -----------------------------------------------------------------------------------
dt = 0.0005000000000000001
__________________________________________________________________________ TestDiffusion2D.test_initialize_domain __________________________________________________________________________

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_domain>

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """

        w=20.0
        h=40.0
        dx=0.1
        dy=0.5

        exact_nx=200
        exact_ny=80

        self.solver.initialize_domain(w,h,dx,dy)

>       self.assertEqual(exact_nx,self.solver.nx)
E       AssertionError: 200 != 400

tests\unit\test_diffusion2d_functions.py:32: AssertionError
___________________________________________________________________ TestDiffusion2D.test_initialize_physical_parameters ____________________________________________________________________

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_physical_parameters>

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_physical_parameters_domain
        """

        dx=0.1
        dy=0.5
        d=5.

        expect_dt=9.61538*10**(-4)

        self.solver.dx=dx
        self.solver.dy=dy
        self.solver.initialize_physical_parameters(d)

>       self.assertAlmostEqual(expect_dt,self.solver.dt,5)
E       AssertionError: 0.0009615380000000001 != 0.0005000000000000001 within 5 places (0.00046153799999999994 difference)

tests\unit\test_diffusion2d_functions.py:51: AssertionError
----------------------------------------------------------------------------------- Captured stdout call -----------------------------------------------------------------------------------
dt = 0.0005000000000000001
________________________________________________________________________ TestDiffusion2D.test_set_initial_condition ________________________________________________________________________

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_set_initial_condition>

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.set_initial_function
        """

        dx=0.1
        dy=0.5
        nx=40
        ny=80

        T_cold=100.
        T_hot=500.

        exact_u = T_cold * np.ones((nx, ny))
        r, cx, cy = 2, 5, 5
        r2 = r ** 2
        for i in range(nx):
            for j in range(ny):
                p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
                if p2 < r2:
                    exact_u[i, j] = T_hot

        self.solver.dx=dx
        self.solver.dy=dy
        self.solver.nx=nx
        self.solver.ny=ny
        self.solver.T_cold=T_cold
        self.solver.T_hot=T_hot
        actual_u = self.solver.set_initial_condition()

        for i in range(nx):
            for j in range(ny):
>               self.assertEqual(exact_u[i,j], actual_u[i,j])
E               AssertionError: 500.0 != 100.0

tests\unit\test_diffusion2d_functions.py:86: AssertionError
================================================================================= short test summary info ==================================================================================
FAILED tests/integration/test_diffusion2d.py::test_initialize_physical_parameters - AssertionError: assert 0.00046153799999999994 < 1e-05
FAILED tests/integration/test_diffusion2d.py::test_set_initial_condition - assert 500.0 == 100.0
FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_domain - AssertionError: 200 != 400
FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_physical_parameters - AssertionError: 0.0009615380000000001 != 0.0005000000000000001 within 5 places (0....
FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_set_initial_condition - AssertionError: 500.0 != 100.0
==================================================================================== 5 failed in 1.11s =====================================================================================

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

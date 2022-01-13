# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

```
=========================================================== test session starts ===========================================================
platform darwin -- Python 3.7.12, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /Users/jona/Documents/Uni/Master/1_Semester/Simulation_Software_Engineering/testing-python-exercise
plugins: typeguard-2.12.1
collected 5 items                                                                                                                         

tests/integration/test_diffusion2d.py ..                                                                                            [ 40%]
tests/unit/test_diffusion2d_functions.py FFF                                                                                        [100%]

================================================================ FAILURES =================================================================
_________________________________________________________ test_initialize_domain __________________________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
    
        # Expected result
        expected_nx = 250
        expected_ny = 400
    
        # Actual result
        solver.initialize_domain(w=5., h=20., dx=0.02, dy=0.05)
        actual_nx = solver.nx
        actual_ny = solver.ny
    
        # Test
>       assert expected_nx == actual_nx
E       assert 250 == 1000

tests/unit/test_diffusion2d_functions.py:25: AssertionError
___________________________________________________ test_initialize_physical_parameters ___________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
    
        # Expected result
        expected_T_cold = 200.
        expected_T_hot = 600.
        expected_dt = 1/32
    
        # Actual result
        solver.dx = 1
        solver.dy = 1
        solver.initialize_physical_parameters(d=8., T_cold=expected_T_cold, T_hot=expected_T_hot)
        actual_T_cold = solver.T_cold
        actual_T_hot = solver.T_hot
        actual_dt = solver.dt
    
        # Test
        assert expected_T_cold == actual_T_cold
        assert expected_T_hot == actual_T_hot
>       assert expected_dt == actual_dt
E       assert 0.03125 == 0.020833333333333332

tests/unit/test_diffusion2d_functions.py:51: AssertionError
---------------------------------------------------------- Captured stdout call -----------------------------------------------------------
dt = 0.020833333333333332
_______________________________________________________ test_set_initial_condition ________________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
    
        # Expected result
        dx = 0.2
        dy = 0.3
        nx = 100
        ny = 150
        T_cold = 200.
        T_hot = 600.
        expected_u = T_cold * np.ones((nx, ny))
        r, cx, cy = 2, 5, 5
        r2 = r ** 2
        for i in range(nx):
            for j in range(ny):
                p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
                if p2 < r2:
                    expected_u[i, j] = T_hot
    
        # Actual result
        solver.dx = dx
        solver.dy = dy
        solver.nx = nx
        solver.ny = ny
        solver.T_cold = T_cold
        solver.T_hot = T_hot
        actual_u = solver.set_initial_condition()
    
        # Test
        for i in range(nx):
            for j in range(ny):
>               assert expected_u[i,j] == actual_u[i,j]
E               assert 200.0 == 600.0

tests/unit/test_diffusion2d_functions.py:88: AssertionError
========================================================= short test summary info =========================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 250 == 1000
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - assert 0.03125 == 0.020833333333333332
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - assert 200.0 == 600.0
======================================================= 3 failed, 2 passed in 0.74s =======================================================
```

### unittest log

```
Fdt = 0.020833333333333332
FF
======================================================================
FAIL: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestOperations)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/jona/Documents/Uni/Master/1_Semester/Simulation_Software_Engineering/testing-python-exercise/tests/unit/test_diffusion2d_functions.py", line 32, in test_initialize_domain
    self.assertEqual(expected_nx, actual_nx)
AssertionError: 250 != 1000

======================================================================
FAIL: test_initialize_physical_parameters (tests.unit.test_diffusion2d_functions.TestOperations)
Checks function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/jona/Documents/Uni/Master/1_Semester/Simulation_Software_Engineering/testing-python-exercise/tests/unit/test_diffusion2d_functions.py", line 57, in test_initialize_physical_parameters
    self.assertEqual(expected_dt, actual_dt)
AssertionError: 0.03125 != 0.020833333333333332

======================================================================
FAIL: test_set_initial_condition (tests.unit.test_diffusion2d_functions.TestOperations)
Checks function SolveDiffusion2D.get_initial_function
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/jona/Documents/Uni/Master/1_Semester/Simulation_Software_Engineering/testing-python-exercise/tests/unit/test_diffusion2d_functions.py", line 93, in test_set_initial_condition
    self.assertEqual(expected_u[i,j], actual_u[i,j])
AssertionError: 200.0 != 600.0

----------------------------------------------------------------------
Ran 3 tests in 0.027s

FAILED (failures=3)
```

### Integration test log

```
========================================================= test session starts ==========================================================
platform darwin -- Python 3.7.12, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /Users/jona/Documents/Uni/Master/1_Semester/Simulation_Software_Engineering/testing-python-exercise
plugins: typeguard-2.12.1
collected 5 items                                                                                                                      

tests/integration/test_diffusion2d.py FF                                                                                         [ 40%]
tests/unit/test_diffusion2d_functions.py FFF                                                                                     [100%]

=============================================================== FAILURES ===============================================================
_________________________________________________ test_initialize_physical_parameters __________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain()
        solver.initialize_physical_parameters()
    
        # Expected result
        expected_dt = 0.000625
    
        # Actual result
        actual_dt = solver.dt
    
        #Test
>       assert abs(expected_dt - actual_dt) < 1e-5
E       assert 0.0002083333333333332 < 1e-05
E        +  where 0.0002083333333333332 = abs((0.000625 - 0.0004166666666666668))

tests/integration/test_diffusion2d.py:24: AssertionError
--------------------------------------------------------- Captured stdout call ---------------------------------------------------------
dt = 0.0004166666666666668
______________________________________________________ test_set_initial_condition ______________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
    
        # Expected result
        w = 20.
        h = 30.
        dx = 0.5
        dy = 0.2
        nx = 40
        ny = 150
        T_cold = 250.
        T_hot = 900.
        d = 6.
        expected_u0 = T_cold * np.ones((nx, ny))
        r, cx, cy = 2, 5, 5
        r2 = r ** 2
        for i in range(nx):
            for j in range(ny):
                p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
                if p2 < r2:
                    expected_u0[i, j] = T_hot
    
        # Actual result
        solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
        solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)
        actual_u0 = solver.set_initial_condition()
    
        # Test
        for i in range(nx):
            for j in range(ny):
>               assert expected_u0[i,j] == actual_u0[i,j]
E               assert 250.0 == 900.0

tests/integration/test_diffusion2d.py:60: AssertionError
--------------------------------------------------------- Captured stdout call ---------------------------------------------------------
dt = 0.0019157088122605365
________________________________________________ TestOperations.test_initialize_domain _________________________________________________

self = <tests.unit.test_diffusion2d_functions.TestOperations testMethod=test_initialize_domain>

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
    
    
        # Expected result
        expected_nx = 250
        expected_ny = 400
    
        # Actual result
        self.solver.initialize_domain(w=5., h=20., dx=0.02, dy=0.05)
        actual_nx = self.solver.nx
        actual_ny = self.solver.ny
    
        # Test
>       self.assertEqual(expected_nx, actual_nx)
E       AssertionError: 250 != 1000

tests/unit/test_diffusion2d_functions.py:32: AssertionError
__________________________________________ TestOperations.test_initialize_physical_parameters __________________________________________

self = <tests.unit.test_diffusion2d_functions.TestOperations testMethod=test_initialize_physical_parameters>

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
    
        # Expected result
        expected_T_cold = 200.
        expected_T_hot = 600.
        expected_dt = 1/32
    
        # Actual result
        self.solver.dx = 1
        self.solver.dy = 1
        self.solver.initialize_physical_parameters(d=8., T_cold=expected_T_cold, T_hot=expected_T_hot)
        actual_T_cold = self.solver.T_cold
        actual_T_hot = self.solver.T_hot
        actual_dt = self.solver.dt
    
        # Test
        self.assertEqual(expected_T_cold, actual_T_cold)
        self.assertEqual(expected_T_hot, actual_T_hot)
>       self.assertEqual(expected_dt, actual_dt)
E       AssertionError: 0.03125 != 0.020833333333333332

tests/unit/test_diffusion2d_functions.py:57: AssertionError
--------------------------------------------------------- Captured stdout call ---------------------------------------------------------
dt = 0.020833333333333332
______________________________________________ TestOperations.test_set_initial_condition _______________________________________________

self = <tests.unit.test_diffusion2d_functions.TestOperations testMethod=test_set_initial_condition>

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
    
        # Expected result
        dx = 0.2
        dy = 0.3
        nx = 100
        ny = 150
        T_cold = 200.
        T_hot = 600.
        expected_u = T_cold * np.ones((nx, ny))
        r, cx, cy = 2, 5, 5
        r2 = r ** 2
        for i in range(nx):
            for j in range(ny):
                p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
                if p2 < r2:
                    expected_u[i, j] = T_hot
    
        # Actual result
        self.solver.dx = dx
        self.solver.dy = dy
        self.solver.nx = nx
        self.solver.ny = ny
        self.solver.T_cold = T_cold
        self.solver.T_hot = T_hot
        actual_u = self.solver.set_initial_condition()
    
        # Test
        for i in range(nx):
            for j in range(ny):
>               self.assertEqual(expected_u[i,j], actual_u[i,j])
E               AssertionError: 200.0 != 600.0

tests/unit/test_diffusion2d_functions.py:93: AssertionError
======================================================= short test summary info ========================================================
FAILED tests/integration/test_diffusion2d.py::test_initialize_physical_parameters - assert 0.0002083333333333332 < 1e-05
FAILED tests/integration/test_diffusion2d.py::test_set_initial_condition - assert 250.0 == 900.0
FAILED tests/unit/test_diffusion2d_functions.py::TestOperations::test_initialize_domain - AssertionError: 250 != 1000
FAILED tests/unit/test_diffusion2d_functions.py::TestOperations::test_initialize_physical_parameters - AssertionError: 0.03125 != 0.0...
FAILED tests/unit/test_diffusion2d_functions.py::TestOperations::test_set_initial_condition - AssertionError: 200.0 != 600.0
========================================================== 5 failed in 0.52s ===========================================================
```

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

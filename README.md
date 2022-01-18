# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

geistlerji@ubuntu:~/Desktop/testing-python-exercise$ python3 -m pytest
============================= test session starts ==============================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /home/geistlerji/Desktop/testing-python-exercise
collected 5 items                                                              

tests/integration/test_diffusion2d.py ..                                 [ 40%]
tests/unit/test_diffusion2d_functions.py F..                             [100%]

=================================== FAILURES ===================================
____________________________ test_initialize_domain ____________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
    
        solver.initialize_domain(100.0, 200.0, 0.4, 0.2)
    
>       assert solver.nx == 250
E       assert 500 == 250
E        +  where 500 = <diffusion2d.SolveDiffusion2D object at 0x7fa40a63e250>.nx

tests/unit/test_diffusion2d_functions.py:17: AssertionError
=========================== short test summary info ============================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - ass...
========================= 1 failed, 4 passed in 3.63s ==========================


geistlerji@ubuntu:~/Desktop/testing-python-exercise$ python3 -m pytest tests/unit/test_diffusion2d_functions.py 
============================= test session starts ==============================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /home/geistlerji/Desktop/testing-python-exercise
collected 3 items                                                              

tests/unit/test_diffusion2d_functions.py .F.                             [100%]

=================================== FAILURES ===================================
_____________ TestDiffusion2D.test_initialize_physical_parameters ______________

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_physical_parameters>

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        self.solver.dx = 0.4
        self.solver.dy = 0.2
        self.solver.initialize_physical_parameters(self.solver, d=20.0, T_cold=500.0, T_hot=550.0)
    
>       self.assertAlmostEqual(0.0512, self.solver.dt, 5)
E       AssertionError: 0.0512 != 0.0008000000000000001 within 5 places (0.0504 difference)

tests/unit/test_diffusion2d_functions.py:38: AssertionError
----------------------------- Captured stdout call -----------------------------
dt = 0.0008000000000000001
=========================== short test summary info ============================
FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_physical_parameters
========================= 1 failed, 2 passed in 2.06s ==========================



geistlerji@ubuntu:~/Desktop/testing-python-exercise$ python3 -m pytest
============================= test session starts ==============================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /home/geistlerji/Desktop/testing-python-exercise
collected 5 items                                                              

tests/integration/test_diffusion2d.py ..                                 [ 40%]
tests/unit/test_diffusion2d_functions.py ..F                             [100%]

=================================== FAILURES ===================================
__________________________ test_set_initial_condition __________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.T_cold = 500.0
        solver.T_hot = 550.0
        solver.nx = 250
        solver.ny = 1000
        solver.dx = 0.4
        solver.dy = 0.2
    
        manuel_u = 500.0 * np.ones((250, 1000))
        r, cx, cy = 2, 5, 5
        r2 = r ** 2
        for i in range(250):
            for j in range(1000):
                p2 = (i * 0.4 - cx) ** 2 + (j * 0.2 - cy) ** 2
                if p2 < r2:
                    manuel_u[i, j] = 550.0
    
        automated_u = solver.set_initial_condition()
    
        for i in range(250):
                for j in range(1000):
>                    assert manuel_u[i,j]  == automated_u[i,j]
E                    assert 500.0 == 550.0

tests/unit/test_diffusion2d_functions.py:59: AssertionError
=========================== short test summary info ============================
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition
========================= 1 failed, 4 passed in 1.90s ==========================

### unittest log

geistlerji@ubuntu:~/Desktop/testing-python-exercise$ python3 -m unittest tests/unit/test_diffusion2d_functions.py
Fdt = 0.05120000000000004
..
======================================================================
FAIL: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/geistlerji/Desktop/testing-python-exercise/tests/unit/test_diffusion2d_functions.py", line 26, in test_initialize_domain
    self.assertEqual(self.solver.nx, 250)
AssertionError: 500 != 250

----------------------------------------------------------------------
Ran 3 tests in 0.644s

FAILED (failures=1)


geistlerji@ubuntu:~/Desktop/testing-python-exercise$ python3 -m unittest tests/unit/test_diffusion2d_functions.py
.dt = 0.0008000000000000001
F.
======================================================================
FAIL: test_initialize_physical_parameters (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/geistlerji/Desktop/testing-python-exercise/tests/unit/test_diffusion2d_functions.py", line 38, in test_initialize_physical_parameters
    self.assertAlmostEqual(0.0512, self.solver.dt, 5)
AssertionError: 0.0512 != 0.0008000000000000001 within 5 places (0.0504 difference)

----------------------------------------------------------------------
Ran 3 tests in 0.594s

FAILED (failures=1)


geistlerji@ubuntu:~/Desktop/testing-python-exercise$ python3 -m unittest tests/unit/test_diffusion2d_functions.py 
.dt = 0.0008000000000000001
.F
======================================================================
FAIL: test_set_initial_condition (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.get_initial_function
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/geistlerji/Desktop/testing-python-exercise/tests/unit/test_diffusion2d_functions.py", line 67, in test_set_initial_condition
    self.assertEqual(manuel_u[i,j], automated_u[i,j])
AssertionError: 500.0 != 550.0

----------------------------------------------------------------------
Ran 3 tests in 0.302s

FAILED (failures=1)

### integration test log

eistlerji@ubuntu:~/Desktop/testing-python-exercise$ python3 -m pytest tests/integration/test_diffusion2d.py 
============================= test session starts ==============================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /home/geistlerji/Desktop/testing-python-exercise
collected 2 items                                                              

tests/integration/test_diffusion2d.py F.                                 [100%]

=================================== FAILURES ===================================
_____________________ test_initialize_physical_parameters ______________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=100.0, h=200.0, dx=0.4, dy=0.2)
    
        solver.initialize_physical_parameters(d=20.0, T_cold=500.0, T_hot=550.0)
    
>       assert pytest.approx(0.0008, abs=0.00001) == solver.dt
E       assert 0.0008 ± 1.0e-05 == 0.05120000000000004
E        +  where 0.0008 ± 1.0e-05 = <function approx at 0x7f890c510790>(0.0008, abs=1e-05)
E        +    where <function approx at 0x7f890c510790> = pytest.approx
E        +  and   0.05120000000000004 = <diffusion2d.SolveDiffusion2D object at 0x7f8902cc0700>.dt

tests/integration/test_diffusion2d.py:19: AssertionError
----------------------------- Captured stdout call -----------------------------
dt = 0.05120000000000004
=========================== short test summary info ============================
FAILED tests/integration/test_diffusion2d.py::test_initialize_physical_parameters
========================= 1 failed, 1 passed in 1.65s ==========================

geistlerji@ubuntu:~/Desktop/testing-python-exercise$ python3 -m pytest tests/integration/test_diffusion2d.py 
============================= test session starts ==============================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /home/geistlerji/Desktop/testing-python-exercise
collected 2 items                                                              

tests/integration/test_diffusion2d.py .F                                 [100%]

=================================== FAILURES ===================================
__________________________ test_set_initial_condition __________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(100.0, 200.0, 0.4, 0.2)
    
        solver.initialize_physical_parameters(20.0, 500.0, 550.0)
    
        # I feel like this is bad practice because I should calculate these
        # values manualy, but my Input values are to high, so I do it automated ;-)
        manuel_u = 500.0 * np.ones((250, 1000))
        r, cx, cy = 2, 5, 5
        r2 = r ** 2
        for i in range(250):
            for j in range(1000):
                p2 = (i * 0.4 - cx) ** 2 + (j * 0.2 - cy) ** 2
                if p2 < r2:
                    manuel_u[i, j] = 550.0
    
        automated_u = solver.set_initial_condition()
        for i in range(solver.nx):
            for j in range(solver.ny):
>               assert manuel_u[i,j] == automated_u[i,j]
E               IndexError: index 250 is out of bounds for axis 0 with size 250

tests/integration/test_diffusion2d.py:44: IndexError
----------------------------- Captured stdout call -----------------------------
dt = 0.05120000000000004
=========================== short test summary info ============================
FAILED tests/integration/test_diffusion2d.py::test_set_initial_condition - In...
========================= 1 failed, 1 passed in 2.13s ==========================


## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

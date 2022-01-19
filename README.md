# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log
=========================== test session starts ===========================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /home/lmb/SimSE/testing-python-exercise
collected 3 items                                                         

tests/unit/test_diffusion2d_functions.py F..                        [100%]

================================ FAILURES =================================
_________________________ test_initialize_domain __________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        # fixture
        w = 1.
        h = 2.
        dx = 0.2
        dy = 0.5
        # expected result
        expected_nx = 5
        expected_ny = 4
        # actual result
        solver = SolveDiffusion2D()
        solver.initialize_domain(w, h, dx, dy)
        # test
>       assert expected_nx == solver.nx
E       assert 5 == 10
E        +  where 10 = <diffusion2d.SolveDiffusion2D object at 0x7f5b5cdc4a30>.nx

tests/unit/test_diffusion2d_functions.py:26: AssertionError
========================= short test summary info =========================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain
======================= 1 failed, 2 passed in 0.31s =======================

=========================== test session starts ===========================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /home/lmb/SimSE/testing-python-exercise
collected 3 items                                                         

tests/unit/test_diffusion2d_functions.py .F.                        [100%]

================================ FAILURES =================================
___________________ test_initialize_physical_parameters ___________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        # fixture
        solver = SolveDiffusion2D()
        d = 2.
        T_cold = 350.
        T_hot = 420.
        solver.dx = 1.
        solver.dy = 1.
        # expected result
        expected_dt = 0.125
        # actual result
        solver.initialize_physical_parameters(d, T_cold, T_hot)
        # test
        assert expected_dt == solver.dt
>       assert T_cold == solver.T_cold
E       assert 350.0 == 420.0
E        +  where 420.0 = <diffusion2d.SolveDiffusion2D object at 0x7fba53eb4a60>.T_cold

tests/unit/test_diffusion2d_functions.py:47: AssertionError
-------------------------- Captured stdout call ---------------------------
dt = 0.125
========================= short test summary info =========================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters
======================= 1 failed, 2 passed in 0.32s =======================

=========================== test session starts ===========================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /home/lmb/SimSE/testing-python-exercise
collected 3 items                                                         

tests/unit/test_diffusion2d_functions.py ..F                        [100%]

================================ FAILURES =================================
_______________________ test_set_initial_condition ________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        # fixture
        solver = SolveDiffusion2D()
        solver.nx = 2
        solver.ny = 2
        solver.dx = 4.5
        solver.dy = 5.5
        solver.T_cold = 200.
        solver.T_hot = 420.
    
        # expected result
        expected_u = np.array([[200., 200.], [200., 420.]])
        # actual result
        actual_u = solver.set_initial_condition()
        expected_u_approx = pytest.approx(expected_u, abs=0.01)
        # test
>       assert expected_u_approx == actual_u
E       assert approx([[200.0 ± 1.0e-02, 200.0 ± 1.0e-02], [200.0 ± 1.0e-02, 420.0 ± 1.0e-02]]) == array([[420., 420.],\n       [420., 420.]])

tests/unit/test_diffusion2d_functions.py:72: AssertionError
========================= short test summary info =========================
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition
======================= 1 failed, 2 passed in 0.32s =======================


### unittest log

Fdt = 0.125
..
======================================================================
FAIL: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/lmb/SimSE/testing-python-exercise/tests/unit/test_diffusion2d_functions.py", line 29, in test_initialize_domain
    self.assertEqual(self.solver.nx, expected_nx)
AssertionError: 10 != 5

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)

.dt = 0.25
F.
======================================================================
FAIL: test_initialize_physical_parameters (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/lmb/SimSE/testing-python-exercise/tests/unit/test_diffusion2d_functions.py", line 47, in test_initialize_physical_parameters
    self.assertAlmostEqual(expected_dt, self.solver.dt)
AssertionError: 0.125 != 0.25 within 7 places (0.125 difference)

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)

.dt = 0.125
.F
======================================================================
FAIL: test_set_initial_condition (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.get_initial_function
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/lmb/SimSE/testing-python-exercise/tests/unit/test_diffusion2d_functions.py", line 73, in test_set_initial_condition
    self.assertEqual(expected_u[idx_x, idx_y], actual_u[idx_x, idx_y])
AssertionError: 200.0 != 420.0

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)

### pytest integration test logs

=========================== test session starts ===========================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /home/lmb/SimSE/testing-python-exercise
collected 2 items                                                         

tests/integration/test_diffusion2d.py F.                            [100%]

================================ FAILURES =================================
___________________ test_initialize_physical_parameters ___________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        # fixture
        w = 1.
        h = 2.
        d = 2.
        T_cold = 350.
        T_hot = 420.
        dx = 1.
        dy = 0.5
        # expected result
        expected_dt = 0.125
        # actual result
        solver.initialize_domain(w, h, dx, dy)
        solver.initialize_physical_parameters(d, T_cold, T_hot)
        # test
>       assert expected_dt == solver.dt
E       assert 0.125 == 0.05
E        +  where 0.05 = <diffusion2d.SolveDiffusion2D object at 0x7f4a116fd430>.dt

tests/integration/test_diffusion2d.py:28: AssertionError
-------------------------- Captured stdout call ---------------------------
dt = 0.05
========================= short test summary info =========================
FAILED tests/integration/test_diffusion2d.py::test_initialize_physical_parameters
======================= 1 failed, 1 passed in 0.32s =======================

=========================== test session starts ===========================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /home/lmb/SimSE/testing-python-exercise
collected 2 items                                                         

tests/integration/test_diffusion2d.py .F                            [100%]

================================ FAILURES =================================
_______________________ test_set_initial_condition ________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        # fixture
        w = 9.
        h = 11.
        dx = 4.5
        dy = 5.5
        d = 2.
        T_cold = 200.
        T_hot = 420.
    
        # expected result
        nx = int(w/dx)
        ny = int(h/dy)
        expected_u = T_cold * np.ones((nx,ny))
        expected_u[1,1] = T_cold
        # actual result
        solver.initialize_domain(w, h, dx, dy)
        solver.initialize_physical_parameters(d, T_cold, T_hot)
        actual_u = solver.set_initial_condition()
        # expected_u_approx = pytest.approx(expected_u, abs=0.01)
        # test
        # self.assertAlmostEqual(expected_u_approx, actual_u)
        for idx_x in range(solver.nx):
            for idx_y in range(solver.ny):
>               assert expected_u[idx_x, idx_y] == actual_u[idx_x, idx_y]
E               assert 200.0 == 420.0

tests/integration/test_diffusion2d.py:58: AssertionError
-------------------------- Captured stdout call ---------------------------
dt = 3.032487623762376
========================= short test summary info =========================
FAILED tests/integration/test_diffusion2d.py::test_set_initial_condition
======================= 1 failed, 1 passed in 0.32s =======================


## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

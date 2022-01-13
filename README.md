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

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
